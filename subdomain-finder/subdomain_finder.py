import socket

print("=== Subdomain Finder ===")

domain = input("Enter target domain (example: google.com): ")

print("\nSearching for subdomains...\n")

with open("subdomains.txt", "r") as file:
    for subdomain in file:
        subdomain = subdomain.strip()
        target = f"{subdomain}.{domain}"

        try:
            ip = socket.gethostbyname(target)
            print(f"[FOUND] {target} --> {ip}")

        except socket.gaierror:
            pass

print("\nScan Completed!")