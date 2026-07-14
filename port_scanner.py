import socket

print(" ===Simple Port Scanner===")

host = input("Enter IP address (example: 192.168.1.1): ")

ports =[21,22,23,25,53,80,110,143,443,445,3389]

print("Scanning ports on host:", host)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

print("Port scanning completed!!")