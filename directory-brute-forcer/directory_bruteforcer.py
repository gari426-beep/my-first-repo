import requests

print("=== Directory Brute Forcer ===")

url = input("Enter website URL (example: https://example.com): ")

with open("wordlist.txt", "r") as file:
    directories = file.readlines()

print("\nScanning...\n")

for directory in directories:
    directory = directory.strip()
    target = f"{url}/{directory}"

    try:
        response = requests.get(target, timeout=5)
        print(f"Scanning: {target} - Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"[FOUND] {target}")

        elif response.status_code == 403:
            print(f"[FORBIDDEN] {target}")

    except requests.exceptions.RequestException:
        pass

print("\nScan Completed.")