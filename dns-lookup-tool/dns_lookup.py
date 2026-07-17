import socket

print("=== DNS Lookup Tool ===")

domain = input("Enter a domain name (e.g., google.com): ")

try:
    ip_address = socket.gethostbyname(domain)
    print(f"\nDomain: {domain}")
    print(f"IP Address: {ip_address}")
except socket.gaierror:
    print("Invalid domain or unable to resolve the address.")