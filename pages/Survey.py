# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Chess Habits Survey 📝")
st.write("Tell us a little about your chess habits.")

# DATA INPUT FORM
# Collect all three answers before submitting.
with st.form("survey_form"):
    favorite_opening = st.text_input("What is your favorite chess opening?")

    time_control = st.selectbox(
        "What is your favorite time control?",
        ["Bullet", "Blitz", "Rapid", "Classical"]
    )

    games_per_week = st.number_input(
        "About how many chess games do you play per week?",
        min_value=0,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Submit Data")

# Append one row when the form is submitted.
if submitted:
    with open("data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([favorite_opening, time_control, games_per_week])

    st.success("Your response has been saved!")

# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Survey Responses")

current_data = pd.read_csv("data.csv")
st.dataframe(current_data, hide_index=True)