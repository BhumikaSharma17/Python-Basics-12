import requests

url = "https://wttr.in/Dehradun?format=j1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Extract location information
    area = data["nearest_area"][0]
    city = area["areaName"][0]["value"]

    # Extract current weather
    current = data["current_condition"][0]
    temperature = current["temp_C"]
    condition = current["weatherDesc"][0]["value"]

    # Display weather information
    print("=" * 35)
    print("       DEHRADUN WEATHER")
    print("=" * 35)
    print(f"City        : {city}")
    print(f"Temperature : {temperature}°C")
    print(f"Condition   : {condition}")
    print("=" * 35)

except requests.exceptions.RequestException as error:
    print("Error connecting to weather API:", error)

except (KeyError, IndexError, ValueError) as error:
    print("Error processing weather data:", error)