import streamlit as st
import pandas as pd
from utils.charts import (
    salary_distribution,
    correlation_heatmap
)

df = pd.read_csv(
    "data/education_career_success.csv"
)

st.title("📊 Executive Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Salary",
    f"${df['Starting_Salary'].mean():,.0f}"
)

col2.metric(
    "Average Job Offers",
    round(df["Job_Offers"].mean(), 1)
)

col3.metric(
    "Career Satisfaction",
    round(
        df["Career_Satisfaction"].mean(),
        2
    )
)

st.plotly_chart(
    salary_distribution(df),
    use_container_width=True
)

st.plotly_chart(
    correlation_heatmap(df),
    use_container_width=True
)
