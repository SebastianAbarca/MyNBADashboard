import requests
import streamlit as st

class NbaApiHelper:
    class PlayerDataAdvanced:
        def __init__(self):
            self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvanced"

        def name_endpoint(self):
            response = requests.get(f"{self.base_url}/name/Lebron James")
            print(f"PlayerDataAdvanced Name Endpoint: Status Code = {response.status_code}")

        def season_endpoint(self):
            response = requests.get(f"{self.base_url}/season/2023")
            print(f"PlayerDataAdvanced Season Endpoint: Status Code = {response.status_code}")

        def team_endpoint(self):
            response = requests.get(f"{self.base_url}/team/LAL")
            print(f"PlayerDataAdvanced Team Endpoint: Status Code = {response.status_code}")

    class PlayerDataAdvancedPlayoffs:
        def __init__(self):
            self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs"

        def name_endpoint(self):
            response = requests.get(f"{self.base_url}/name/Lebron James")
            print(f"PlayerDataAdvancedPlayoffs Name Endpoint: Status Code = {response.status_code}")

        def season_endpoint(self):
            response = requests.get(f"{self.base_url}/season/2023")
            print(f"PlayerDataAdvancedPlayoffs Season Endpoint: Status Code = {response.status_code}")

        def team_endpoint(self):
            response = requests.get(f"{self.base_url}/team/LAL")
            print(f"PlayerDataAdvancedPlayoffs Team Endpoint: Status Code = {response.status_code}")

    class PlayerDataTotals:
        def __init__(self):
            self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals"

        def name_endpoint(self):
            response = requests.get(f"{self.base_url}/name/Lebron James")
            print(f"PlayerDataTotals Name Endpoint: Status Code = {response.status_code}")

        def season_endpoint(self):
            response = requests.get(f"{self.base_url}/season/2023")
            print(f"PlayerDataTotals Season Endpoint: Status Code = {response.status_code}")

        def team_endpoint(self):
            response = requests.get(f"{self.base_url}/team/LAL")
            print(f"PlayerDataTotals Team Endpoint: Status Code = {response.status_code}")

    class PlayerDataTotalsPlayoffs:
        def __init__(self):
            self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotalsPlayoffs"

        def name_endpoint(self):
            response = requests.get(f"{self.base_url}/name/Lebron James")
            print(f"PlayerDataTotalsPlayoffs Name Endpoint: Status Code = {response.status_code}")

        def season_endpoint(self):
            response = requests.get(f"{self.base_url}/season/2023")
            print(f"PlayerDataTotalsPlayoffs Season Endpoint: Status Code = {response.status_code}")

        def team_endpoint(self):
            response = requests.get(f"{self.base_url}/team/LAL")
            print(f"PlayerDataTotalsPlayoffs Team Endpoint: Status Code = {response.status_code}")

    class ShotChartData:
        def __init__(self):
            self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/ShotChartData"

        def base_endpoint(self):
            response = requests.get(f"{self.base_url}")
            print(f"ShotChartData Base Endpoint: Status Code = {response.status_code}")

        def distinct_names_endpoint(self):
            response = requests.get(f"{self.base_url}/distinct-player-names")
            print(f"ShotChartData Distinct Names Endpoint: Status Code = {response.status_code}")
            return response.json()
            ##NOTE: FOR SHOT CHART DATA PLAYER HAS TO COME FROM THIS LIST

        def name_endpoint(self, name, year):
            response = requests.get(f"{self.base_url}/player/{name}/season/{year}")
            return response.json()
            print(f"ShotChartData Name Endpoint: Status Code = {response.status_code}")
            ##NOTE: THIS WILL RETURN THE SHOT CHART DATA

        def season_endpoint(self, name):
            response = requests.get(f"{self.base_url}/seasons/{name}")
            return response.json()
            print(f"ShotChartData Season Endpoint: Status Code = {response.status_code}")
            ##NOTE: THIS WILL RETURN A LIST OF SEASONS
