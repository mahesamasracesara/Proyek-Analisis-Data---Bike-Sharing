# Bike Sharing Dashboard 🚲

Dashboard ini dibuat menggunakan **Streamlit** untuk menampilkan hasil analisis data pada **Bike Sharing Dataset**.  
Dashboard bertujuan menyajikan insight utama terkait pola penyewaan sepeda secara interaktif dan mudah dipahami.

---

## 📌 Insight Utama

1. Perbandingan rata-rata jumlah penyewaan sepeda berdasarkan **musim**.
2. Perbedaan pola penyewaan sepeda antara **hari kerja dan hari libur**.
3. Distribusi tingkat permintaan penyewaan sepeda (**Low Demand, Medium Demand, High Demand**) berdasarkan analisis lanjutan.

---

## 📂 Struktur Direktori
```text
submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── data/
│   ├── day.csv
│   └── hour.csv
│
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

---

## 🚀 Cara Menjalankan Dashboard

### 1. Clone Repository
```bash
git clone <repository-url>
cd submission
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Dashboard
```bash
streamlit run dashboard/dashboard.py
```

### 4. Akses Dashboard
Dashboard akan terbuka otomatis di browser pada `http://localhost:8501`

---

## 📊 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset** yang berisi informasi penyewaan sepeda dengan berbagai variabel seperti:
- Tanggal dan waktu
- Musim
- Cuaca
- Suhu
- Kelembaban
- Jumlah penyewaan (casual, registered, total)

---

## 🛠️ Teknologi yang Digunakan

- **Python** - Bahasa pemrograman utama
- **Streamlit** - Framework untuk membuat dashboard interaktif
- **Pandas** - Manipulasi dan analisis data
- **Matplotlib/Seaborn** - Visualisasi data
- **Jupyter Notebook** - Eksplorasi dan analisis data

---

## 📝 Catatan

- File `notebook.ipynb` berisi eksplorasi data dan analisis lengkap
- File `url.txt` berisi URL deployment dashboard (jika ada)
- Data mentah tersimpan di folder `data/`
- Dashboard dan data yang sudah diproses ada di folder `dashboard/`

---

## 👤 Author

Proyek ini dibuat sebagai bagian dari submission analisis data bike sharing.

---

## 📄 License

Project ini dibuat untuk keperluan pembelajaran dan analisis data.
