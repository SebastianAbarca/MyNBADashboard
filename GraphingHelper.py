import streamlit as st
import requests
import json
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as datetime
import numpy as np
from APIHelper import NbaApiHelper


def create_scatter_plot(shot_chart_df, selected_player, x_column, y_column):
    """
    Generalized function to create a Plotly scatter plot for shot chart data.

    Parameters:
    - shot_chart_df: DataFrame containing the shot chart data
    - selected_player: str, name of the selected player for title
    - x_column: str, column name to use for the x-axis
    - y_column: str, column name to use for the y-axis

    Returns:
    - fig: Plotly Figure object
    """

    # Convert timeRemaining to seconds for both x and y columns if they are set to 'timeRemaining'
    if x_column == 'timeRemaining':
        shot_chart_df['timeRemaining'] = shot_chart_df['timeRemaining'].apply(
            lambda x: int(x.split(':')[0]) * 60 + int(round(float(x.split(':')[1])))
        )
    if y_column == 'timeRemaining':
        shot_chart_df['timeRemaining'] = shot_chart_df['timeRemaining'].apply(
            lambda x: int(x.split(':')[0]) * 60 + int(round(float(x.split(':')[1])))
        )

    # Randomly sample half of the data
    shot_chart_df = shot_chart_df.sample(frac=0.5, random_state=42)

    # Separate missed and made shots
    missed = shot_chart_df[shot_chart_df['result'] == False]
    made = shot_chart_df[shot_chart_df['result'] == True]

    # Create the Plotly figure
    fig = go.Figure()

    # Add scatter for missed shots
    fig.add_trace(go.Scatter(
        x=missed[x_column],
        y=missed[y_column],
        mode='markers',
        marker=dict(color='red', size=8),
        name='Missed'
    ))

    # Add scatter for made shots
    fig.add_trace(go.Scatter(
        x=made[x_column],
        y=made[y_column],
        mode='markers',
        marker=dict(color='green', size=8),
        name='Made'
    ))

    # Customize layout
    fig.update_layout(
        title=f"{selected_player}'s Shots by {y_column} and {x_column}",
        xaxis_title=x_column,
        yaxis_title=y_column,
        template="simple_white",
        legend=dict(title="Shot Result"),
    )

    # Customize x-axis if x_column involves time
    if x_column == 'timeRemaining':
        fig.update_xaxes(
            tickmode='array',
            tickvals=np.arange(0, 12 * 60 + 1, 60),
            ticktext=[f"{int(val // 60):02}:{int(val % 60):02}" for val in np.arange(0, 12 * 60 + 1, 60)],
            showgrid=True,
            gridcolor='lightgrey'
        )

    # Customize y-axis if y_column involves time
    if y_column == 'timeRemaining':
        fig.update_yaxes(
            tickmode='array',
            tickvals=np.arange(0, 12 * 60 + 1, 60),
            ticktext=[f"{int(val // 60):02}:{int(val % 60):02}" for val in np.arange(0, 12 * 60 + 1, 60)],
            showgrid=True,
            gridcolor='lightgrey'
        )

    # Customize x-axis for quarters if x_column is 'qtr'
    if x_column == 'qtr':
        fig.update_xaxes(
            tickvals=[0, 1, 2, 3, 4, 5],
            ticktext=['Q1', 'Q2', 'Q3', 'Q4', 'OT1', 'OT2'],
            showgrid=True,
            gridcolor='lightgrey'
        )

    # Customize y-axis for quarters if y_column is 'qtr'
    if y_column == 'qtr':
        fig.update_yaxes(
            tickvals=[0, 1, 2, 3, 4, 5],
            ticktext=['Q1', 'Q2', 'Q3', 'Q4', 'OT1', 'OT2'],
            showgrid=True,
            gridcolor='lightgrey'
        )

    return fig



def create_bar_chart(shot_chart_data, selected_player, x_axis):
    df = pd.DataFrame(shot_chart_data)

    # Group data by x_axis and filter by result (True for made, False for missed)
    made_shots = df[df['result'] == True].groupby(x_axis).size()
    missed_shots = df[df['result'] == False].groupby(x_axis).size()

    # Combine the counts into a single DataFrame
    grouped_data = pd.DataFrame({'Made': made_shots, 'Missed': missed_shots})

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=grouped_data.index,
        y=grouped_data['Made'],
        name='Made',
        marker_color='green'
    ))
    fig.add_trace(go.Bar(
        x=grouped_data.index,
        y=grouped_data['Missed'],
        name='Missed',
        marker_color='red'
    ))

    fig.update_layout(
        title=f"{selected_player}'s Shot Distribution by {x_axis}",
        xaxis_title=x_axis,
        yaxis_title='Count',
        barmode='stack'
    )

    return fig