import requests
import unittest


class TestPlayerDataAdvancedEndpoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvanced"

    def test_query_endpoint(self):
        response = requests.get(f"{self.base_url}/query")
        self.assertEqual(response.status_code, 200)

    def test_name_endpoint(self):
        response = requests.get(f"{self.base_url}/name/Lebron James")
        self.assertEqual(response.status_code, 200)

    def test_season_endpoint(self):
        response = requests.get(f"{self.base_url}/season/2023")
        self.assertEqual(response.status_code, 200)

    #def test_player_id_endpoint(self):
        #response = requests.get(f"{self.base_url}/playerid/2544")
        #self.assertEqual(response.status_code, 200)

    def test_team_endpoint(self):
        response = requests.get(f"{self.base_url}/team/LAL")
        self.assertEqual(response.status_code, 200)

    def test_count_endpoint(self):
        response = requests.get(f"{self.base_url}/count")
        self.assertEqual(response.status_code, 200)


class TestPlayerDataAdvancedPlayoffsEndpoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs"

    def test_query_endpoint(self):
        response = requests.get(f"{self.base_url}/query")
        self.assertEqual(response.status_code, 200)

    def test_name_endpoint(self):
        response = requests.get(f"{self.base_url}/name/Lebron James")
        self.assertEqual(response.status_code, 200)

    def test_season_endpoint(self):
        response = requests.get(f"{self.base_url}/season/2023")
        self.assertEqual(response.status_code, 200)

    #def test_player_id_endpoint(self):
        #response = requests.get(f"{self.base_url}/playerid/2544")
        #self.assertEqual(response.status_code, 200)

    def test_team_endpoint(self):
        response = requests.get(f"{self.base_url}/team/LAL")
        self.assertEqual(response.status_code, 200)

    def test_count_endpoint(self):
        response = requests.get(f"{self.base_url}/count")
        self.assertEqual(response.status_code, 200)


class TestPlayerDataTotalsEndpoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals"

    def test_query_endpoint(self):
        response = requests.get(f"{self.base_url}/query")
        self.assertEqual(response.status_code, 200)

    def test_name_endpoint(self):
        response = requests.get(f"{self.base_url}/name/Lebron James")
        self.assertEqual(response.status_code, 200)

    def test_season_endpoint(self):
        response = requests.get(f"{self.base_url}/season/2023")
        self.assertEqual(response.status_code, 200)

    #def test_player_id_endpoint(self):
        #response = requests.get(f"{self.base_url}/playerid/2544")
        #self.assertEqual(response.status_code, 200)

    def test_team_endpoint(self):
        response = requests.get(f"{self.base_url}/team/LAL")
        self.assertEqual(response.status_code, 200)

    def test_count_endpoint(self):
        response = requests.get(f"{self.base_url}/count")
        self.assertEqual(response.status_code, 200)


class TestPlayerDataTotalsPlayoffsEndpoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotalsPlayoffs"

    def test_query_endpoint(self):
        response = requests.get(f"{self.base_url}/query")
        self.assertEqual(response.status_code, 200)

    def test_name_endpoint(self):
        response = requests.get(f"{self.base_url}/name/Lebron James")
        self.assertEqual(response.status_code, 200)

    def test_season_endpoint(self):
        response = requests.get(f"{self.base_url}/season/2023")
        self.assertEqual(response.status_code, 200)

    #def test_player_id_endpoint(self):
        #response = requests.get(f"{self.base_url}/playerid/2544")
        #self.assertEqual(response.status_code, 200)

    def test_team_endpoint(self):
        response = requests.get(f"{self.base_url}/team/LAL")
        self.assertEqual(response.status_code, 200)

    def test_count_endpoint(self):
        response = requests.get(f"{self.base_url}/count")
        self.assertEqual(response.status_code, 200)


class TestShotChartDataEndpoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/ShotChartData"

    def test_query_endpoint(self):
        response = requests.get(f"{self.base_url}/query")
        self.assertEqual(response.status_code, 200)

    def test_name_endpoint(self):
        response = requests.get(f"{self.base_url}/name/Lebron James")
        self.assertEqual(response.status_code, 500)

    def test_season_endpoint(self):
        response = requests.get(f"{self.base_url}/season/2023")
        self.assertEqual(response.status_code, 500)

    #def test_player_id_endpoint(self):
        #response = requests.get(f"{self.base_url}/playerid/2544")
        #self.assertEqual(response.status_code, 200)

    def test_team_endpoint(self):
        response = requests.get(f"{self.base_url}/team/LAL")
        self.assertEqual(response.status_code, 500)

    def test_count_endpoint(self):
        response = requests.get(f"{self.base_url}/count")
        self.assertEqual(response.status_code, 404)


##NOTE: PlayerDataAdvanced by id is confusing me
##NOTE 2: Im just getting rid of by id endpoints I dont see how they'll be useful for us
