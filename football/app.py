import streamlit as st
import pandas as pd

st.set_page_config(page_title="Football Moneyline Predictions", layout="wide")

st.title("🏈 Weekly Football Moneyline Predictions")

st.write("""
Welcome! These are my weekly model predictions for the football moneylines.
Data updates occur on Thursdays.
""")

# Load the data
df = pd.read_csv("football/weekly_prediction.csv")

st.dataframe(df, use_container_width=True)

