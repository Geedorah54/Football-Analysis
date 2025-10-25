import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Team Analytics", layout="wide")

st.title("🏈 Team Analytics")

st.write("""
Use the dropdown below to explore advanced stats for each team —
EPA trends, touchdowns, yards, and more.
""")

# --- Load Data ---
try:
    df = pd.read_csv("season_team_stats.csv")  # Replace with your team-level stats CSV
except FileNotFoundError:
    st.error("⚠️ season_team_stats.csv not found. Please add it to the project folder.")
    st.stop()

# --- Team Selection ---
teams = sorted(df['team'].unique())
selected_team = st.selectbox("Select a Team", teams)

# --- Filter for Selected Team ---
team_df = df[df['team'] == selected_team]

# --- Plot EPA Trend ---
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=team_df['week'],
    y=team_df['epa'],
    mode='lines+markers',
    line=dict(color='#00FFFF', width=3),
    marker=dict(size=8, color='#00FFFF'),
    fill='tozeroy',
    fillcolor='rgba(0,255,255,0.1)',
))
fig.update_layout(
    title=f"{selected_team} — Expected Points Added (EPA) Trend",
    paper_bgcolor='#0A0A0F',
    plot_bgcolor='#0A0A0F',
    font=dict(color='#FFFFFF', family='Orbitron'),
)
st.plotly_chart(fig, use_container_width=True)

# --- Display Summary Stats ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Touchdowns", int(team_df['touchdowns'].sum()))
col2.metric("Total Yards", int(team_df['yards'].sum()))
col3.metric("Avg. EPA per Game", round(team_df['epa'].mean(), 2))
