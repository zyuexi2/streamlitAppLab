import pandas as pd
import streamlit as st

st.title('Boy Band Explorer')

# Use the raw GitHub URL for the CSV file
url = 'https://raw.githubusercontent.com/the-pudding/data/master/boybands/bands.csv'
df = pd.read_csv(url)

# Band Search
band_name = st.text_input('Search for a band', '')

if band_name:
    # Filtered Data
    filtered_data = df[df['band'].str.contains(band_name, case=False, na=False)]

    if not filtered_data.empty:
        band_info = filtered_data.iloc[0]
        # Display Band Details
        st.write(f"**Band Name:** {band_info['band']}")
        st.write(f"**Highest Position on Billboard Hot 100:** {band_info['highest_pos']}")
        st.write(f"**Date Reached Highest Position:** {band_info['highest_pos_date']}")
        st.write(f"**Highest Charting Song:** {band_info['highest_song']}")
        st.write(f"**Dance Speed:** {band_info['danceSpeed']}")
        st.write(f"**Featuring Artist:** {band_info['featuring_artist']}")
        # Provide a clickable link to the YouTube video
        video_link = band_info['highest_song_vid']
        st.markdown(f"[Watch '{band_info['highest_song']}' on YouTube]({video_link})", unsafe_allow_html=True)
    else:
        st.write("No matching band found. Please try another search.")
