import streamlit as st
import pandas as pd

st.markdown("""
    <style>
        /* Import futuristic font */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Orbitron', sans-serif;
            color: #FFFFFF;
        }

        /* === Glow Animation Keyframes === */
        @keyframes glow {
            0% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
            50% { text-shadow: 0 0 20px #00FFFF, 0 0 30px #00FFFF; }
            100% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; }
        }

        /* Headers with glowing effect */
        h1, h2, h3 {
            color: #00FFFF;
            animation: glow 2s ease-in-out infinite alternate;
        }

        /* Underline accent for h2 */
        h2 {
            border-bottom: 2px solid #00FFFF;
            padding-bottom: 4px;
            display: inline-block;
        }

        /* Buttons */
        .stButton>button {
            color: #00FFFF;
            border: 1px solid #00FFFF;
            background-color: transparent;
            border-radius: 12px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #00FFFF;
            color: #0A0A0F;
            box-shadow: 0 0 20px #00FFFF;
        }

        /* Input fields */
        .stTextInput>div>div>input, .stSelectbox>div>div>select {
            background-color: #141421;
            color: #FFFFFF;
            border: 1px solid #00FFFF;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0F0F15;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Football Moneyline Predictions", layout="wide")

st.title("🏈 Weekly Football Moneyline Predictions")

st.write("""
Welcome! These are my weekly model predictions for the football moneylines.
Data updates occur on Thursdays.
""")

# Load the data
df = pd.read_csv("weekly_prediction.csv")

st.dataframe(df,width=True)