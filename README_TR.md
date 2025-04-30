# Kütüphane Nesne Tespit Sistemi

## Açıklama
Bu proje, video görüntülerinde insanları, kitapları, masaları ve sandalyeleri tespit etmek ve izlemek için YOLOv8 kullanan gerçek zamanlı bir nesne tespit sistemi uygulamaktadır. Sistem, tespit edilen nesnelerin etrafına renkli dikdörtgenler çizer ve kişi sayacı gösterir.

## Özellikler
- Gerçek zamanlı nesne tespiti
- Çoklu nesne sınıfı tespiti:
  - İnsan (Yeşil dikdörtgen)
  - Kitap (Mavi dikdörtgen)
  - Masa (Kırmızı dikdörtgen)
  - Sandalye (Turkuaz dikdörtgen)
- Sağ alt köşede kişi sayacı
- Canlı video işleme

## Gereksinimler
- Python 3.8 veya üstü
- Gerekli paketler için requirements.txt dosyasına bakınız

## Kurulum
1. Depoyu klonlayın
2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım
1. Video yolunu betik içinde güncelleyin
2. Betiği çalıştırın:
```bash
python "Proje Bitirme.py"
```
3. Çıkmak için 'q' tuşuna basın

## Notlar
- Gerçek zamanlı işleme için yeterli GPU/CPU kaynaklarına sahip olduğunuzdan emin olun
- YOLO model dosyası (yolov8n.pt) ilk çalıştırmada otomatik olarak indirilecektir 