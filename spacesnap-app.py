import requests
import pandas as pd
import streamlit as st

# NASA APOD API URL
APOD_URL = "https://api.nasa.gov/planetary/apod"

# API key
API_KEY = "6x1BFJezktd34g2615qORdf3FfOpIo0g3NcTX2tZ"

# Display the APOD and its information
st.set_page_config(page_title="SpaceSnap: NASA Astronomy Picture of the Day")

st.title("SpaceSnap: NASA Astronomy Picture of the Day 🔭")

# Fetch APOD data
def fetch_apod_data():
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}")
    data = response.json()
    return data

def fetch_apod_data_date(date):
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}&date={date}")
    data = response.json()
    return data

def display_apod(data):
    st.title(data['title'])
    st.image(data["url"], use_column_width=True)
    st.write(f"**Title:** {data['title']}")
    st.write(f"**Date:** {data['date']}")
    st.write(f"**Explanation:** \n\n{data['explanation']}")

# Get APOD
apod_data = fetch_apod_data()
display_apod(apod_data)

today = pd.Timestamp.today().strftime("%Y-%m-%d")

# Allow users to browse previous APODs
st.sidebar.title("Browse APODs")
selected_date = st.sidebar.date_input("Select date", pd.Timestamp.today())
selected_date_str = selected_date.strftime("%Y-%m-%d")
if selected_date_str != today:
    apod_data = fetch_apod_data_date(selected_date_str)
    display_apod(apod_data)

# Random APOD generator
st.sidebar.title("Random APOD")
if st.sidebar.button("Show random APOD"):
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}")
    data = response.json()
    display_apod(data)
