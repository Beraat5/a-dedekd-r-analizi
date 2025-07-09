# 🛡️ Ağ Güvenliği Analizi: Port Taraması ve Şüpheli Trafik Tespiti

---

## 👤 Hazırlayan
**Adı Soyadı:** Berat Uysal  
**Bölüm:** Bilişim Güvenliği Teknolojisi  
**Sınıf:** 2. Sınıf  

---

## 🎯 Projenin Amacı
Bu projenin amacı, bir ağda gerçekleşen **port tarama saldırılarını** ve şüpheli trafik hareketlerini **gerçek zamanlı olarak tespit** eden, bu bilgileri loglayan ve gerektiğinde alarm üreten bir sistem geliştirmektir.

---

## 📌 Projenin Kapsamı
Proje, yerel bir ağda çalışan bir sniffer aracılığıyla şu işlemleri gerçekleştirir:
- TCP/UDP trafiğini analiz eder,
- Kara listede yer alan IP’leri tespit eder,
- Port tarama gibi şüpheli davranışları algılar,
- Logları veritabanına kaydeder,
- E-posta yoluyla uyarı gönderir.

---

## ⚙️ Kullanılan Teknolojiler
- **Python 3.x**
- **Scapy** (ağ trafiği analiz aracı)
- **SQLite** (yerel veritabanı)
- **Wireshark** (test ve analiz aracı)
- **Kali Linux** (geliştirme ortamı)
- **SMTP** (e-posta gönderimi)

---

## 🧱 Proje Mimarisi

    +---------------------+
    |   Sniffer (scapy)   |
    +----------+----------+
               |
    +----------v----------+
    |  Trafik Analizi     |
    | - Port Scan Tespiti |
    | - Kara Liste Kontrol|
    +----------+----------+
               |
    +----------v----------+
    |  Loglama ve Alarm   |
    | - SQLite Log        |
    | - Email Alert       |
    +---------------------+

---

## 🔍 Gerçekleştirilen Modüller

### 1. sniffer.py
- Ağ trafiğini dinler ve TCP/UDP paketleri analiz eder.
- Port taraması tespit algoritması içerir.

### 2. Kara Liste Kontrolü
- `blacklist.txt` içinde tanımlı IP adreslerinden gelen paketler işaretlenir ve loglanır.

### 3. Veritabanı Sistemi
- `logs.db` dosyasında `suspicious_traffic` tablosuna şüpheli hareketler kaydedilir.

### 4. E-posta Uyarı Sistemi
- `email_alert.py` modülü ile belirlenen adreslere olay bildirimi gönderilir.

---

## 🧪 Test Senaryoları

- **Senaryo 1:** Nmap ile hedef IP’ye SYN tarama yapıldı. Sistem 5 saniyede 15 farklı porta erişimi tespit etti ve bunu port tarama olarak işaretledi.
- **Senaryo 2:** Kara listede olan `192.168.1.100` IP’sinden gelen trafik tespit edildi ve alarm gönderildi.

---

## 📸 Ekran Görüntüleri

_(Buraya terminal çıktılarının ekran görüntülerini veya veritabanı/log dosyalarının içeriklerini .png olarak ekleyeceksin)_

---

## 📚 Sonuç ve Değerlendirme

Bu proje sayesinde ağ üzerinde yapılan temel keşif saldırıları tespit edilerek, sistem yöneticisine erken uyarılar sunulmuştur. Gerçek zamanlı analiz yapılması ve e-posta bildirimi gibi özelliklerle sistem proaktif savunma yaklaşımı sergilemektedir.  
Gelecek çalışmalarda, görsel arayüz ve dışa aktarılabilir log raporları gibi eklemeler yapılabilir.

---

## 🔗 Kaynakça

- https://scapy.net/  
- https://www.nmap.org/  
- https://docs.python.org/  
- https://www.kali.org/  
- Kendi geliştirdiğim test senaryoları ve kodlar
