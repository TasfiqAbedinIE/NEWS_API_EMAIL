import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Laser_Towards_Milky_Ways_Centre.jpg/660px-Laser_Towards_Milky_Ways_Centre.jpg"

response = requests.get(url)

with open("astronomy.jpg", "wb") as file:
    file.write(response.content)