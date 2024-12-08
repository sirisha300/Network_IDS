from scapy.all import rdpcap
import pandas as pd

def pcap_to_csv(pcap_file, csv_file):
    packets = rdpcap(pcap_file)
    rows = []
    
    for packet in packets:
        if packet.haslayer('IP'):
            ip_layer = packet.getlayer('IP')
            row = {
                "time": packet.time,
                "src": ip_layer.src if hasattr(ip_layer, 'src') else None,
                "dst": ip_layer.dst if hasattr(ip_layer, 'dst') else None,
                "proto": packet.proto if hasattr(packet, 'proto') else None,
                "length": len(packet)
            }
            rows.append(row)
    
    df = pd.DataFrame(rows)
    df.to_csv(csv_file, index=False)

# Provide the path to your .pcap file using forward slashes
pcap_file_path = 'C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/sample.pcap'
csv_file_path = 'C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/capture.csv'

# Convert captured pcap file to csv
pcap_to_csv(pcap_file_path, csv_file_path)
