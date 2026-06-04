import plotly.express as px
import plotly.graph_objects as go


def success_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Career Success Score"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    return fig


def salary_distribution(df):

    return px.histogram(
        df,
        x="Starting_Salary",
        nbins=25,
        title="Salary Distribution"
    )


def correlation_heatmap(df):

    numeric = df.select_dtypes(include="number")

    corr = numeric.corr()

    return px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Matrix"
    )
