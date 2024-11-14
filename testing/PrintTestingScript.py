import requests
from matplotlib import image as mpimg, pyplot as plt
import plotly.graph_objects as go
from PIL import Image
import numpy as np



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




'''
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


# Load the court diagram image
court_img_path = 'court.png'  # Replace with your actual image path

court_img = mpimg.imread(court_img_path)


# Get image dimensions
image_width, image_height = court_img.shape[:2]

# Sample data point (replace with your actual data)
data_point = {
    "id": 33253,
    "playerName": "LeBron James",
    "top": 93,
    "left": 95
}

# Normalize data points
normalized_top = data_point["top"] / image_height
normalized_left = data_point["left"] / image_width

# Create a figure object
fig = go.Figure()

fig.add_layout_image(
    x=0,  # x position of the bottom left corner
    y=0,  # y position of the bottom left corner
    sizex=image_width,  # width of the image
    sizey=image_height,  # height of the image
    source=court_img_path,  # path or data of the image
)


# Create scatter trace for data point
trace = go.Scatter(
    x=[normalized_left * image_width],  # List of x-coordinates
    y=[normalized_top * image_height],   # List of y-coordinates
    mode="markers",  # Set to 'markers' for scatter plot
    marker=dict(size=50, color="red", symbol="circle"),  # Marker properties
)

# Add trace to the figure
fig.add_trace(trace)

# Display the plot
fig.show()
'''

# Load the court diagram image
court_img_path = '../court.png'  # Replace with your actual image path
court_img = mpimg.imread(court_img_path)

# Get image dimensions
image_width, image_height = court_img.shape[:2]

# Sample data point (replace with your actual data)
data_point = {
    "id": 33253,
    "playerName": "LeBron James",
    "top": 93,
    "left": 95,
    "result": False,  # Change to False for red marker
    "distance": 15
}

# Normalize data points
normalized_top = data_point["top"] / image_height
normalized_left = data_point["left"] / image_width


# Create the plot figure
fig, ax = plt.subplots(figsize=(image_width/100, image_height/100))  # Adjust figsize for clarity

# Turn off axis visibility
ax.axis('off')

# Display the court image
ax.imshow(court_img, aspect='auto', extent=(0, image_width, 0, image_height))  # Set extent for correct placement

# Set marker color based on result
marker_color = 'green' if data_point["result"] else 'red'

# Plot the data point
point = ax.scatter(normalized_left * image_width, normalized_top * image_height, s=50, c=marker_color, marker='o')  # Adjust marker size and color

# Display the plot
plt.show()
