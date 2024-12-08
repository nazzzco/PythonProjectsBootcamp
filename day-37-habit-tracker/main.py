import requests
from datetime import datetime


USERNAME = "nazzzco"
TOKEN = "asiuhdiuasjdpokh2231"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=params, verify=False)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Training Graph",
    "unit": "times",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
#(response.text)

#today=datetime.now()
today = datetime(year=2024, month=10, day=23)
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers, verify=False)
#print(response.text)