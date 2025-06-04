from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Sniffer çalışıyor...")
sniff(prn=packet_callback, count=10)
from scapy.all import sniff, TCP

def packet_callback(packet):
    if TCP in packet:
        log = packet.summary()
        print(log)
        with open("suspicious.log", "a") as f:
            f.write(log + "\n")

print("Sniffer çalışıyor, TCP paketlerini yakalıyor...")
sniff(prn=packet_callback)
