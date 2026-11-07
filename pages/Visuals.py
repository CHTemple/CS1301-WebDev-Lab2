# This creates the page for displaying data visualizations.

import streamlit as st

import json
import matplotlib.pyplot as plt

import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Chess by the Numbers")


# PART 1: GRAPHS FROM data.json
data_path = "data.json"

with open(data_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# ---------- STATIC PIE CHART ----------

st.header("10 Most Popular First Moves")

moves = list(data["opening_moves"].keys())
counts = list(data["opening_moves"].values())

figure_1, ax = plt.subplots()

ax.pie(
    counts,
    labels=moves,
    autopct="%1.0f%%",  # Display percentages as a whole number (like our data)
    startangle=90,
    pctdistance=0.85,
    textprops={"fontsize": 8}  # Make the percentage labels smaller so they fit (better, at least)
)

ax.set_title("White's First Moves")

st.pyplot(figure_1)
plt.close(figure_1)

st.caption(
    "Source: [Chess.com Opening Explorer](https://www.chess.com/analysis/explorer). "
    "Accessed October 23, 2026."
)


# ---------- DYNAMIC LINE CHART ----------

st.header("Lichess.org Games Played Over Time")

# JSON dictionary keys are strings, so convert years to integers.
years = []

for year in data["games"]:
    years.append(int(year))

years.sort()

if "year_range" not in st.session_state:
    st.session_state["year_range"] = (years[0], years[-1])

st.slider(
    "Select a year range",
    min_value=years[0],
    max_value=years[-1],
    key="year_range"
)

start_year, end_year = st.session_state["year_range"]

selected_years = []
selected_games = []

for year in years:
    if start_year <= year <= end_year:
        selected_years.append(year)
        selected_games.append(data["games"][str(year)])

figure_2, ax = plt.subplots()

ax.plot(selected_years, selected_games, marker="o")

ax.set(
    title="Lichess Games Played in January by Year",
    xlabel="Year",
    ylabel="Games",
    xticks=selected_years
)

ax.tick_params(axis="x", labelsize=8)
ax.ticklabel_format(style="plain", axis="y")
ax.grid(True, alpha=0.3)

st.pyplot(figure_2)
plt.close(figure_2)

st.caption(
    "Each point shows games played during January of that year, "
    "not the annual total or number of unique players."
)

st.caption(
    "Source: [Lichess Open Database](https://database.lichess.org/). "
    "Accessed October 23, 2026."
)



# PART 2: GRAPHS FROM data.csv

st.divider()
st.header("Chess Survey Results")

survey_data = pd.read_csv("data.csv")

# ---------- STATIC BAR CHART ----------

st.subheader("Favorite Time Controls")

time_controls = ["Bullet", "Blitz", "Rapid", "Classical"]
counts = []

for control in time_controls:
    matching_rows = survey_data["time_control"] == control
    matching_responses = survey_data[matching_rows]
    count = len(matching_responses)
    counts.append(count)

figure_3, ax = plt.subplots()

ax.bar(time_controls, counts)

ax.set(
    title="Favorite Time Controls",
    xlabel="Time Control",
    ylabel="Number of Respondents"
)

# Respondent counts should be displayed as whole numbers.
ax.set_yticks(range(max(counts) + 1))

st.pyplot(figure_3)
plt.close(figure_3)


# ---------- DYNAMIC HISTOGRAM ----------

st.subheader("Games Played per Week")

if "survey_time_control" not in st.session_state:
    st.session_state["survey_time_control"] = "All"

st.selectbox(
    "Filter by favorite time control:",
    ["All"] + time_controls,
    key="survey_time_control"
)

selected_control = st.session_state["survey_time_control"]

if selected_control == "All":
    filtered_data = survey_data
else:
    filtered_data = survey_data[
        survey_data["time_control"] == selected_control
    ]

if filtered_data.empty:
    st.info("No responses for this selection yet.")
else:
    figure_4, ax = plt.subplots()

    ax.hist(
        filtered_data["games_per_week"],
        bins=5,
        edgecolor="black"
    )

    ax.set(
        title=f"Weekly Games: {selected_control}",
        xlabel="Games Played per Week",
        ylabel="Number of Respondents"
    )

    ax.set_yticks(range(len(filtered_data) + 1))

    st.pyplot(figure_4)
    plt.close(figure_4)

