import streamlit as st
import pandas as pd

# --- Neon CSS Styling ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Orbitron', sans-serif;
            color: #FFFFFF;
        }

        @keyframes glow {
            0% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
            50% { text-shadow: 0 0 20px #00FFFF, 0 0 30px #00FFFF; }
            100% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
        }

        /* Neon Data Card */
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

st.set_page_config(page_title="Football Moneyline Predictions", layout="wide")

st.title("🏈 Jordan's Weekly Picks")

st.write("""
- This is a weekly summary of my NFL moneyline predictions.  No machine learning model is %100 - bet at your own risk!
""")

st.write("""
- Predictions will be updated on Thursdays before TNF, and capture every game for the weekend including Monday Night.
""")

# Load the data
df = pd.read_csv("weekly_prediction.csv")

st.dataframe(df, use_container_width=True)

