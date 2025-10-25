import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

st.markdown("""
    <style>
        /* Import Orbitron font */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

        /* ===== GLOBAL STYLING ===== */
        html, body, [class^="st-"], [class^="css-"]:not(.material-icons) {
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
        h1,h2, [data-testid="stMarkdownContainer"] h1 {
            color: #00FFFF !important;
            text-shadow: 0 0 15px #00FFFF;
            animation: glow 2s ease-in-out infinite alternate;
            text-align: center !important;
            width 100%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
            
        h3, [data-testid="stMarkdownContainer"] h3 {
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

st.title("📊 Team Comparison Analytics")
st.markdown("<p style='text-align:center;'>Select two teams to compare EPA, touchdowns, and yards over the season.</p>", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_team_season(path="this_season.csv") -> pd.DataFrame:
    # expected columns: team, week, epa, touchdowns, yards
    return pd.read_csv(path)

try:
    df = load_team_season()
    teams = sorted(df["team"].unique().tolist())

    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        team_a = st.selectbox("Team A", teams, index=0)
    with col_sel2:
        team_b = st.selectbox("Team B", teams, index=1)

    team_a_df = df[df["team"] == team_a].sort_values("week")
    team_b_df = df[df["team"] == team_b].sort_values("week")

    # ---- KPI Row ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("Team Stats")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h3 style='color:#D16D02;text-align:center'>{team_a}</h3>", unsafe_allow_html=True)
        st.metric("Average TDs", int(team_a_df["touchdown"].mean()))
        st.metric("Average Yards", int(team_a_df["yards_gained"].mean()))
        st.metric("Avg EPA", round(team_a_df["epa"].mean(), 3))

    with col2:
        st.markdown(f"<h3 style='color:#FF00FF;text-align:center'>{team_b}</h3>", unsafe_allow_html=True)
        st.metric("Average TDs", int(team_b_df["touchdown"].mean()))
        st.metric("Average Yards", int(team_b_df["yards_gained"].mean()))
        st.metric("Avg EPA", round(team_b_df["epa"].mean(), 3))

    # ---- EPA Trend Comparison ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("EPA Trend Comparison")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["epa"],
        mode="lines+markers",
        name=team_a,
        line=dict(color="#D16D02", width=3),
        marker=dict(size=8, color="#D16D02")
    ))
    fig.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["epa"],
        mode="lines+markers",
        name=team_b,
        line=dict(color="#FF00FF", width=3),
        marker=dict(size=8, color="#FF00FF")
    ))
    fig.update_layout(
        title=f"{team_a} vs {team_b} — EPA by Week",
        paper_bgcolor="#0A0A0F",
        plot_bgcolor="#0A0A0F",
        font=dict(color="#FFFFFF", family="Orbitron"),
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ---- Yards Comparison ----
    st.subheader("Yards Trend")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["yards_gained"],
        mode="lines+markers", name=f"{team_a} Yards",
        line=dict(color="#D16D02")
    ))
    fig2.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["yards_gained"],
        mode="lines+markers", name=f"{team_b} Yards",
        line=dict(color="#FF00FF")
    ))
    fig2.update_layout(
        paper_bgcolor="#0A0A0F",
        plot_bgcolor="#0A0A0F",
        font=dict(color="#FFFFFF", family="Orbitron"),
        hovermode="x unified"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ---- Touchdowns Comparison ----
    st.subheader("Touchdown Trend")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["touchdown"],
        mode="lines+markers", name=f"{team_a} Touchdowns",
        line=dict(color="#D16D02")
    ))
    fig2.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["touchdown"],
        mode="lines+markers", name=f"{team_b} Touchdowns",
        line=dict(color="#FF00FF")
    ))
    fig2.update_layout(
        paper_bgcolor="#0A0A0F",
        plot_bgcolor="#0A0A0F",
        font=dict(color="#FFFFFF", family="Orbitron"),
        hovermode="x unified"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ---- Raw Data Display ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("Raw Data (Selected Teams)")
    st.dataframe(pd.concat([team_a_df, team_b_df]).reset_index(drop=True), use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")

