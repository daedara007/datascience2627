# 💤 Klasifikasi Risiko Gangguan Tidur Berdasarkan Pola Hidup dan Biometrik

---

## 📌 Ringkasan Proyek

Proyek ini bertujuan untuk membangun sistem klasifikasi tingkat risiko gangguan tidur (*sleep disorder risk*) berbasis *Machine Learning* menggunakan data multivariat gaya hidup, biometrik, lingkungan, dan performa kognitif.

Dataset terdiri dari **100.000 observasi** dengan **31 fitur prediktor** dan **1 label target 4 kelas**:
* 🟢 **Healthy**: Individu dengan kualitas tidur optimal tanpa indikasi patologis.
* 🟡 **Mild**: Gejala gangguan tidur ringan.
* 🟠 **Moderate**: Gangguan tidur tingkat sedang yang mulai mempengaruhi performa harian.
* 🔴 **Severe**: Gangguan tidur parah/kritis yang memerlukan atensi medis segera.

---

## 📂 Struktur Repositori

Repositori ini disusun secara modular berdasarkan tahapan siklus **CRISP-DM** untuk memudahkan kolaborasi tim dan proses *Pull Request* (PR) ke branch `main`:

```text
Sains Data/
├── .gitignore                      # Mengabaikan virtual environment (.venv) & cache
├── README.md                       # Dokumentasi utama proyek & panduan alur kerja
├── dataset_GANGGUAN_TIDUR.csv      # Dataset mentah tugas (100.000 baris x 32 kolom, ~10% missing value)
│
├── 01_Data_Understanding/          # [BAB 2] Eksplorasi & Pemahaman Data
│   ├── Sains_data.ipynb            # Notebook analisis eksploratif komprehensif (Bab 1 & Bab 2)
│   ├── data-sains.ipynb            # Notebook analisis eksplorasi kolaborasi tim
│   └── dataset_GANGGUAN_TIDUR.csv  # Salinan dataset lokal modul
│
├── 02_Data_Preparation/            # [BAB 3] Penyiapan & Rekayasa Data (WIP di branch fitur)
│   └── README.md                   # Panduan & status pengerjaan data preparation
│
└── 03_Modeling/                    # [BAB 4] Pemodelan & Evaluasi (Tahap Selanjutnya)
    └── README.md                   # Panduan eksperimen model klasifikasi tim
```

---

## 🧩 Kamus Data Singkat (32 Atribut)

| Kategori | Fitur / Kolom | Tipe | Deskripsi |
|:---|:---|:---:|:---|
| **Identifier** | `person_id` | Int | ID unik responden (dipertahankan untuk tahap *Feature Selection*) |
| **Demografi** | `age`, `gender`, `occupation`, `country` | Num/Cat | Usia, jenis kelamin, profesi, dan negara asal |
| **Biometrik** | `bmi`, `heart_rate_resting_bpm` | Float/Int | Indeks massa tubuh dan detak jantung istirahat |
| **Pola Tidur** | `sleep_duration_hrs`, `sleep_quality_score`, `rem_percentage`, `deep_sleep_percentage`, `sleep_latency_mins`, `wake_episodes_per_night`, `nap_duration_mins`, `weekend_sleep_diff_hrs`, `felt_rested` | Campuran | Metrik durasi, kualitas tidur, fase REM/Deep sleep, latensi, dan kesegaran bangun |
| **Gaya Hidup** | `caffeine_mg_before_bed`, `alcohol_units_before_bed`, `screen_time_before_bed_mins`, `exercise_day`, `steps_that_day` | Campuran | Konsumsi kafein/alkohol, paparan layar (*screen time*), rutinitas olahraga, dan jumlah langkah |
| **Psikologis & Beban Kerja** | `stress_score`, `mental_health_condition`, `work_hours_that_day`, `shift_work` | Campuran | Tingkat stres (1-10), kondisi mental, jam kerja harian, dan sistem kerja giliran |
| **Sirkadian & Lingkungan** | `chronotype`, `room_temperature_celsius`, `season`, `day_type` | Campuran | Kronotipe (*Morning/Neutral/Evening*), suhu kamar, musim, dan jenis hari (*Weekday/Weekend*) |
| **Kognitif & Medis** | `cognitive_performance_score`, `sleep_aid_used` | Float/Int | Skor performa kognitif (0-100) dan penggunaan obat tidur |
| **Target Variabel** | `sleep_disorder_risk` | String | Label klasifikasi risiko (*Healthy*, *Mild*, *Moderate*, *Severe*) |

---


## 🚀 Panduan Memulai (*Getting Started*)

### 1. Prasyarat Sistem
* Python 3.10+ (Direkomendasikan Python 3.12)
* Git

### 2. Instalasi Dependensi
Aktifkan virtual environment dan pasang pustaka yang diperlukan:
```bash
# Mengaktifkan virtual environment (Windows)
.venv\Scripts\activate

# Instalasi paket utama
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
```

### 3. Menjalankan Notebook
Jalankan Jupyter Notebook atau buka di IDE (VS Code / Antigravity):
1. **Buka modul eksplorasi**:  
   `01_Data_Understanding/Sains_data.ipynb` untuk melihat statistik deskriptif dan visualisasi EDA.
2. **Buka modul persiapan data**:  
   `02_Data_Preparation/data_preparation.ipynb` untuk meninjau atau mereproduksi imputasi data dan penyeimbangan kelas.

---

## 🌿 Alur Kerja Kolaborasi Git (*Git Workflow*)

Untuk menjaga branch `main` tetap bersih dan siap untuk pengumpulan final/penilaian:

1. **Buat Branch Khusus untuk Pekerjaan Anda**:
   ```bash
   git checkout -b feature/<nama-fitur-atau-nama-anggota>
   # Contoh: git checkout -b feature/modeling-kevin
   ```
2. **Kerjakan Perubahan & Buat Commit**:
   ```bash
   git add .
   git commit -m "feat: tambahkan baseline model Random Forest pada folder 03_Modeling"
   ```
3. **Push Branch ke Remote GitHub**:
   ```bash
   git push origin feature/<nama-fitur-atau-nama-anggota>
   ```
4. **Buat Pull Request (PR)**:
   * Buka repositori GitHub.
   * Buat PR dari branch fitur Anda menuju branch `main`.
   * Lakukan *code review* bersama anggota kelompok sebelum melakukan *merge*.

---