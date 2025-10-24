import streamlit as st
import pandas as pd

st.set_page_config(page_title="Football Moneyline Predictions", layout="wide")

st.title("🏈 Jordan's Weekly Picks")

st.write("""
This is a weekly summary of my NFL moneyline predictions.  No machine learning model is %100 - bet at your own risk!
""")

# Load the data
df = pd.read_csv("football/weekly_prediction.csv")

st.dataframe(df, use_container_width=True)

