import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)
data = response.json()

current_weather = data["current_condition"][0]

temperature = current_weather["temp_C"]
condition = current_weather["weatherDesc"][0]["value"]

print("==============================")
print("      DEHRADUN WEATHER")
print("==============================")
print("City        : Dehradun")
print("Temperature :", temperature, "°C")
print("Condition   :", condition)
print("==============================")


numbers = [10, 15, 20, 25, 30]
total = 0

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        print("Even number:", numbers[i])
        total += numbers[i]
    else:
        print("Odd number:", numbers[i])

print("Total of even numbers:", total)

count = 0
while count < len(numbers):
    if numbers[count] > 20:
        print("Large:", numbers[count])
    count = count + 2

for num in numbers:
    print("Square:", num ** 2)
