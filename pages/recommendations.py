import streamlit as st

from utils.insights import (
    generate_recommendations
)

st.title("💡 Career Recommendations")

gpa = st.number_input(
    "GPA",
    2.0,
    4.0,
    3.0
)

internships = st.number_input(
    "Internships",
    0,
    10,
    1
)

projects = st.number_input(
    "Projects",
    0,
    20,
    2
)

certifications = st.number_input(
    "Certifications",
    0,
    10,
    1
)

networking = st.number_input(
    "Networking",
    1,
    10,
    5
)

soft_skills = st.number_input(
    "Soft Skills",
    1,
    10,
    5
)

if st.button("Generate Recommendations"):

    recommendations = generate_recommendations(
        gpa,
        internships,
        projects,
        certifications,
        networking,
        soft_skills
    )

    for rec in recommendations:
        st.warning(rec)
