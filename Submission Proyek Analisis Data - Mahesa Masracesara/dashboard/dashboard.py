import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("main_data.csv")

df = load_data()

# Mapping season agar tidak membingungkan
season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}
df['season_label'] = df['season'].map(season_map)

# Sidebar
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season_label'].unique(),
    default=df['season_label'].unique()
)

filtered_df = df[df['season_label'].isin(selected_season)]

# Title
st.title("📊 Bike Sharing Dashboard")
st.markdown("Dashboard ini menampilkan ringkasan pola penyewaan sepeda berdasarkan musim, jenis hari, dan tingkat permintaan.")


# Visualisasi 1: Musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")

season_avg = (
    filtered_df
    .groupby('season_label', observed=True)['cnt']
    .mean()
    .reset_index()
)

fig1, ax1 = plt.subplots()
sns.barplot(
    data=season_avg,
    x='season_label',
    y='cnt',
    ax=ax1
)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig1)


# Visualisasi 2: Hari Kerja vs Libur
st.subheader("Pola Penyewaan: Hari Kerja vs Hari Libur")

workingday_avg = (
    filtered_df
    .groupby('workingday', observed=True)['cnt']
    .mean()
    .reset_index()
)

workingday_avg['workingday'] = workingday_avg['workingday'].map({
    0: "Hari Libur",
    1: "Hari Kerja"
})

fig2, ax2 = plt.subplots()
sns.barplot(
    data=workingday_avg,
    x='workingday',
    y='cnt',
    ax=ax2
)
ax2.set_xlabel("Jenis Hari")
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)

# Visualisasi 3: Demand Category
st.subheader("Distribusi Tingkat Permintaan")

demand_count = (
    filtered_df['demand_category']
    .value_counts()
    .reset_index()
)
demand_count.columns = ['Kategori Permintaan', 'Jumlah Hari']

fig3, ax3 = plt.subplots()
sns.barplot(
    data=demand_count,
    x='Kategori Permintaan',
    y='Jumlah Hari',
    ax=ax3
)
st.pyplot(fig3)
