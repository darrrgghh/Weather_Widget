import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"  # Изменено на lang=en
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']  
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"""Weather forecast: {city.capitalize()}:
- Conditions: {weather}
- Temperature: {temp}°C (feels like {feels_like}°C)
- Humidity: {humidity}%
- Wind speed: {wind_speed} m/s"""
    elif response.status_code == 404:
        return "Can't find the city. Check the spelling."
    else:
        return "Can't access weather info. Try again later."

API_KEY = "0b45a6c2ad5406c2ed122fe3981bd785"

# Request city
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"  # Изменено на lang=en

# Send request
response = requests.get(url)

# Output information
if response.status_code == 200:
    weather_report = get_weather(API_KEY, city)
    print("\n" + weather_report)
else:
    print(f"HTTP status: {response.status_code}")
    print(f"Response: {response.text}")
