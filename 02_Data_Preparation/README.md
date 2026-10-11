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
