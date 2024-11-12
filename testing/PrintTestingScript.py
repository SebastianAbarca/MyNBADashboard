import requests

class TestPlayerDataAdvancedEndpoints:
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




class TestPlayerDataAdvancedPlayoffsEndpoints:
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




class TestPlayerDataTotalsEndpoints:
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



class TestPlayerDataTotalsPlayoffsEndpoints:
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




class TestShotChartDataEndpoints:
    def __init__(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/ShotChartData"

    def base_endpoint(self):
        response = requests.get(f"{self.base_url}")
        print(f"ShotChartData Base Endpoint: Status Code = {response.status_code}")

    def distinctNames_endpoint(self):
        response = requests.get(f"{self.base_url}/distinct-player-names")
        print(f"ShotChartData Distinct Names Endpoint: Status Code = {response.status_code}")
        ##NOTE: FOR SHOT CHART DATA PLAYER HAS TO COME FROM THIS LIST

    def name_endpoint(self):
        response = requests.get(f"{self.base_url}/player/LeBron James/season/2020")
        print(f"ShotChartData Name Endpoint: Status Code = {response.status_code}")
        ##NOTE: THIS WILL RETURN THE SHOT CHART DATA

    def season_endpoint(self):
        response = requests.get(f"{self.base_url}/seasons/Lebron James")
        print(f"ShotChartData Season Endpoint: Status Code = {response.status_code}")
        ##NOTE: THIS WILL RETURN A LIST OF SEASONS





# Initialize each test class and run the methods
player_data_advanced = TestPlayerDataAdvancedEndpoints()
player_data_advanced.name_endpoint()
player_data_advanced.season_endpoint()
player_data_advanced.team_endpoint()

player_data_advanced_playoffs = TestPlayerDataAdvancedPlayoffsEndpoints()
player_data_advanced_playoffs.name_endpoint()
player_data_advanced_playoffs.season_endpoint()
player_data_advanced_playoffs.team_endpoint()

player_data_totals = TestPlayerDataTotalsEndpoints()
player_data_totals.name_endpoint()
player_data_totals.season_endpoint()
player_data_totals.team_endpoint()

player_data_totals_playoffs = TestPlayerDataTotalsPlayoffsEndpoints()
player_data_totals_playoffs.name_endpoint()
player_data_totals_playoffs.season_endpoint()
player_data_totals_playoffs.team_endpoint()


shot_chart_data = TestShotChartDataEndpoints()
shot_chart_data.base_endpoint()
shot_chart_data.name_endpoint()
shot_chart_data.season_endpoint()

