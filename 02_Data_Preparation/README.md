# 🛠️ Bab 3 - Penyiapan Data (Data Preparation)

Direktori ini berisi implementasi pipeline penyiapan data sesuai metodologi CRISP-DM:
* **Penanganan Missing Values**: Rekonstruksi `person_id`, KNN Imputer ($k=5$) untuk 23 fitur numerik, dan Modus untuk 7 fitur kategorikal.
* **Audit Outliers**: Analisis distribusi dan identifikasi outlier tanpa pemangkasan data valid biometrik.
* **Penanganan Ketidakseimbangan Kelas**: Algoritma **SMOTE-NC** menyeimbangkan 4 kelas target (*Healthy*, *Mild*, *Moderate*, *Severe*) dari 100k observasi menjadi 216.624 observasi seimbang (54.156 per kelas).

---

## 📂 Berkas Modul

* **`data_preparation.ipynb`**: Notebook Jupyter pipeline penyiapan data lengkap dari pemuatan data mentah hingga ekspor artefak.
* **`dataset_imputed.csv`**: Dataset hasil imputasi lengkap tanpa missing values (100.000 baris x 32 kolom).
* **`dataset_balanced.csv`**: Dataset hasil imputasi dan penyeimbangan kelas SMOTE-NC (216.624 baris x 32 kolom seimbang).

## One Hot Encoding untuk Modeling

Jalankan **bagian 7** notebook dari sel import-nya; bagian ini mandiri dan membaca
ulang dataset mentah. Urutannya: split stratified 80/20 → imputasi dan scaling
berdasarkan train → SMOTE-NC hanya pada train → One Hot Encoding 7 fitur teks.
Empat fitur biner tetap 0/1; `person_id` dan target tidak masuk fitur model.
Baseline numerik menggunakan median dan StandardScaler. Encoder menggunakan
`handle_unknown='ignore'`, `drop=None`, dan output sparse float32.

Artefak di `artifacts_ohe/`:
- `X_train_encoded.npz`, `X_test_encoded.npz`: matriks fitur sparse.
- `y_train.csv`, `y_test.csv`: label sesuai urutan baris matriks.
- `feature_names.json`: nama dan urutan fitur.
- `preprocessing.joblib`: imputer, scaler, dan encoder untuk inference.
- `metadata.json`: konfigurasi split, skema input, dimensi, dan versi pustaka.

**Evaluasi:** `dataset_imputed.csv` dan `dataset_balanced.csv` merupakan artefak
alur eksplorasi lama yang diproses sebelum split; jangan memakainya untuk
mengukur performa holdout. Untuk cross-validation atau tuning, fit imputasi,
scaling, SMOTE-NC, dan encoding dalam setiap fold memakai imblearn Pipeline;
jangan melakukan cross-validation pada matriks yang sudah di-resample.

Dependensi bagian 7: pandas, numpy, scipy, scikit-learn >= 1.2,
imbalanced-learn yang kompatibel, dan joblib. Gunakan versi environment yang
tercatat dalam metadata saat memuat preprocessing.

## Feature Selection: ANOVA + Chi-square

Jalankan **bagian 8** setelah bagian 7. ANOVA mengukur perbedaan rata-rata
19 fitur numerik antarkelas. Chi-square mengukur hubungan 47 kolom indikator
kategori/biner dengan target; fitur numerik hasil scaling yang bisa negatif tidak
dimasukkan ke Chi-square. Skor kedua metode diurutkan terpisah. Alasan,
asumsi, dan batasan interpretasi p-value dijelaskan di notebook.

Jumlah fitur dipilih dengan 3-fold stratified cross-validation pada train
mentah, membandingkan 50%, 75%, dan 100% fitur pada setiap kelompok. Setiap fold
mem-fit ulang imputasi, scaling, encoding, seleksi, dan Logistic Regression
berbobot kelas. Macro-F1 menentukan konfigurasi terbaik; recall Severe juga
dilaporkan. Seleksi di-refit pada train asli sebelum SMOTE-NC dan tidak memakai
test. Seleksi terjadi pada level kolom hasil encoding, bukan kelompok fitur asli.

`artifacts_feature_selection/` berisi ranking ANOVA/Chi-square, hasil CV,
daftar fitur terpilih, matriks train asli/train balanced/test dengan label
berurutan sama, preprocessing untuk inference, metadata, dan pipeline baseline.
Untuk baseline berbobot kelas, gunakan `X_train_original_selected.npz` dengan
`y_train_original.csv`. Matriks balanced tersedia untuk eksperimen model lain;
validasi ulang pilihan fitur dalam CV jika model atau resampling berubah.
Test tetap disimpan untuk evaluasi final di tahap modeling.
