import streamlit as st
import pandas as pd
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import ShotChartDetail, commonplayerinfo, alltimeleadersgrids
from json import decoder
import GraphingHelper as gh
import json

st.title('MyNBADashboard :basketball:')
st.divider()
st.header('Your Place for all NBA Data :bar_chart:')
st.divider()
st.markdown('*Note: some charts may use random sampling for readability*')
selected_option = st.sidebar.radio(
    "Choose a section:",
    ["Players", "All Time", "Shot Data"]
)

if selected_option == "Players":
    st.header('Players')
elif selected_option == "All Time":
    st.header('All Time Leaders')
    try:
        # Fetch the All Time Leaders data
        json_data = alltimeleadersgrids.AllTimeLeadersGrids(
            league_id="00",
            per_mode_simple="Totals",
            season_type="Regular Season"
        ).get_json()

    except KeyError as e:
        st.error(f"Error fetching data: {e}")

    # Parse the JSON data into a DataFrame
    data_set = json.loads(json_data)
    all_time_data = data_set["resultSets"]
    ##st.write(all_time_data)
    # Extracting the relevant data from the first result set
    if all_time_data:

        category_option = st.selectbox(
            "Select Category:",
            ["GPLeaders", "PTSLeader", "ASTLeader", "STLLeader", "OREDLeaders", "DREBLeaders"
                , "REBLeaders", "BLKLeaders", "FGMLeaders", "FGALeaders", "FGLeaders", "FG_PCTLeaders",
             "TOVLeaders", "FG3MLeaders", "FG3ALeaders", "FG3_PCTLeaders", "PFLeaders", "FTMLeaders",
             "FTALeaders", "FT_PCTLeaders"]
        )
        # Create a DataFrame based on the selected category
        if category_option == "GPLeaders":
            headers = all_time_data[0]["headers"]
            rows = all_time_data[0]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'GP', 'GP_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Games Played', 'Ranking', 'Active Status']
            st.subheader("Games Played Leader")
            df_visual_sorted = df_visual.sort_values(by='Games Played', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Games Played'])

        elif category_option == "PTSLeader":
            headers = all_time_data[1]["headers"]
            rows = all_time_data[1]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'PTS', 'PTS_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Points', 'Ranking', 'Active Status']
            st.subheader("Points Leader")
            df_visual_sorted = df_visual.sort_values(by='Points', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Points'])

        elif category_option == "ASTLeader":
            headers = all_time_data[2]["headers"]
            rows = all_time_data[2]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'AST', 'AST_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Assists', 'Ranking', 'Active Status']
            st.subheader("Assists Leader")
            df_visual_sorted = df_visual.sort_values(by='Assists', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Assists'])

        elif category_option == "STLLeader":
            headers = all_time_data[3]["headers"]
            rows = all_time_data[3]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'STL', 'STL_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Steals', 'Ranking', 'Active Status']
            st.subheader("Steals Leader")
            df_visual_sorted = df_visual.sort_values(by='Steals', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Steals'])

        elif category_option == "OREDLeaders":
            headers = all_time_data[4]["headers"]
            rows = all_time_data[4]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'OREB', 'OREB_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Offensive Rebounds', 'Ranking', 'Active Status']
            st.subheader("Offensive Rebounds Leader")
            df_visual_sorted = df_visual.sort_values(by='Offensive Rebounds', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Offensive Rebounds'])

        elif category_option == "DREBLeaders":
            headers = all_time_data[5]["headers"]
            rows = all_time_data[5]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'DREB', 'DREB_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Defensive Rebounds', 'Ranking', 'Active Status']
            st.subheader("Defensive Rebounds Leader")
            df_visual_sorted = df_visual.sort_values(by='Defensive Rebounds', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Defensive Rebounds'])

        elif category_option == "REBLeaders":
            headers = all_time_data[6]["headers"]
            rows = all_time_data[6]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'REB', 'REB_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Rebounds', 'Ranking', 'Active Status']
            st.subheader("Rebounds Leader")
            df_visual_sorted = df_visual.sort_values(by='Rebounds', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Rebounds'])

        elif category_option == "BLKLeaders":
            headers = all_time_data[7]["headers"]
            rows = all_time_data[7]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'BLK', 'BLK_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Blocks', 'Ranking', 'Active Status']
            st.subheader("Blocks Leader")
            df_visual_sorted = df_visual.sort_values(by='Blocks', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Blocks'])

        elif category_option == "FGMLeaders":
            headers = all_time_data[8]["headers"]
            rows = all_time_data[8]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FGM', 'FGM_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Field Goals Made', 'Ranking', 'Active Status']
            st.subheader("Field Goals Made Leader")
            df_visual_sorted = df_visual.sort_values(by='Field Goals Made', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Field Goals Made'])

        elif category_option == "FGALeaders":
            headers = all_time_data[9]["headers"]
            rows = all_time_data[9]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FGA', 'FGA_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Field Goals Attempted', 'Ranking', 'Active Status']
            st.subheader("Field Goals Attempted Leader")
            df_visual_sorted = df_visual.sort_values(by='Field Goals Attempted', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Field Goals Attempted'])

        elif category_option == "FGLeaders":
            headers = all_time_data[10]["headers"]
            rows = all_time_data[10]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'FG_PCT_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Field Goals Made', 'Field Goals Attempted', 'Field Goal %', 'Ranking',
                                 'Active Status']
            st.subheader("Field Goal % Leader")
            df_visual_sorted = df_visual.sort_values(by='Field Goal %', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Field Goal %'])

        elif category_option == "FG_PCTLeaders":
            headers = all_time_data[11]["headers"]
            rows = all_time_data[11]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FG_PCT', 'FG_PCT_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Field Goal %', 'Ranking', 'Active Status']
            st.subheader("Field Goal % Leader")
            df_visual_sorted = df_visual.sort_values(by='Field Goal %', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Field Goal %'])

        elif category_option == "TOVLeaders":
            headers = all_time_data[12]["headers"]
            rows = all_time_data[12]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'TOV', 'TOV_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Turnovers', 'Ranking', 'Active Status']
            st.subheader("Turnovers Leader")
            df_visual_sorted = df_visual.sort_values(by='Turnovers', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Turnovers'])

        elif category_option == "FG3MLeaders":
            headers = all_time_data[13]["headers"]
            rows = all_time_data[13]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FG3M', 'FG3M_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', '3-Point Field Goals Made', 'Ranking', 'Active Status']
            st.subheader("3-Point Field Goals Made Leader")
            df_visual_sorted = df_visual.sort_values(by='3-Point Field Goals Made', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['3-Point Field Goals Made'])

        elif category_option == "FG3PCTLeaders":
            headers = all_time_data[14]["headers"]
            rows = all_time_data[14]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FG3_PCT', 'FG3_PCT_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', '3-Point Field Goal %', 'Ranking', 'Active Status']
            st.subheader("3-Point Field Goal % Leader")
            df_visual_sorted = df_visual.sort_values(by='3-Point Field Goal %', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['3-Point Field Goal %'])

        elif category_option == "FTMLeaders":
            headers = all_time_data[16]["headers"]
            rows = all_time_data[16]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FTM', 'FTM_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Free Throws Made', 'Ranking', 'Active Status']
            st.subheader("Free Throws Made Leader")
            df_visual_sorted = df_visual.sort_values(by='Free Throws Made', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Free Throws Made'])

        elif category_option == "FTALeaders":
            headers = all_time_data[17]["headers"]
            rows = all_time_data[17]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FTA', 'FTA_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Free Throws Attempted', 'Ranking', 'Active Status']
            st.subheader("Free Throws Attempted Leader")
            df_visual_sorted = df_visual.sort_values(by='Free Throws Attempted', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Free Throws Attempted'])

        elif category_option == "FT_PCTLeaders":
            headers = all_time_data[18]["headers"]
            rows = all_time_data[18]["rowSet"]

            # Convert it to a pandas DataFrame for easier display
            df_all_time = pd.DataFrame(rows, columns=headers)
            df_visual = df_all_time[['PLAYER_NAME', 'FT_PCT', 'FT_PCT_RANK', 'IS_ACTIVE_FLAG']]
            df_visual.columns = ['Player', 'Free Throw %', 'Ranking', 'Active Status']
            st.subheader("Free Throw % Leader")
            df_visual_sorted = df_visual.sort_values(by='Free Throw %', ascending=False)
            st.bar_chart(df_visual_sorted.set_index('Player')['Free Throw %'])

        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown("**Note**: Data and rankings are sourced from NBA API.")

        # Display the DataFrame as a table in Streamlit
        st.dataframe(df_visual_sorted)

elif selected_option == "Shot Data":
    st.header('Shot Data')
    players_dict = players.get_active_players()
    names = ['']
    for player in players_dict:
        names.append(player['full_name'])

    selected_player = st.selectbox('Player Name', names)
    if selected_player:
        player_instance = players.find_players_by_full_name(selected_player)
        player_id = player_instance[0]['id']
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_json()
        player_info = decoder.JSONDecoder().decode(player_info)
        team_id = player_info['resultSets'][0]['rowSet'][0][18]
        shot_chart_df = ShotChartDetail(player_id=player_id, team_id=team_id).get_data_frames()[0]
        shot_chart_df['TOTAL_TIME_SECONDS'] = (
                shot_chart_df['SECONDS_REMAINING'].astype(int) + (shot_chart_df['MINUTES_REMAINING'].astype(int) * 60))
        shot_chart_df = shot_chart_df.drop(columns=['SECONDS_REMAINING', 'MINUTES_REMAINING'])
        st.dataframe(shot_chart_df)
        if shot_chart_df.empty:
            st.error('Sorry :neutral_face: no shot data available')

        radioOptions = ['', 'Shot Map', 'Histograms']
        radioChoice = st.radio('Select your Visualization', radioOptions)
        if radioChoice == 'Shot Map':
            st.plotly_chart(gh.shotChartVisual(shot_chart_df,selected_player), use_container_width=True)
        if radioChoice == 'Histograms':
            cols = ['', 'PERIOD', 'ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE']
            st.warning('The period option must be chosen on its own sorry :(')
            column_selections = st.multiselect('Select your Variables', cols)
            st.plotly_chart(gh.histogram(shot_chart_df, column_selections), use_container_width=True)
