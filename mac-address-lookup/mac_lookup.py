import requests

print("=== MAC Address Lookup Tool ===")

mac = input("Enter MAC Address (example: 44:38:39:ff:ef:57): ")

url = f"https://api.macvendors.com/{mac}"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("\nVendor Information")
        print("------------------------")
        print("MAC Address :", mac)
        print("Vendor      :", response.text)
    else:
        print("Vendor not found or invalid MAC address.")

except requests.exceptions.RequestException as e:
    print("Error:", e)