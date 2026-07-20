import requests

print("=== IP Geolocation Tool ===")

ip = input("Enter an IP address (example: 8.8.8.8): ")

url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)

data = response.json()

if data["status"] == "success":
    print("\nIP Information")
    print("---------------------------")
    print("IP Address :", data["query"])
    print("Country    :", data["country"])
    print("Region     :", data["regionName"])
    print("City       :", data["city"])
    print("ISP        :", data["isp"])
    print("Latitude   :", data["lat"])
    print("Longitude  :", data["lon"])
    print("Timezone   :", data["timezone"])
else:
    print("Invalid IP Address!")