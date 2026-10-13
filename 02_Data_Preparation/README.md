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
ulang dataset mentah. Urutannya: split stratified 80/20 → imputasi, Yeo-Johnson, dan RobustScaler
berdasarkan train → SMOTE-NC hanya pada train → One Hot Encoding 7 fitur teks.
Empat fitur biner tetap 0/1; `person_id` dan target tidak masuk fitur model.
Baseline numerik menggunakan imputasi median → Yeo-Johnson → RobustScaler. Encoder menggunakan
`handle_unknown='ignore'`, `drop=None`, dan output sparse float32.

Artefak di `artifacts_ohe/`:
- `X_train_encoded.npz`, `X_test_encoded.npz`: matriks fitur sparse.
- `y_train.csv`, `y_test.csv`: label sesuai urutan baris matriks.
- `feature_names.json`: nama dan urutan fitur.
- `preprocessing.joblib`: imputer, Yeo-Johnson, scaler, dan encoder untuk inference.
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
mem-fit ulang imputasi, Yeo-Johnson, scaling, encoding, seleksi, dan Logistic Regression
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

Scaling menggunakan **RobustScaler** pada 19 fitur numerik: median nilai train setelah Yeo-Johnson sebagai
pusat dan IQR-nya (P75 − P25) sebagai skala. Statistik ini lebih tahan terhadap
nilai ekstrem, sesuai keputusan mempertahankan outlier. Fitur biner dan One Hot
Encoding tetap 0/1. Scaling tidak menghapus outlier dan hanya di-fit pada train
atau bagian train di setiap fold CV. Konfigurasi scaler dicatat dalam metadata.

## Transformasi Numerik: Yeo-Johnson

Yeo-Johnson diterapkan pada 19 fitur numerik setelah imputasi dan sebelum
RobustScaler, untuk mengurangi kemencengan distribusi. Metode ini mendukung
nilai positif, nol, dan negatif; fitur biner/kategori dan target tetap utuh.
`PowerTransformer(method='yeo-johnson', standardize=False)` digunakan agar
scaling ditangani oleh RobustScaler. Parameter transformasi dipelajari hanya
dari train atau bagian train di setiap fold CV.

`artifacts_ohe/transformation_audit.csv` mencatat lambda dan skewness sebelum
serta sesudah transformasi pada train asli. Transformasi tidak menjamin semua
fitur menjadi normal atau performa meningkat; hasil CV dan audit menjadi
bahan evaluasi. ANOVA dihitung ulang karena transformasi nonlinear dapat
mengubah skor F; Chi-square tetap hanya menerima kolom kategori/biner.

## PCA: Reduksi Dimensi

Jalankan **bagian 9** setelah bagian 7–8. PCA membentuk komponen gabungan dari
fitur yang lolos ANOVA + Chi-square. `PCA(n_components=0.95, svd_solver='full',
whiten=False)` di-fit pada train asli sebelum SMOTE-NC; train balanced dan test
hanya ditransformasi. Numerik sudah memakai Yeo-Johnson + RobustScaler, dan
indikator kategori/biner tetap 0/1. PCA melakukan centering, tanpa scaling
tambahan pada dummy. Kontribusi kategori langka dapat menjadi kecil karena
PCA mempertimbangkan variansi, bukan relevansi target.

Threshold 95% menyatakan variansi train yang dipertahankan, bukan akurasi.
CV membandingkan baseline tanpa PCA dengan PCA 95%, mem-fit ulang seluruh
tahap dalam setiap fold train. Test disimpan untuk evaluasi final. Matriks
tanpa PCA tetap tersedia karena reduksi dimensi tidak menjamin peningkatan
prediksi atau interpretabilitas.

`artifacts_pca/` berisi matriks dense `.npy` untuk train asli, train balanced,
dan test, label berurutan sama, nama komponen, explained variance, koefisien
komponen, hasil CV, preprocessing lengkap, dan metadata. Gunakan
`X_train_original_pca.npy` bersama `y_train_original.csv` untuk baseline
berbobot kelas. Muat matriks dengan `numpy.load`; untuk data baru, transformasi
imputasi/Yeo-Johnson/scaling → encoding → indeks fitur terpilih → PCA.

Hasil saat ini: PCA mereduksi 49 kolom menjadi **31 komponen** dengan
**95,20% variansi train**. Macro-F1 CV turun dari **0,67046** menjadi **0,64641**,
dan recall Severe dari **0,74455** menjadi **0,72733**. Gunakan baseline tanpa
PCA sebagai pilihan utama saat ini; PCA disimpan sebagai alternatif eksperimen.
