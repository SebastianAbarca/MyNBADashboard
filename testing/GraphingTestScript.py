import plotly
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as datetime
from APIHelper import NbaApiHelper

nbaApiHelper = NbaApiHelper()
shot_chart = nbaApiHelper.ShotChartData()


def create_shot_chart(selected_player, shotChartDataFrame):
    """Creates a Seaborn scatterplot for shot chart data."""
    fig, ax = plt.subplots()  # Create a figure and axes for Seaborn compatibility
    sns.scatterplot(ax=ax, data=shotChartDataFrame, x='timeRemaining', y='distanceFt', hue='result', hue_order=[False, True])
    handles, labels = ax.get_legend_handles_labels()

    # Replace the legend labels
    new_labels = ['Missed', 'Made']

    # Set the new labels to the legend
    ax.legend(handles, new_labels)
    ax.set_title(f"{selected_player}'s Shot Data")  # Use f-string for dynamic title
    ax.set_xlabel("Time Remaining")
    ax.set_ylabel("Distance Ft")
    plt.figure(figsize=(15, 10))
    return fig  # Return the figure for Streamlit display


shot_chart_data = shot_chart.name_endpoint("LeBron James","2020")
shotChartDataFrame = pd.DataFrame(shot_chart_data)
print(shotChartDataFrame['timeRemaining'].sort_values(ascending=True))
shotChartDataFrame['timeRemaining'] = shotChartDataFrame['timeRemaining'].apply(lambda x: int(x.split(':')[0]) * 100 + int(x.split(':')[1]))
print(shotChartDataFrame['timeRemaining'].sort_values(ascending=True))
fig = create_shot_chart("LeBron James", shotChartDataFrame)
plt.show()