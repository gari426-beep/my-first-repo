import socket
import time

print("=" * 40)
print("        Simple Port Scanner")
print("=" * 40)

host = input("Enter IP address (e.g. 192.168.1.1): ")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

try:
    socket.inet_aton(host)
except socket.error:
    print("Invalid IP address!")
    exit()

print(f"\nScanning {host}...\n")

start = time.time()

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    try:
        service = socket.getservbyport(port)
    except:
        service = "Unknown"

    if result == 0:
        print(f"[OPEN ] Port {port:<5} ({service})")
    else:
        print(f"[CLOSED] Port {port:<5} ({service})")

    sock.close()

end = time.time()

print("\nScan completed.")
print(f"Time taken: {end - start:.2f} seconds")