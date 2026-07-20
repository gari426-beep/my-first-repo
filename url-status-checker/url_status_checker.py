import requests

print("=== URL Status Checker ===")

url = input("Enter website URL (include https://): ")

try:
    response = requests.get(url, timeout=5)

    print("\nWebsite Information")
    print("----------------------")
    print("URL:", url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Status: Website is reachable.")
    elif response.status_code == 404:
        print("Status: Page not found.")
    elif response.status_code == 403:
        print("Status: Access forbidden.")
    elif response.status_code == 500:
        print("Status: Internal server error.")
    else:
        print("Status: Received response from server.")

except requests.exceptions.RequestException as e:
    print("Error:", e)