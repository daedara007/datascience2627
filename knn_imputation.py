"""Train-only KNN imputation with scaled distances and sampled donors.

Import this module from the project root before loading preprocessing.joblib.
"""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from sklearn.utils.validation import check_is_fitted, validate_data


class ScaledKNNImputer(TransformerMixin, BaseEstimator):
    """Impute continuous features, preserving observed values and original units.

    A RobustScaler learns distance scales from observed training values.
    Donors are sampled only from the supplied training partition. Transform
    batches change memory usage, not the donor population or fitted statistics.
    """

    def __init__(self, n_neighbors=5, max_donors=10000, batch_size=5000,
                 weights='uniform', random_state=42):
        self.n_neighbors = n_neighbors
        self.max_donors = max_donors
        self.batch_size = batch_size
        self.weights = weights
        self.random_state = random_state

    def fit(self, X, y=None):
        if self.max_donors < 1 or self.batch_size < 1:
            raise ValueError('max_donors and batch_size must be positive.')
        data = validate_data(self, X, dtype=np.float64,
                             ensure_all_finite='allow-nan')
        if np.isnan(data).all(axis=0).any():
            raise ValueError('A continuous feature is entirely missing in train.')
        self.distance_scaler_ = RobustScaler().fit(data)
        count = min(self.max_donors, len(data))
        self.donor_positions_ = np.random.RandomState(self.random_state).choice(
            len(data), size=count, replace=False
        )
        self.n_training_samples_ = len(data)
        self.n_donors_ = count
        donors = self.distance_scaler_.transform(data[self.donor_positions_])
        if np.isnan(donors).all(axis=0).any():
            raise ValueError('A sampled donor feature is entirely missing; increase max_donors.')
        self.imputer_ = KNNImputer(n_neighbors=self.n_neighbors,
                                  weights=self.weights,
                                  keep_empty_features=True).fit(donors)
        return self

    def transform(self, X):
        check_is_fitted(self, ['distance_scaler_', 'imputer_'])
        data = validate_data(self, X, reset=False, dtype=np.float64,
                             ensure_all_finite='allow-nan')
        result = np.empty_like(data)
        for start in range(0, len(data), self.batch_size):
            batch = data[start:start + self.batch_size]
            scaled = self.distance_scaler_.transform(batch)
            completed = self.imputer_.transform(scaled)
            restored = self.distance_scaler_.inverse_transform(completed)
            # Avoid roundoff changes to values originally observed.
            observed = ~np.isnan(batch)
            restored[observed] = batch[observed]
            result[start:start + len(batch)] = restored
        return result

    def get_feature_names_out(self, input_features=None):
        check_is_fitted(self, 'n_features_in_')
        if input_features is not None:
            names = np.asarray(input_features, dtype=object)
            if len(names) != self.n_features_in_:
                raise ValueError('Feature count does not match fitted input.')
            return names
        if hasattr(self, 'feature_names_in_'):
            return self.feature_names_in_.copy()
        return np.asarray([f'x{i}' for i in range(self.n_features_in_)], dtype=object)
