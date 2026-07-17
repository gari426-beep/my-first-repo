import socket

print("=== Network Scanner ===")

host = input("Enter a hostname or IP address: ")

try:
    ip = socket.gethostbyname(host)

    print("\nHost Information")
    print("----------------")
    print("Hostname :", host)
    print("IP Address:", ip)

except socket.gaierror:
    print("Invalid hostname or IP address.")