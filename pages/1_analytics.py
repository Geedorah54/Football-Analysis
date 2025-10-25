import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Team Analytics", layout="wide")

st.markdown("""
    <style>
        /* Import Orbitron font */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

        /* ===== GLOBAL STYLING ===== */
        html, body, [class^="st-"], [class^="css-"] {
            font-family: 'Orbitron', sans-serif !important;
            color: #FFFFFF !important;
            background-color: linear-gradient(145deg, #0A0A0F 0%, #141421 50%, #1A1A25 100%) !important;
        }

        /* Main content area */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(145deg, #0A0A0F 0%, #141421 50%, #1A1A25 100%) !important;
            padding: 2rem;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #0F0F15 !important;
            border-right: 1px solid #00FFFF33;
        }

        /* Headers and Titles */
        h1, h2, h3, [data-testid="stMarkdownContainer"] h1 {
            color: #00FFFF !important;
            text-shadow: 0 0 15px #00FFFF;
            animation: glow 2s ease-in-out infinite alternate;
            text-align: center !important;
            width 100%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        @keyframes glow {
            0% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
            50% { text-shadow: 0 0 20px #00FFFF, 0 0 30px #00FFFF; }
            100% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
        }

        /* Paragraph text */
        p, li, span, div {
            color: #FFFFFF !important;
        }

        /* Buttons */
        .stButton>button {
            color: #00FFFF !important;
            background-color: transparent !important;
            border: 2px solid #00FFFF !important;
            border-radius: 10px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #00FFFF !important;
            color: #0A0A0F !important;
            box-shadow: 0 0 20px #00FFFF !important;
        }

        /* DataFrame styling */
        [data-testid="stDataFrame"] {
            background-color: #141421 !important;
            color: #FFFFFF !important;
            border: 1px solid #00FFFF !important;
            border-radius: 10px;
        }

        /* ===== NEON CARD ===== */
        .neon-card {
            background-color: #141421;
            border: 2px solid #00FFFF;
            border-radius: 15px;
            padding: 20px 30px;
            margin: 20px auto;
            box-shadow: 0 0 20px #00FFFF55;
            transition: 0.3s ease-in-out;
            text-align: center;
            display: flex;
            flex-direction: column;  
            align-items: center;         
            justify-content: center;
            max-width: 500px;
            width: fit-content;     
        }

        .neon-card:hover {
            box-shadow: 0 0 35px #00FFFFAA;
            transform: scale(1.02);
        }

        .neon-title {
            color: #00FFFF;
            font-size: 24px;
            font-weight: 700;
            text-shadow: 0 0 10px #00FFFF;
            animation: glow 2s ease-in-out infinite alternate;
        }

        .neon-value {
            font-size: 36px;
            font-weight: bold;
            color: #FFFFFF;
            text-shadow: 0 0 12px #00FFFF;
        }

        .neon-subtext {
            color: #AAAAAA;
            font-size: 14px;
        }
            
        /* Responsive table width */
        [data-testid="stDataFrame"], [data-testid="stTable"] {
            max-width: 95vw !important;
            margin: auto;
            border: 1px solid #00FFFF !important;
            border-radius: 10px;
            box-shadow: 0 0 15px #00FFFF33;
        }
            
        [data-testid="stTable"] {
            width: 100% !important;
            table-layout: fixed !important;
        }    
    </style>
""", unsafe_allow_html=True)

st.title("🏈 Team Analytics")

st.write("""
Use the dropdown below to explore advanced stats for each team —
EPA trends, touchdowns, yards, and more.
""")

# --- Load Data ---
try:
    df = pd.read_csv("this_season.csv")  # Replace with your team-level stats CSV
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
col1.metric("Total Touchdowns", int(team_df['touchdown'].mean()))
col2.metric("Total Yards", int(team_df['yards_gained'].mean()))
col3.metric("Avg. EPA per Game", round(team_df['epa'].mean(), 2))
