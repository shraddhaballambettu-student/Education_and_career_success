import streamlit as st

from utils.calculations import (
    calculate_success_score,
    calculate_promotion_score,
    career_level
)

from utils.charts import success_gauge

st.title("🎯 Career Success Calculator")

col1, col2 = st.columns(2)

with col1:

    gpa = st.slider(
        "University GPA",
        2.0,
        4.0,
        3.5
    )

    internships = st.slider(
        "Internships",
        0,
        10,
        2
    )

    projects = st.slider(
        "Projects",
        0,
        20,
        5
    )

with col2:

    certifications = st.slider(
        "Certifications",
        0,
        10,
        2
    )

    networking = st.slider(
        "Networking",
        1,
        10,
        7
    )

    soft_skills = st.slider(
        "Soft Skills",
        1,
        10,
        7
    )

if st.button("Calculate"):

    success = calculate_success_score(
        gpa,
        internships,
        projects,
        certifications,
        networking,
        soft_skills
    )

    promotion = calculate_promotion_score(
        projects,
        certifications,
        networking,
        soft_skills
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Success Score",
        f"{success}%"
    )

    c2.metric(
        "Promotion Score",
        f"{promotion}%"
    )

    c3.metric(
        "Level",
        career_level(success)
    )

    st.plotly_chart(
        success_gauge(success),
        use_container_width=True
    )
