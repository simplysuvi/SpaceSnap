import requests
import pandas as pd
import streamlit as st

# NASA APOD API URL
APOD_URL = "https://api.nasa.gov/planetary/apod"

# API key
API_KEY = "6x1BFJezktd34g2615qORdf3FfOpIo0g3NcTX2tZ"

# Streamlit code to display the APOD and its information
st.title("SpaceSnap: NASA Astronomy Picture of the Day")

# User preferences
st.sidebar.title("Preferences")
user_dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Fetch APOD data
def fetch_apod_data(date):
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}&date={date}")
    data = response.json()
    return data

def display_apod(data):
    st.write(data)
    st.image(data["url"], use_column_width=True)
    st.write(f"**Title:** {data['title']}")
    st.write(f"**Date:** {data['date']}")
    st.write(f"**Explanation:** \n\n{data['explanation']}")

# Get today's APOD
today = pd.Timestamp.today().strftime("%Y-%m-%d")
apod_data = fetch_apod_data(today)
display_apod(apod_data)

# Allow users to browse previous APODs
st.sidebar.title("Browse APODs")
selected_date = st.sidebar.date_input("Select date", pd.Timestamp.today())
selected_date_str = selected_date.strftime("%Y-%m-%d")
if selected_date_str != today:
    apod_data = fetch_apod_data(selected_date_str)
    display_apod(apod_data)

# Share on social media
st.sidebar.title("Share on social media")
twitter_url = f"https://twitter.com/intent/tweet?url={apod_data['url']}&text={apod_data['title']}%0A{apod_data['explanation']}"
st.sidebar.write(f"Twitter: [{apod_data['title']}]({twitter_url})")

# Download image
st.sidebar.title("Download image")
file_type = st.sidebar.selectbox("Select file type", ["JPEG", "PNG"])
if st.sidebar.button("Download image"):
    response = requests.get(apod_data["url"])
    with open(f"{apod_data['title']}.{file_type.lower()}", "wb") as f:
        f.write(response.content)
    st.sidebar.write("Image downloaded successfully!")

# Random APOD generator
st.sidebar.title("Random APOD")
if st.sidebar.button("Show random APOD"):
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}")
    data = response.json()
    display_apod(data)

# Set user preferences
if user_dark_mode:
    st.set_theme("dark")
else:
    st.set_theme("default")
