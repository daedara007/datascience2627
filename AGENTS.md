# AGENTS.md - Catatan Progress Proyek Sains Data
> **Mata Kuliah**: IF2515403 - Sains Data (Semester 5, ITK)
> **Topik**: Klasifikasi Risiko Gangguan Tidur Berdasarkan Pola Hidup dan Biometrik
> **Dosen**: Ramadhan Paninggalih
> **Deadline**: UTS (Bab 1-3), UAS (Bab 1-5 penuh)
> **Pembagian Jobdesk Anggota**: Khusus **Penanganan Missing Values** dan **Penanganan Ketidakseimbangan Data (Class Imbalance)**

---

## STRUKTUR WORKSPACE & FILE UTAMA

```
datascience2627/
├── Sains_data.ipynb             # Notebook Utama: Bab 1 (Business Understanding) & Bab 2 (Data Understanding)
├── dataset_GANGGUAN_TIDUR.csv   # Dataset mentah tugas (100.000 baris x 32 kolom, ada 10% NaN per kolom)
├── data prep/                   # Folder Khusus Tahap Penyiapan Data (Bab 3)
│   ├── data_preparation.ipynb  # Notebook Bab 3: Khusus Jobdesk Missing Values & Imbalanced Data
│   ├── dataset_imputed.csv      # Dataset hasil imputasi utuh (100.000 baris x 31 kolom, 0 missing)
│   └── dataset_balanced.csv     # Dataset seimbang hasil resampling (216.624 baris x 31 kolom, 0 missing)
├── by team/                     # Berkas kolaborasi kelompok
│   └── data-sains.ipynb         # Eksplorasi Data Understanding (Bab 2) tim
├── reference/                   # Sumber Referensi Benchmark Kaggle
│   ├── sleep_health_dataset.csv # Dataset asli Kaggle (100.000 baris, 0 missing value - Ground Truth)
│   └── sleep-health-cognitive-performance-analysis.ipynb # Notebook analisis referensi Kaggle
└── AGENTS.md                    # Catatan dokumentasi & tracking progres proyek
```

---

## SETUP & ENVIRONMENT

