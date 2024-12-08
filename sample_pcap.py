from scapy.all import *

# Create a few example packets
packet1 = IP(src="192.168.1.1", dst="192.168.1.2")/TCP(dport=80)/"GET / HTTP/1.1\r\n\r\n"
packet2 = IP(src="192.168.1.2", dst="192.168.1.1")/TCP(sport=80)/"HTTP/1.1 200 OK\r\n\r\n"
packet3 = IP(src="10.0.0.1", dst="10.0.0.2")/ICMP()

# List of packets
packets = [packet1, packet2, packet3]

# Save packets to a .pcap file
wrpcap("sample.pcap", packets)

print("Sample pcap file 'sample.pcap' created.")
