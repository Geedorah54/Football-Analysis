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

'''
# Optional: sort or filter
df = df.sort_values(by="Confidence", ascending=False)
'''

st.dataframe(df, use_container_width=True)

'''
# Optional chart
st.bar_chart(df.set_index("Team")["Confidence"])
'''
