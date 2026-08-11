import requests
url = "https://wttr.in/Dehradun?format=j1"
response = requests.get(url)

print("Status code:", response.status_code)

weather_data = response.json()
# print("Weather data:", weather_data)
# or print(response.json())

current_weather = weather_data["current_condition"][0]
temperature = current_weather["temp_C"]
condition = current_weather["weatherDesc"][0]["value"]

print("\n--- Dehradun Weather ---")
print("City:", "Dehradun")
print("Temperature:", temperature, "°C")
print("Condition:", condition)