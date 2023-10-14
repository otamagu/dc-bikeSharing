import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')


# Menyiapkan data
day_bs = pd.read_csv("day.csv")
hour_bs = pd.read_csv("hour.csv")

# Merubah angka menjadi keterangan
day_bs['mnth'] = day_bs['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_bs['season'] = day_bs['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_bs['weekday'] = day_bs['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_bs['weathersit'] = day_bs['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Menyiapkan DataFrame

# Jumlah perjalanan bike sharing setiap hari
def create_daily_trip(df):
    daily_trips = day_bs.groupby("dteday")["cnt"].sum()
    return create_daily_trip

# Jumlah perjalanan bike sharing untuk setiap hari dalam seminggu
def create_weekday_trip(df):
    weekday_trips = day_bs.groupby("weekday")["cnt"].sum()
    weekday_trips.sort_values(ascending=False)
    return create_weekday_trip

# Jumlah perjalanan bike sharing untuk setiap jam dalam sehari
def create_hour_trips(df):
    hour_trips = hour_bs.groupby("hr")["cnt"].sum()
    hour_trips.sort_values(ascending=False, inplace=True)
    return create_hour_trips

# Jumlah perjalanan bike sharing untuk setiap kondisi cuaca
def create_weather_trips(df):
    weathersit_trips = day_bs.groupby("weathersit")["cnt"].sum()
    weathersit_trips.sort_values(ascending=False, inplace=True)
    return create_weather_trips

# Membuat komponen filter
min_date = pd.to_datetime(day_bs['dteday']).dt.date.min()
max_date = pd.to_datetime(day_bs['dteday']).dt.date.max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://vibrantoutlook.files.wordpress.com/2021/09/17311121653_63d5d8bee2_o.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_bs[(day_bs['dteday'] >= str(start_date)) & 
                (day_bs['dteday'] <= str(end_date))]

# Membuat Dashboard
# Membuat Judul
st.header('Bike Sharing Dashboard:sparkles:')

# Membuat Daily Trip
st.subheader('Daily Trips')
plt.figure(figsize=(10, 5))

daily_trip_df = day_bs.groupby("dteday")["cnt"].mean()
daily_trip_df.plot(marker='o', linestyle='-', color='blue')

plt.xlabel("Tanggal")
plt.ylabel("Rata-rata Perjalanan")
plt.xticks(rotation=45)

st.pyplot(plt)

# Membuat Weekday Trip
st.subheader('Weekday Trips')
plt.figure(figsize=(10, 5))

weekday_trip_df = day_bs.groupby("weekday")["cnt"].sum()

plt.bar(weekday_trip_df.index, weekday_trip_df.values)
plt.xlabel("Hari")
plt.ylabel("Jumlah Perjalanan")
st.pyplot(plt)

# Membuat Hour Trip
st.subheader('Hour Trips')
plt.figure(figsize=(10, 5))

hour_trip_df = hour_bs.groupby("hr")["cnt"].sum()

plt.bar(hour_trip_df.index, hour_trip_df.values)
plt.xlabel("Jam")
plt.ylabel("Jumlah Perjalanan")
st.pyplot(plt)

# Membuat Weather Trip
st.subheader('Weather Trips')
plt.figure(figsize=(10, 5))

weathersit_trip_df = day_bs.groupby("weathersit")["cnt"].sum()

plt.bar(weathersit_trip_df.index, weathersit_trip_df.values)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Perjalanan")
st.pyplot(plt)