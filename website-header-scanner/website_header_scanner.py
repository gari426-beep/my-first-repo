import requests

print("=== Website Header Scanner ===")

url = input("Enter website URL (include https://): ")

try:
    response = requests.get(url)

    print("\nResponse Headers")
    print("----------------------------")

    for key, value in response.headers.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException:
    print("Unable to connect to the website.")