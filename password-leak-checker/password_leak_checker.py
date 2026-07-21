import hashlib
import requests

print("=== Password Leak Checker ===")

password = input("Enter your password: ")

sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

first5 = sha1_password[:5]
remaining = sha1_password[5:]

url = f"https://api.pwnedpasswords.com/range/{first5}"

try:
    response = requests.get(url)

    if response.status_code != 200:
        print("Error connecting to the API.")
        exit()

    hashes = response.text.splitlines()

    found = False

    for line in hashes:
        hash_suffix, count = line.split(":")

        if hash_suffix == remaining:
            print(f"\n⚠️ WARNING!")
            print(f"This password has appeared in data breaches {count} times.")
            found = True
            break

    if not found:
        print("\n✅ Good news!")
        print("This password was not found in the database.")

except requests.exceptions.RequestException as e:
    print("Error:", e)