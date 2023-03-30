import requests
import streamlit as st

# NASA APOD API URL
APOD_URL = "https://api.nasa.gov/planetary/apod"

# API key
API_KEY = "6x1BFJezktd34g2615qORdf3FfOpIo0g3NcTX2tZ"

# Display the APOD
st.title("NASA Astronomy Picture of the Day")

with st.spinner("Loading APOD..."):
    response = requests.get(f"{APOD_URL}?api_key={API_KEY}")
    data = response.json()

    # Display the APOD image
    st.image(data["url"], use_column_width=True)

    # Display the APOD information
    st.write(f"Date: {data['date']}")
    st.write(f"Title: {data['title']}")
    st.write(f"Details: {data['explanation']}")
