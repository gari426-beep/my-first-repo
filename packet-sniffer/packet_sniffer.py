from scapy.all import sniff

print("=== Packet Sniffer ===")
print("Capturing 10 packets...\n")

def process_packet(packet):
    print(packet.summary())

sniff(prn=process_packet, count=10)

print("\nCapture completed.")