import streamlit as st
import pandas as pd

# ------------------------------------------------------------
# PAGE CONFIG (must be first Streamlit call)
# ------------------------------------------------------------
st.set_page_config(
    page_title="Football Moneyline Predictions",
    layout="wide",
)

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------
st.markdown("""
    <style>
        /* Import Orbitron font */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

        /* ===== GLOBAL STYLING ===== */
        html, body, [class^="st-"], [class^="css-"] {
            font-family: 'Orbitron', sans-serif !important;
            color: #FFFFFF !important;
            background-color: #0A0A0F !important;
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
            padding: 20px;
            margin: 20px 0px;
            box-shadow: 0 0 20px #00FFFF55;
            transition: 0.3s ease-in-out;
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
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# PAGE CONTENT
# ------------------------------------------------------------

st.title("🏈 Jordan's Weekly Picks")

st.write("""
- This is a weekly summary of my NFL moneyline predictions.  
  No machine learning model is 100% accurate — bet responsibly!
""")

st.write("""
- Predictions are updated **Thursdays before TNF**,  
  covering all weekend games and Monday Night Football.
""")

# Neon data card example
st.markdown("""
<div class="neon-card">
    <div class="neon-title">Weekly Summary</div>
    <div class="neon-value">13 / 15 Correct</div>
    <div class="neon-subtext">Last week’s results</div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# DATA TABLE
# ------------------------------------------------------------
try:
    df = pd.read_csv("weekly_prediction.csv")
    st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.error("⚠️ weekly_prediction.csv not found. Upload or add it to the project folder.")
