
from scapy.all import sniff, IP, Raw
import sqlite3
import re
from datetime import datetime

# Veritabanı bağlantısı
conn = sqlite3.connect("logs.db")
c = conn.cursor()

# Tabloyu oluştur (eğer yoksa)
c.execute("""
    CREATE TABLE IF NOT EXISTS suspicious_traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        src_ip TEXT,
        dst_ip TEXT,
        reason TEXT
    )
""")
conn.commit()

# Kara liste IP'leri oku
with open("blacklist.txt", "r") as f:
    blacklisted_ips = [line.strip() for line in f.readlines()]

# Regex desenleri
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
tc_kimlik_pattern = r"\b[1-9][0-9]{10}\b"

def log_to_db(src_ip, dst_ip, reason):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO suspicious_traffic (timestamp, src_ip, dst_ip, reason) VALUES (?, ?, ?, ?)",
              (timestamp, src_ip, dst_ip, reason))
    conn.commit()
    print(f"[!] Şüpheli trafik: {src_ip} -> {dst_ip} | Sebep: {reason}")

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Kara listedeki IP kontrolü
        if src_ip in blacklisted_ips or dst_ip in blacklisted_ips:
            log_to_db(src_ip, dst_ip, "Kara listedeki IP")

        # Veri sızıntısı kontrolü (Payload içinde TC ya da e-posta)
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors='ignore')
            if re.search(email_pattern, payload):
                log_to_db(src_ip, dst_ip, "E-posta adresi tespit edildi")
            if re.search(tc_kimlik_pattern, payload):
                log_to_db(src_ip, dst_ip, "TC kimlik numarası tespit edildi")

print("[*] Trafik dinleniyor... (CTRL+C ile durdur)")
sniff(prn=analyze_packet, store=False)
