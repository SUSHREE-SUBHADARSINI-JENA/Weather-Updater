import request
import json
import os
if __name__ == '__main__':
    pass
city = input("Enter the name of city\n")
url = "https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q=kolkata"
r = request.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
os.system(f"say ' The current weather in {city} is {w} degrees'")
