import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/education_career_success.csv"
)

st.title("📄 Reports")

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "career_report.csv",
    "text/csv"
)
