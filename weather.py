import requests

filename = 'apikey'

def getFileContents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

def kelvinToFahrenheit(kelvin):
    return kelvin * 1.8 - 459.67

API_KEY = getFileContents(filename)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requestUrl = f"{BASE_URL}?appid={API_KEY}&q={city}"
print(requestUrl)
response = requests.get(requestUrl)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(kelvinToFahrenheit(data['main']['temp']), 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "Fahrenheit")
else:
    print("An error occurred.")
