import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/education_career_success.csv"
)

st.title("📈 Career Analytics")

fig = px.scatter(
    df,
    x="University_GPA",
    y="Starting_Salary",
    color="Field_of_Study",
    size="Job_Offers",
    hover_name="Current_Job_Level"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

field_salary = (
    df.groupby("Field_of_Study")
    ["Starting_Salary"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    field_salary,
    x="Field_of_Study",
    y="Starting_Salary",
    title="Average Salary by Field"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
