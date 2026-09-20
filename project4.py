# pip install requests
import requests

API_KEY = "YOUR_API_KEY" 
city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print(f"City: {data['name']}")
    print(f"Temp: {data['main']['temp']} C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("City Not Found")

#5. Live Cryptocurrency Prices
 # pip install requests
import requests

coin = input("Enter coin (bitcoin, ethereum, dogecoin): ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr,usd"
response = requests.get(url)
data = response.json()

if coin in data:
    print(f"{coin.upper()} Price:")
    print(f"INR: {data[coin]['inr']}")
    print(f"USD: {data[coin]['usd']}")
else:
    print("Coin not found")