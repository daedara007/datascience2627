# AGENTS.md - Catatan Progress Proyek Sains Data
> **Mata Kuliah**: IF2515403 - Sains Data (Semester 5, ITK)
> **Topik**: Klasifikasi Risiko Gangguan Tidur Berdasarkan Pola Hidup dan Biometrik
> **File Utama**: `Sains_data.ipynb`
> **Dataset**: `dataset_GANGGUAN_TIDUR.csv` (100.002 baris x 32 kolom)
> **Dosen**: Ramadhan Paninggalih
> **Deadline**: UTS (Bab 1-3), UAS (Bab 1-5 penuh)

---

## SETUP & ENVIRONMENT

| Item | Detail |
|:---|:---|
| **Python Env** | `.venv` di `d:\kevin\Documents\ITK\Semester 5\Sains Data\.venv` |
| **Kernel Notebook** | Gunakan venv di atas sebagai kernel VSCode |
| **Library Utama** | `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `imbalanced-learn` |
| **Catatan Path** | Dataset dibaca dengan path relatif `"dataset_GANGGUAN_TIDUR.csv"` - pastikan kernel CWD = folder Sains Data |

### Perintah install jika ada library kurang:
`ash
.venv\Scripts\pip install pandas matplotlib seaborn scikit-learn imbalanced-learn
`

---

## TENTANG DATASET

| Properti | Nilai |
|:---|:---|
| Baris | 100.002 (termasuk header) -> 100.000 observasi |
| Kolom | 32 fitur + 1 target |
| Missing Values | **10.000 baris (10%)** di semua kolom KECUALI `sleep_disorder_risk` |
| Duplikasi | 0 |
| Target | `sleep_disorder_risk` -> 4 kelas: Healthy, Mild, Moderate, Severe |
| Imbalanced? | Ya - Healthy ~54%, Mild ~33%, Moderate ~8%, Severe ~4% |
| Outlier Signifikan | `caffeine_mg_before_bed`, `alcohol_units_before_bed`, `screen_time_before_bed_mins` |

### Kategori Fitur:
- **Demografi**: `age`, `gender`, `occupation`, `country`
- **Biometrik**: `bmi`, `heart_rate_resting_bpm`
- **Pola Tidur**: `sleep_duration_hrs`, `sleep_quality_score`, `rem_percentage`, `deep_sleep_percentage`, `sleep_latency_mins`, `wake_episodes_per_night`, `nap_duration_mins`, `weekend_sleep_diff_hrs`, `felt_rested`
- **Gaya Hidup**: `caffeine_mg_before_bed`, `alcohol_units_before_bed`, `screen_time_before_bed_mins`, `exercise_day`, `steps_that_day`
- **Psikologis**: `stress_score`, `mental_health_condition`
- **Pekerjaan/Aktivitas**: `work_hours_that_day`, `shift_work`
- **Sirkadian/Lingkungan**: `chronotype`, `room_temperature_celsius`, `season`, `day_type`
- **Kognitif**: `cognitive_performance_score`
- **Medis**: `sleep_aid_used`
- **Identifier (drop saat Data Prep)**: `person_id`

---

## STRUKTUR NOTEBOOK SAAT INI (21 Cells)

| Cell | Tipe | Isi | Status |
|:---|:---:|:---|:---:|
| [0] | Markdown | **Bab 1 - Business Understanding** (Latbel, Rumusan, Tujuan, Kriteria Sukses) | SELESAI |
| [1] | Markdown | **Bab 2 - Data Understanding**: Gambaran dataset + Kamus Data 32 fitur | SELESAI |
| [2] | Code | Import + pd.set_option + read_csv + sample(20) + info() + describe(include='all').T | SELESAI |
| [3] | Code | Heatmap Korelasi (sns.heatmap) | SELESAI |
| [4] | Markdown | Header "Analisis Tambahan CRISP-DM" | ADA |
| [5] | Code | Missing Value Analysis + Deteksi Duplikasi | SELESAI |
| [6] | Code | Bar Chart distribusi target sleep_disorder_risk | SELESAI |
| [7] | Markdown | Header Pie Chart (Slide 10) | ADA |
| [8] | Code | Pie Chart (Proporsi target & gender) | SELESAI |
| [9] | Code | Histogram: Age & Sleep Duration | SELESAI |
| [10] | Markdown | Header Distribusi Fitur Tambahan (Stres, Kualitas, BMI, Gender) | ADA |
| [11] | Code | Histogram 2x2: Sleep Quality, Stress, BMI, Gender Bar | SELESAI |
| [12] | Markdown | Header Distribusi Gaya Hidup & Pekerjaan | ADA |
| [13] | Code | Histogram 2x2: Kafein, Alkohol, Screen Time, Pekerjaan | SELESAI |
| [14] | Markdown | Header Scatter Plot (Slide 12) | ADA |
| [15] | Code | Scatter Plot: Stres vs Durasi Tidur & Screen Time vs Sleep Latency | SELESAI |
| [16] | Markdown | Header Skewness Analysis (Slide 16) | ADA |
| [17] | Code | Tabel Skewness (Mean, Median, Mode, Bentuk Distribusi) per 13 fitur | SELESAI |
| [18] | Markdown | Header Outlier IQR & Z-Score (Slide 13, 20, 21) | ADA |
| [19] | Code | Tabel Outlier (IQR + Z-Score) + Box Plot Univariate 4 fitur | SELESAI |
| [20] | Markdown | Rangkuman Insight Awal untuk Data Preparation (Slide 22) | SELESAI |

---

## RUBRIK PENILAIAN UTS (s/d Bab 3 - Data Preparation)

### Bab 1 - Business Understanding
| Kriteria | Skor Target | Status |
|:---|:---:|:---:|
| Latar Belakang Masalah (konteks domain & dampak) | 5 | SELESAI |
| Rumusan Masalah (spesifik & terukur) | 5 | SELESAI |
| Tujuan Analisis | 5 | SELESAI |
| Kriteria Kesuksesan (ambang batas metrik >= 85%) | 5 | SELESAI |

### Bab 2 - Data Understanding
| Kriteria | Skor Target | Status |
|:---|:---:|:---:|
| >= 20 Sampel Data ditampilkan | 5 | SELESAI |
| Atribut + Tipe Data dijelaskan (Kamus Data 32 fitur) | 5 | SELESAI |
| Statistik Deskriptif (describe) | 5 | SELESAI |
| Visualisasi Distribusi (Histogram) + Skewness | 5 | SELESAI |
| Korelasi Antar Fitur (Heatmap) | 5 | SELESAI |
| Validasi: Missing Value, Duplikasi, Outlier | 5 | SELESAI |
| Pie Chart + Bar Chart + Scatter Plot | 5 | SELESAI |
| **Bivariate Boxplot (fitur vs. kelas target)** | 5 | PERLU CEK ULANG |
| Narasi/interpretasi di bawah grafik kunci | 5 | BELUM ADA |
| Rangkuman Insight Awal | 5 | SELESAI |

### Bab 3 - Data Preparation (BELUM DIKERJAKAN)
| Tahapan | Detail | Status |
|:---|:---|:---:|
| Penentuan Objek | Drop `person_id` (identifier, tidak prediktif) | BELUM |
| Handling Missing Values | Imputasi Median (fitur numerik skewed) + Modus (fitur kategorik) | BELUM |
| Handling Duplikasi | Verifikasi dan drop jika ada | BELUM |
| Handling Outliers | IQR Capping / Winsorization | BELUM |
| Encoding Target | Healthy->0, Mild->1, Moderate->2, Severe->3 (Ordinal Encoding) | BELUM |
| Encoding Fitur Kategorik | One-Hot Encoding: gender, occupation, country, chronotype, mental_health_condition, season, day_type | BELUM |
| Feature Scaling | StandardScaler atau RobustScaler untuk semua fitur numerik | BELUM |
| Feature Selection | Berdasarkan korelasi Pearson / Mutual Information | BELUM |
| Handling Imbalanced Data | SMOTE atau RandomOverSampler (imbalanced-learn) | BELUM |
| Dimensionality Reduction (PCA) | Wajib sesuai instruksi dosen Hal. 5 | BELUM |

---

## KEPUTUSAN & KONVENSI TEKNIS

| Keputusan | Alasan |
|:---|:---|
| df.describe(include='all').T | Agar seluruh 32 fitur (numerik + kategorik) tampil rapi tanpa terpotong |
| pd.set_option('display.max_columns', None) | Mencegah kolom terpotong dengan tanda ... di output |
| Scatter plot hanya 2 pasangan | Fokus pada pasangan paling relevan secara domain; kuantitas bukan kriteria skor |
| Distribusi tidak untuk semua 32 fitur | Cukup representatif per kategori fitur; fitur binary & identifier tidak perlu divisualisasikan |
| Sampel scatter plot = 3.000 baris (random_state=42) | Optimasi performa render pada dataset 100.000 baris agar tidak padat |
| df.info(verbose=True, show_counts=True) | Menampilkan seluruh 32 kolom secara eksplisit |
| Skewness threshold > 0.5 atau < -0.5 | Sesuai konvensi statistik standar (George & Mallery, 2010) |
| IQR Outlier threshold: 1.5 x IQR | Sesuai rumus baku Tukey (Slide 21 dosen) |
| Z-Score threshold: |Z| > 3 | Sesuai aturan 3-sigma (Slide 21 dosen) |

---

## CATATAN BUSINESS UNDERSTANDING (Dari Tulisan Tangan Anda)

- **Latbel**: Banyak mahasiswa jam tidur kurang -> kesehatan menurun, konsentrasi/intelektual turun
- **Rumusan**: Bagaimana mengetahui tingkat gangguan tidur mahasiswa & cara klasifikasi berdasarkan data
- **Tujuan**: Membuat sistem klasifikasi gangguan tidur & pipeline data preparation
- **Kriteria**: Saat evaluasi matriks mencapai 85% semua

---

## RENCANA TAHAP SELANJUTNYA

### Prioritas Segera (UTS)
1. Tambahkan narasi interpretasi di bawah grafik Heatmap, Scatter Plot, dan Boxplot Outlier
2. Pastikan Bivariate Boxplot (fitur kunci per kelas target) ada di notebook
3. **Kerjakan Bab 3 - Data Preparation** (seluruh pipeline dari atas)

### Setelah UTS (UAS)
4. **Bab 4 - Modeling**: Train/test split -> Pilih algoritma (Random Forest, XGBoost, SVM) -> Training -> Cross-validation
5. **Bab 5 - Evaluasi & Deployment**: Confusion Matrix, Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## BUG & FIX YANG SUDAH DISELESAIKAN

| Masalah | Penyebab | Solusi |
|:---|:---|:---|
| Heatmap error fmt=".2f" | Parameter tidak valid saat annot=False | Hapus fmt=".2f" |
| Heatmap error .corr() | Pandas baru butuh numeric_only=True | Ganti ke kolom_numerik.corr(numeric_only=True) |
| df.describe() hanya tampil fitur numerik | Default hanya numerik | Ganti ke describe(include='all').T |
| Kolom terpotong ... di output | Batas default pandas 20 kolom | Tambah pd.set_option('display.max_columns', None) |
| UnicodeEncodeError karakter aproks di tabel skewness | Windows CP-1252 tidak support unicode tertentu | Ganti karakter ke versi ASCII |