| Item | Detail |
|:---|:---|
| **Python Env** | Virtual Environment di `./.venv` |
| **Kernel Notebook** | `.venv` (Python 3.12) |
| **Library Utama** | `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `imbalanced-learn`, `nbformat` |
| **Path Relatif** | Dataset mentah: `dataset_GANGGUAN_TIDUR.csv` (root) atau `../dataset_GANGGUAN_TIDUR.csv` (dari `data prep/`) |

---

## TENTANG DATASET & STATUS PENGERJAAN JOBDESK

| Properti | Nilai Mentah | Hasil Imputasi (`dataset_imputed.csv`) | Hasil Penyeimbangan (`dataset_balanced.csv`) |
|:---|:---|:---|:---|
| Baris | 100.000 observasi unik | 100.000 observasi unik | 216.624 observasi (seimbang) |
| Kolom | 31 fitur + 1 target (`sleep_disorder_risk`) | 31 fitur + 1 target (32 kolom utuh) | 31 fitur + 1 target (32 kolom utuh) |
| Missing Values | **310.000 sel (10% di 31 kolom)** | **0 sel kosong (100% lengkap)** | **0 sel kosong (100% lengkap)** |
| Identifier | Kolom `person_id` ada | Dipertahankan utuh (rekonstruksi urut `index + 1`) | Dipertahankan utuh |
| Target Kelas | 4 kategori: Healthy, Mild, Moderate, Severe | 4 kategori (distribusi asli) | 4 kategori seimbang (25% per kelas) |
| Proporsi Target | Healthy ~54.2%, Mild ~33.5%, Moderate ~8.3%, Severe ~4.0% | Healthy: 54.156, Mild: 33.479, Mod: 8.299, Sev: 4.066 | Masing-masing kelas 54.156 sampel (25.0%) |

### Kategori Fitur:
- **Demografi**: `age`, `gender`, `occupation`, `country`
- **Biometrik**: `bmi`, `heart_rate_resting_bpm`
- **Pola Tidur**: `sleep_duration_hrs`, `sleep_quality_score`, `rem_percentage`, `deep_sleep_percentage`, `sleep_latency_mins`, `wake_episodes_per_night`, `nap_duration_mins`, `weekend_sleep_diff_hrs`, `felt_rested`
- **Gaya Hidup**: `caffeine_mg_before_bed`, `alcohol_units_before_bed`, `screen_time_before_bed_mins`, `exercise_day`, `steps_that_day`
- **Psikologis & Kerja**: `stress_score`, `mental_health_condition`, `work_hours_that_day`, `shift_work`
- **Sirkadian/Lingkungan**: `chronotype`, `room_temperature_celsius`, `season`, `day_type`
- **Kognitif & Medis**: `cognitive_performance_score`, `sleep_aid_used`
- **Identifier**: `person_id` (dipertahankan untuk tahap Feature Selection rekan tim)

---

## STATUS PROGRES & RUBRIK PENILAIAN UTS (Bab 1 - 3)

### Bab 1 - Business Understanding (`Sains_data.ipynb`)
| Kriteria | Skor Target | Status | Catatan |
|:---|:---:|:---:|:---|
| Latar Belakang Masalah | 5 | SELESAI | Konteks masalah tidur & dampak kognitif/akademik |
| Rumusan Masalah | 5 | SELESAI | Spesifik, terukur untuk klasifikasi 4 tingkat risiko |
| Tujuan Analisis | 5 | SELESAI | Sistem klasifikasi & pipeline CRISP-DM terstandarisasi |
| Kriteria Kesuksesan | 5 | SELESAI | Ambang batas akurasi, F1-macro $\ge 85\%$ |

### Bab 2 - Data Understanding (`Sains_data.ipynb` / `by team/data-sains.ipynb`)
| Kriteria | Skor Target | Status | Catatan |
|:---|:---:|:---:|:---|
| $\ge 20$ Sampel Data | 5 | SELESAI | Ditampilkan via `.sample(20)` |
| Kamus Data 32 Fitur | 5 | SELESAI | Tabel deskripsi atribut & tipe data lengkap |
| Statistik Deskriptif | 5 | SELESAI | `.describe(include='all').T` rapi tanpa terpotong |
| Visualisasi Distribusi & Skewness | 5 | SELESAI | Histogram + Tabel analisis skewness 13 fitur |
| Korelasi Antar Fitur (Heatmap) | 5 | SELESAI | Heatmap korelasi matriks numerik |
| Validasi Missing, Duplikasi, Outlier | 5 | SELESAI | Deteksi 10% NaN, 0 duplikat, dan deteksi outlier IQR & Z-score |
| Pie Chart, Bar Chart, Scatter Plot | 5 | SELESAI | Proporsi kelas, gender, scatter durasi vs stres & screen time |
| Bivariate Boxplot (Fitur vs Target) | 5 | SELESAI | Visualisasi boxplot per kelas target tersedia |
| Rangkuman Insight Awal | 5 | SELESAI | Kesimpulan awal pemandu Data Preparation |

### Bab 3 - Data Preparation (`data prep/data_preparation.ipynb` - Jobdesk Personal)
| Tahapan | Detail | Status | Penanggung Jawab |
|:---|:---|:---:|:---|
| **Retensi Objek & Integritas** | Mempertahankan 32 kolom utuh (retensi `person_id` untuk Feature Selection rekan tim) & 0 duplikasi | SELESAI | Jobdesk Personal |
| **Handling Missing Values** | Rekonstruksi urut `person_id` (`index + 1`) + **KNN Imputer ($k=5$)** untuk 23 numerik + **Modus** untuk 7 kategorik | SELESAI | **Jobdesk Personal (Tugas 1)** |
| **Handling Outliers** | Audit kuantitatif & visualisasi sebaran ekstrem (Retensi Alami / Keep As-Is untuk baseline model Bab 4) | SELESAI | **Jobdesk Personal & Tim** |
| **Handling Imbalanced Data** | Analisis ketimpangan kelas target + **SMOTE-NC** ke 54.156 per kelas | SELESAI | **Jobdesk Personal (Tugas 2)** |
| **Ekspor Berkas Hasil** | `dataset_imputed.csv` (100k baris x 32 kolom) & `dataset_balanced.csv` (216k baris x 32 kolom) | SELESAI | **Jobdesk Personal** |
| *Feature Selection* | Eliminasi `person_id` dan seleksi fitur paling informatif | *Tahap Tim Lain* | Anggota Tim Lain |
| *Feature Engineering* | Pembentukan fitur komposit domain medis | *Tahap Tim Lain* | Anggota Tim Lain |
| *Feature Encoding* | Ordinal / One-Hot Encoding fitur non-numerik | *Tahap Tim Lain* | Anggota Tim Lain |
| *Feature Scaling & PCA* | Standardisasi & reduksi dimensi | *Tahap Tim Lain* | Anggota Tim Lain |

---

## KEPUTUSAN & KONVENSI TEKNIS JOBDESK

| Keputusan | Alasan |
|:---|:---|
| **Retensi Kolom `person_id` (32 Kolom Utuh)** | Menjaga agar porsi tugas rekan tim pada tahap *Feature Selection* tidak terlangkahi. Nilai hilang pada `person_id` direkonstruksi secara eksak sesuai urutan indeks (`index + 1`). |
| **KNN Imputer ($k=5$) untuk Fitur Numerik** | Memanfaatkan kemiripan multivariat profil responden (bukan angka rata-rata/median tunggal). Dioptimasi dengan batch processing 20.000 baris agar cepat (~45 detik) dan hemat RAM. |
| **Modus untuk Fitur Kategorikal String** | Menjaga integritas label kategori (`gender`, `occupation`, dll.) tanpa memaksakan kalkulasi numerik. |
| **Retensi Outlier Alami (Keep As-Is) untuk Baseline Model** | Nilai ekstrem pada biometrik pasien kritis (*Severe*) merupakan sinyal patologis nyata, bukan kesalahan input. Algoritma pohon (Random Forest/XGBoost) kebal outlier univariat. Data dipertahankan murni (*as-is*) sebagai baseline benchmark, dengan opsi A/B testing di Bab 4. |
| **SMOTE-NC untuk Imbalanced Data** | Menghasilkan sampel sintetis realistis via interpolasi $k$-NN kontinu pada fitur numerik, sekaligus menjaga integritas label kategori teks via modus tetangga terdekat. `person_id` direkonstruksi berurutan sehingga seluruh 32 kolom awal tetap utuh dan selaras untuk alur kerja rekan tim berikutnya. |
| **Ekspor Dua File Artefak 32 Kolom** | Menyediakan `dataset_imputed.csv` (distribusi asli) dan `dataset_balanced.csv` (distribusi seimbang) lengkap 32 kolom agar rekan kelompok memiliki fleksibilitas penuh dalam alur pemodelan mereka. |

---

## ROADMAP & RENCANA TAHAP SELANJUTNYA

### 1. Serah Terima Data ke Anggota Kelompok
* [x] Selesaikan pipeline imputasi KNN & penyeimbangan kelas di [data_preparation.ipynb](file:///d:/kevin/Documents/ITK/Semester%205/Sains%20Data/data%20prep/data_preparation.ipynb)
* [x] Generate file [dataset_imputed.csv](file:///d:/kevin/Documents/ITK/Semester%205/Sains%20Data/data%20prep/dataset_imputed.csv) dan [dataset_balanced.csv](file:///d:/kevin/Documents/ITK/Semester%205/Sains%20Data/data%20prep/dataset_balanced.csv)
* [ ] Koordinasi dengan rekan tim yang menangani *outlier*, *feature engineering*, dan *encoding*

### 2. Persiapan Bab 4 - Modeling & Evaluasi (Bersama Kelompok)
* Pengujian algoritma klasifikasi (Random Forest, XGBoost, LightGBM)
* Evaluasi metrik (Confusion Matrix, Macro F1-Score $\ge 85\%$, Recall kelas kritis *Severe* dan *Moderate*)
