import streamlit as st

st.set_page_config(
    page_title="Career Success Platform",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Education Career Success Analytics")

st.markdown("""
Analyze career growth, salary trends,
promotion readiness and satisfaction metrics.
""")

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

[data-testid="stMetric"]{
    background:#f4f6f8;
    padding:15px;
    border-radius:12px;
}

div[data-testid="stPlotlyChart"]{
    border-radius:12px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)
