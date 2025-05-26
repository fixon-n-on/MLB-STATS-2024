import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("archivo_completo.csv")

# Title
st.title("MLB Homerun Stats 2024")

# Sidebar filters
teams = st.sidebar.multiselect("Select team(s)", options=df['team'].unique(), default=df['team'].unique())
players = st.sidebar.multiselect("Select player(s)", options=df['player'].unique(), default=df['player'].unique())
positions = st.sidebar.multiselect("Select position(s)", options=df['position'].unique(), default=df['position'].unique())

# Filtered DataFrame
filtered_df = df[
    (df['team'].isin(teams)) &
    (df['player'].isin(players)) &
    (df['position'].isin(positions))
]

# Bar Chart: Average Home Run Trot
st.subheader("Average Home Run Trot by Player")
fig_avg_trot = px.bar(filtered_df, x="player", y="avg_hr_trot", color="team", title="Average HR Trot by Player")
st.plotly_chart(fig_avg_trot)

# Bar Chart: Doubters vs No Doubters
st.subheader("Doubters vs No-Doubters by Player")
fig_doubt_compare = px.bar(
    filtered_df, 
    x="player", 
    y=["doubters", "no_doubters"], 
    barmode="group",
    title="Comparison of Doubters and No-Doubters"
)
st.plotly_chart(fig_doubt_compare)

# Bar Chart: Total Home Runs
st.subheader("Total Home Runs by Player")
fig_total_hr = px.bar(filtered_df, x="player", y="hr_total", color="team", title="Total Home Runs")
st.plotly_chart(fig_total_hr)

# Scatter Plot: Expected HR vs Total HR
st.subheader("Expected vs Actual Home Runs")
fig_hr_comparison = px.scatter(
    filtered_df, 
    x="xhr", 
    y="hr_total", 
    color="team", 
    hover_name="player", 
    title="Expected vs Actual Home Runs"
)
st.plotly_chart(fig_hr_comparison)

# Pie Chart: Player Distribution by Position
st.subheader("Player Distribution by Position")
fig_pie_position = px.pie(
    filtered_df, 
    names="position", 
    title="Distribution of Players by Position"
)
st.plotly_chart(fig_pie_position)
