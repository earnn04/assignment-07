import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt

    # Load the features file your pipeline generated
    df = pd.read_csv("data/features/events.csv")
    return alt, df, mo


@app.cell
def _(alt, df, mo):
    # Create an Altair histogram of the duration_minutes column
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X("duration_minutes:Q", bin=True, title="Event Duration (Minutes)"),
            alt.Y("count()", title="Number of Events")
        )
        .properties(
            title="Distribution of Event Durations",
            width=600,
            height=400
        )
    )

    # Display the chart in Marimo
    mo.ui.altair_chart(chart)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
