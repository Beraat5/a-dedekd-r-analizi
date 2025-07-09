import sqlite3
from datetime import datetime, timedelta

def generate_daily_report():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()

    # Dün ve bugün tarihleri
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    # Veritabanından dünün kayıtlarını çek
    c.execute("""
        SELECT src_ip, COUNT(*) as count, MIN(timestamp), MAX(timestamp)
        FROM suspicious_traffic
        WHERE DATE(timestamp) = ?
        GROUP BY src_ip
    """, (yesterday.isoformat(),))

    rows = c.fetchall()

    report_lines = []
    report_lines.append(f"Günlük Şüpheli Trafik Raporu - {yesterday}\n")
    report_lines.append(f"Toplam farklı şüpheli IP sayısı: {len(rows)}\n")

    for row in rows:
        src_ip, count, first_seen, last_seen = row
        report_lines.append(f"- IP: {src_ip}, Olay Sayısı: {count}, İlk Görülme: {first_seen}, Son Görülme: {last_seen}")

    report_text = "\n".join(report_lines)

    # Raporu dosyaya yaz
    with open(f"daily_report_{yesterday}.txt", "w") as f:
        f.write(report_text)

    print(f"Rapor oluşturuldu: daily_report_{yesterday}.txt")

    conn.close()

if __name__ == "__main__":
    generate_daily_report()
