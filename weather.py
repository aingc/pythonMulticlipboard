import requests

filename = 'apikey'

def getFileContents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

API_KEY = getFileContents(filename)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requestUrl = f"{BASE_URL}?appid={API_KEY}&q={city}"
print(requestUrl)
response = requests.get(requestUrl)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred.")
