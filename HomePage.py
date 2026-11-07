# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

st.title("Chess by the Numbers")

st.write("""
This dashboard explores chess openings, online chess activity,
and the chess playing habits of survey respondents.

### Survey
Choose **Survey** in the sidebar to answer a survey on your favorite opening,
favorite time control, and how many games you play per week.

### Visualizations
Choose **Visuals** in the sidebar to explore:
- A pie chart of popular first moves using Chess.com data.
- A line chart of Lichess games played during January of each year.
- A bar chart of survey respondents' favorite time controls.
- A histogram of weekly games played, filtered by favorite time control.
""")


st.image("images/welcome_image.jpg")