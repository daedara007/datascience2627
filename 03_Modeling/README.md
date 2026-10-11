# 🤖 Bab 4 - Pemodelan & Evaluasi Klasifikasi

Direktori ini disiapkan untuk tahapan **Modeling (Bab 4)** dan **Evaluation (Bab 5)**.

---

## 📋 Panduan Pengerjaan untuk Anggota Tim:

1. **Dataset Acuan**:
   * Gunakan dataset bersih hasil penyeimbangan kelas dari folder Data Preparation:
     `../02_Data_Preparation/dataset_balanced.csv` (216.624 baris seimbang, 0 missing value).
   * Atau dataset distribusi asli tanpa missing value:
     `../02_Data_Preparation/dataset_imputed.csv` (100.000 baris, 0 missing value) untuk perbandingan (*A/B testing* performa model sebelum vs sesudah SMOTE).

2. **Rekomendasi Algoritma Klasifikasi**:
   * **Baseline**: Logistic Regression / Decision Tree.
   * **Ensemble Tree**: Random Forest Classifier, XGBoost, LightGBM, CatBoost.

3. **Metrik Evaluasi Sesuai Rubrik**:
   * **Macro F1-Score** (Target $\ge 85\%$).
   * **Confusion Matrix** (4 kelas: *Healthy*, *Mild*, *Moderate*, *Severe*).
   * **Recall khusus kelas kritis** (*Moderate* dan *Severe*) untuk meminimalkan *False Negative* pada risiko tinggi.
