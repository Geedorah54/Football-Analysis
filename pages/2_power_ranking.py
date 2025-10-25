import pandas as pd # data modeling/transformation
import matplotlib.pyplot as plt # for plotting
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

df2 = pd.read_csv('this_season.csv')

# Load your game scores
games = pd.read_csv("2025_games.csv")

# Stack home and away data into one long table
home = games[["week", "home_team", "home_score"]].rename(
    columns={"home_team": "team", "home_score": "points"}
)
away = games[["week", "away_team", "away_score"]].rename(
    columns={"away_team": "team", "away_score": "points"}
)

# Combine both into one table
team_points = pd.concat([home, away], ignore_index=True)
print(team_points.head(15))

team_scoring = (
    team_points.groupby("team")
    .agg(points_per_game=("points", "mean"), total_points=("points", "sum"))
    .reset_index()
)


summary = df2.groupby("team").agg({
    "epa": "mean",
    "yards_gained": "sum",
    "touchdown": "sum",
}).reset_index()

# Merge the scoring data
summary = summary.merge(team_scoring, on="team", how="left")

logos = pd.read_csv('logos.csv')


summary = summary.merge(logos, on='team', how='left')

summary["logo"] = summary["logo"].fillna("https://upload.wikimedia.org/wikipedia/commons/e/e0/Question_mark_black.png")



afc = {"BAL","BUF","CIN","CLE","DEN","HOU","IND","JAX","KC","LAC","LV","MIA","NE","NYJ","PIT","TEN"}
summary["conference"] = summary["team"].apply(lambda t: "AFC" if t in afc else "NFC")

fig = px.scatter(
    summary,
    x="epa",
    y="points_per_game",
    size="yards_gained",
    color="conference",
    hover_name="team",
    hover_data={"touchdown": True, "yards_gained": True, "points_per_game": ":.1f"},
    color_discrete_map={"AFC": "#00FFFF", "NFC": "#FF00FF"},
    template="plotly_dark",
)
fig.update_traces(marker=dict(opacity=0.85, line=dict(width=1, color="#FFFFFF")))
fig.update_layout(
    paper_bgcolor="#0A0A0F",
    plot_bgcolor="#0A0A0F",
    font=dict(color="#FFFFFF", family="Orbitron"),
    title="EPA Efficiency vs. Points Scored per Game",
    xaxis_title="Average EPA per Play (Efficiency)",
    yaxis_title="Points per Game (Power)",
)
st.plotly_chart(fig, use_container_width=True)