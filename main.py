import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours were you at the gym for today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_updation_endpoint = f"{pixel_creation_endpoint}/20241209"

pixel_updation_data = {
    "quantity": "1.5"
}
# response = requests.put(url=pixel_updation_endpoint, json=pixel_updation_data, headers=headers)
# print(response.text)

pixel_deletion_endpoint = f"{pixel_creation_endpoint}/20241209"

# response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# print(response.text)
