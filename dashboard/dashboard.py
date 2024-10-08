import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Memuat data
data = pd.read_csv('./data/day.csv')

# Fungsi untuk visualisasi pengaruh suhu
def plot_temp_effect():
    plt.figure(figsize=(10, 5))
    plt.scatter(data['temp'], data['cnt'], alpha=0.7, color='orange')
    plt.title("Pengaruh Suhu terhadap Penyewaan Sepeda")
    plt.xlabel("Suhu (Normalized)")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Fungsi untuk visualisasi pengaruh kelembaban
def plot_humidity_effect():
    plt.figure(figsize=(10, 5))
    plt.scatter(data['hum'], data['cnt'], alpha=0.7, color='green')
    plt.title("Pengaruh Kelembaban terhadap Penyewaan Sepeda")
    plt.xlabel("Kelembaban (Normalized)")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Fungsi untuk visualisasi distribusi penyewaan sepeda berdasarkan musim
def plot_season_distribution():
    plt.figure(figsize=(10, 5))
    data.boxplot(column='cnt', by='season', grid=False)
    plt.title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    plt.suptitle("")  # Menghilangkan judul default
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Fungsi untuk visualisasi distribusi penyewaan sepeda
def plot_distribution():
    plt.figure(figsize=(10, 5))
    plt.hist(data['cnt'], bins=30, color='blue', alpha=0.7)
    plt.title("Distribusi Penyewaan Sepeda")
    plt.xlabel("Jumlah Penyewaan")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

# Fungsi untuk visualisasi pengaruh musim
def plot_season_effect():
    plt.figure(figsize=(10, 5))
    data.boxplot(column='cnt', by='season', grid=False)
    plt.title("Pengaruh Musim terhadap Penyewaan Sepeda")
    plt.suptitle("")  # Menghilangkan judul default
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Fungsi untuk visualisasi hubungan cuaca
def plot_weather_relationship():
    plt.figure(figsize=(10, 5))
    data.boxplot(column='cnt', by='weather', grid=False)
    plt.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    plt.suptitle("")  # Menghilangkan judul default
    plt.xlabel("Cuaca")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Fungsi untuk visualisasi pengaruh hari kerja
def plot_workday_effect():
    plt.figure(figsize=(10, 5))
    data.boxplot(column='cnt', by='weekday', grid=False)
    plt.title("Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
    plt.suptitle("")  # Menghilangkan judul default
    plt.xlabel("Hari Kerja")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

# Menambahkan gambar dan nama pada sidebar
image = Image.open("./dashboard/elang.jpg")
st.sidebar.image(image, caption="Erlangga Nursyahbani", use_column_width=True)
 
# Judul dashboard
st.title("Dashboard Penyewaan Sepeda 🚲")

# Membuat tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Distribusi Penyewaan Sepeda", "Pengaruh Musim", "Pengaruh Hari Kerja", "Distribusi Berdasarkan Musim", "Pengaruh Suhu"]
)

# Teks Analisis
teks_analisis_tab1 = """
Gambar ini menunjukkan distribusi penyewaan sepeda secara keseluruhan. Rentang penyewaan paling umum berkisar antara 2000 hingga 6000 penyewaan. Beberapa outlier berada di atas 8000, menunjukkan bahwa dalam kondisi tertentu penyewaan bisa meningkat tajam. Namun, sebagian besar penyewaan sepeda terjadi dalam rentang yang lebih teratur.
"""
teks_analisis_tab2 = """
Boxplot ini memperlihatkan pengaruh musim terhadap jumlah penyewaan sepeda. Musim semi dan panas menunjukkan rata-rata penyewaan yang lebih tinggi dibandingkan musim lainnya, kemungkinan besar karena kondisi cuaca yang lebih mendukung aktivitas di luar ruangan. Sedangkan musim dingin menunjukkan penyewaan yang lebih rendah.
"""
teks_analisis_tab3 = """
Boxplot ini menunjukkan pengaruh cuaca terhadap penyewaan sepeda. Cuaca buruk atau berawan cenderung mengurangi jumlah penyewaan, sementara cuaca cerah menunjukkan penyewaan yang lebih tinggi. Ini memperkuat bahwa faktor cuaca memiliki pengaruh signifikan terhadap keputusan pengguna untuk menyewa sepeda.
"""
teks_analisis_tab3 = """
Boxplot ini memperlihatkan dampak hari kerja terhadap penyewaan sepeda. Pada hari kerja, penyewaan lebih tinggi pada jam-jam sibuk pagi dan sore, sementara akhir pekan menunjukkan pola penyewaan yang lebih terdistribusi sepanjang hari, mengindikasikan penggunaan sepeda untuk rekreasi.
"""
teks_analisis_tab4 = """
Gambar ini menunjukkan distribusi penyewaan sepeda berdasarkan musim. Penyewaan sepeda cenderung lebih tinggi di musim semi dan panas, sedangkan musim dingin menunjukkan penurunan signifikan.
"""
teks_analisis_tab5 = """
Boxplot ini memperlihatkan pengaruh suhu terhadap penyewaan sepeda. Penyewaan cenderung meningkat pada suhu sedang hingga hangat, yang lebih nyaman untuk bersepeda, dan menurun pada suhu ekstrem.
"""

# Tab Distribusi Penyewaan Sepeda
with tab1:
    st.header("Distribusi Penyewaan Sepeda")
    plot_distribution()  # Fungsi untuk menampilkan distribusi penyewaan sepeda
    st.subheader("Analisis Data : ")
    st.markdown(f"<div style='text-align: justify;'>{teks_analisis_tab1}</div>", unsafe_allow_html=True)

# Tab Pengaruh Musim
with tab2:
    st.header("Pengaruh Musim terhadap Penyewaan Sepeda")
    plot_season_effect()  # Fungsi untuk menampilkan boxplot pengaruh musim
    st.subheader("Analisis Data : ")
    st.markdown(f"<div style='text-align: justify;'>{teks_analisis_tab2}</div>", unsafe_allow_html=True)

# Tab Pengaruh Cuaca

# Tab Pengaruh Hari Kerja
with tab3:
    st.header("Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
    plot_workday_effect()  # Fungsi untuk menampilkan boxplot pengaruh hari kerja
    st.subheader("Analisis Data : ")
    st.markdown(f"<div style='text-align: justify;'>{teks_analisis_tab3}</div>", unsafe_allow_html=True)

# Tab Distribusi Berdasarkan Musim
with tab4:
    st.header("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    plot_season_distribution()  # Fungsi untuk menampilkan distribusi penyewaan berdasarkan musim
    st.subheader("Analisis Data : ")
    st.markdown(f"<div style='text-align: justify;'>{teks_analisis_tab4}</div>", unsafe_allow_html=True)

# Tab Pengaruh Suhu
with tab5:
    st.header("Pengaruh Suhu terhadap Penyewaan Sepeda")
    plot_temp_effect()  # Fungsi untuk menampilkan boxplot pengaruh suhu
    st.subheader("Analisis Data : ")
    st.markdown(f"<div style='text-align: justify;'>{teks_analisis_tab5}</div>", unsafe_allow_html=True)
