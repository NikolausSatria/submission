import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


sns.set(style='dark')

def create_season_data(df):
    season_data = df.groupby('season_day')['cnt_day'].mean().reset_index()
    return season_data

def create_wather_data(df):
    weather_data = df.groupby('weathersit_day')['cnt_day'].mean().reset_index()
    return weather_data




# Load all_data.csv
all_df = pd.read_csv("https://raw.githubusercontent.com/NikolausSatria/submission/main/dashboard/all_data.csv")



season_data_df = create_season_data(all_df)
weather_data_df = create_wather_data(all_df)


## Melengkapi Dashboard dengan berbagai visualisasi data
st.header(':sparkles: Bike Sharing Report Dashboard :sparkles:') 
 
# colors = ["#7dc0a7", "#ed936b", "#b0d767", "#e0c59a"]

# tampilkan pada dashboard terkait demografi pelanggan

st.subheader("Rent Based on Season")
fig, ax = plt.subplots(figsize=(50, 40))
 
sns.barplot(
        y="cnt_day", 
        x="season_day",
        data=season_data_df,
        palette='Set2',
        ax=ax
    )
ax.set_title("Rata-Rata Penyewaan Harian", loc="center", fontsize=100)
ax.set_ylabel("Rata-Rata Penyewa",loc="center", fontsize=100)
ax.set_xlabel("Season", loc="center", fontsize=100)
ax.tick_params(axis='x', labelsize=75)
ax.tick_params(axis='y', labelsize=75)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Musim memiliki hubungan yang kuat dengan rata-rata penyewaan sepeda harian. Jumlah rata-rata penyewa sepeda paling banyak menyewa pada musim fall dan penyewa paling sedikit terjadi pada musim spring
        """
    )

st.subheader("Rent Based on Weather")
fig, ax = plt.subplots(figsize=(50, 40))
 
sns.barplot(
        x="weathersit_day",
        y="cnt_day", 
        data=weather_data_df,
        palette='Set2',
        ax=ax
    )
ax.set_title("Rata-Rata Penyewaan Harian", loc="center", fontsize=100)
ax.set_ylabel("Rata-Rata Penyewa",loc="center", fontsize=100)
ax.set_xlabel("Weather", loc="center", fontsize=100)
ax.tick_params(axis='x', labelsize=75)
ax.tick_params(axis='y', labelsize=75)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """ Cuaca mempengaruhi jumlah rata-rate penyewa sepeda harian. Pada saat cuaca clear, tingkat penyewa sepeda merupakan yang terbanyak. Kemudian dilanjutkan dengan cuaca mist yang memiliki tingkat penyewaan sepeda terbanyak kedua. Cuaca rain memiliki tingkat penyewaan sepeda paling sedikit.
        """
    )
