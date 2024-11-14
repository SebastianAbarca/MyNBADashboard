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
import GraphingHelper as gh


##make an instance of all api helpers
nba_api = NbaApiHelper()
shot_chart = nba_api.ShotChartData()
player_data_advanced = nba_api.PlayerDataAdvanced()
player_data_totals = nba_api.PlayerDataTotals()
player_data_advanced_playoffs = nba_api.PlayerDataAdvancedPlayoffs()
player_data_totals_playoffs = nba_api.PlayerDataTotalsPlayoffs()

##all available years
current_year = datetime.datetime.now().year
years = [""] + [str(year) for year in range(current_year, 2008, -1)]

distinct_players = shot_chart.distinct_names_endpoint()

st.title('MyNBADashboard :basketball:')
st.header('Your Place for all NBA Data :bar_chart:')
st.write('Note: some charts may use random sampling for readability')
selected_option = st.sidebar.radio(
    "Choose a section:",
    ["Players", "Playoffs", "Shot Charts"]
)


if selected_option == "Players":
    st.header('Players')
elif selected_option == "Playoffs":
    st.header('Playoffs')
elif selected_option == "Shot Charts":
    st.header('Shot Charts')
    selected_player = st.selectbox('Select a player', distinct_players)

    if selected_player:
        shot_chart_years = shot_chart.season_endpoint(selected_player)
        selected_year = st.selectbox('Select a year', shot_chart_years)

        if selected_year:
            st.write("Note: when interacting with figure Time Remaining is show in seconds (distance, time in seconds)")
            shot_chart_data = shot_chart.name_endpoint(selected_player,selected_year)
            shot_chart_dataFrame = pd.DataFrame(shot_chart_data)
            st.write(shot_chart_dataFrame.describe())
            st.dataframe(shot_chart_data)
            plot_type = st.radio('Plot Type:', ['Scatter plot', 'Bar plot', 'Shot map'])

            if plot_type == 'Scatter plot':
                scatter_columns = ['qtr', 'timeRemaining', 'distanceFt', 'opponent']
                scatter_df = shot_chart_dataFrame[scatter_columns]
                selected_columns = st.multiselect("Statistical Categories", scatter_columns, max_selections=2)
                st.markdown(f"Selected columns: {selected_columns}")
                if selected_columns.__len__() == 2:
                    scatter_fig = gh.create_scatter_plot(shot_chart_dataFrame, selected_player, selected_columns[0], selected_columns[1])
                    st.plotly_chart(scatter_fig, use_container_width=True)


            if plot_type == 'Bar plot':
                x_axis_bar_columns = ['','qtr', 'opponent', 'lead']
                bar_option = st.selectbox("What data would you like to explore?", x_axis_bar_columns)
                if bar_option:
                    bar_fig = gh.create_bar_chart(shot_chart_data, selected_player, bar_option)
                    st.plotly_chart(bar_fig, use_container_width=True)


            if plot_type == 'Shot map':
                shot_map = gh.create_shot_map(shot_chart_data, selected_player)
                st.pyplot(shot_map, use_container_width=True)
