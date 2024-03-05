import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat sebuah fungsi untuk melakukan pemuatan data
def load_data(file_path):
    return pd.read_csv(file_path)

# Proses pemuatan data
daysbd_df = load_data("day.csv")

# Mengubah kolom datetime menjadi tipe datetime
daysbd_df['datetime'] = pd.to_datetime(daysbd_df['dteday'])

# Menyesuaikan nama kolom dan memetakan nilai-nilai tertentu
daysbd_df.rename(columns={'yr': 'year', 'mnth': 'month', 'weathersit': 'condition_weather', 'cnt': 'count'}, inplace=True)
daysbd_df['month'] = daysbd_df['month'].map({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'Augustus', 9: 'September', 10: 'October', 11: 'November', 12: 'December'})
daysbd_df['season'] = daysbd_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
daysbd_df['weekday'] = daysbd_df['weekday'].map({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})
daysbd_df['condition_weather'] = daysbd_df['condition_weather'].map({1: 'C and the other', 2: 'M+C and the other', 3: 'LS and the other', 4: 'HR and the other'})
daysbd_df['workingday'] = daysbd_df['workingday'].map({1: 'Weekdays', 0: 'Weekend'})

# Menampilkan judul aplikasi
st.title('Bike Sharing Data Analysis')
st.subheader("by Virandy Bagaskara Syahwanto")
st.text(
    "Analisis Data dengan Python : Bike Sharing Dataset"
)
st.subheader("Berikut merupakan data mentah dari Bike Sharing Dataset")
st.write(daysbd_df)

# Visualisasi data
st.subheader('Data Visualization')
st.text("Berikut merupakan visualisasi data dari hasil analisis data")

# Menampilkan perbandingan pengguna di Weekdays dan Weekend
with st.expander("Perbandingan Pengguna di Weekdays dan Weekend"):
    fig, ax = plt.subplots(figsize=(6,5))
    sns.barplot(x='workingday', y='count', palette=['red', 'blue'], data=daysbd_df)
    plt.title('Perbandingan Pengguna di Weekdays dan Weekend')
    plt.xlabel('Jenis Hari')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    col1.metric(label="Weekend", value="4330")
    col2.metric(label="Weekdays", value="4584")


# Menampilkan rata-rata peminjaman sepeda berdasarkan kondisi cuaca
with st.expander("Rata-rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca"):
    fig, ax = plt.subplots(figsize=(6,5))
    sns.barplot(x='condition_weather', y='count', palette=['yellow', 'blue', 'red'], data=daysbd_df)
    plt.title('Rata-rata Peminjaman Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Peminjaman Sepeda')
    st.pyplot(fig)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="M+C and the other", value="4035")
    col2.metric(label="C and the other", value="4876")
    col3.metric(label="LS and the other", value="1803")

st.caption("Copyright (c) Virandy Bagaskara Syahwanto")