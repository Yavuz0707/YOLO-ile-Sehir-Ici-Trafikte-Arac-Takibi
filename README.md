# 🚗 YOLO Araç Takip Sistemi

Bu proje, YOLO (You Only Look Once) modelini kullanarak videolardaki araçları gerçek zamanlı tespit etme ve takip etme sistemidir. Ultralytics YOLO v8 modeli ve ByteTrack algoritması ile geliştirilmiştir.

## ✨ Özellikler

- **Gerçek Zamanlı Araç Tespiti**: YOLO v8n modeli ile yüksek performanslı nesne tespiti
- **Akıllı Takip Sistemi**: ByteTrack algoritması ile tutarlı araç takibi
- **Video İşleme**: Video dosyalarından araç tespiti ve işleme
- **Görsel Çıktı**: Tespit edilen araçları kutular ve ID'ler ile işaretleme
- **Video Kaydetme**: İşlenmiş videoyu otomatik kaydetme

## 🎯 Nasıl Çalışır

1. **Video Girişi**: Sistem belirtilen video dosyasını okur
2. **YOLO Tespiti**: Her karede araçları %30 güven eşiği ile tespit eder
3. **ByteTrack Takibi**: Tespit edilen araçlara benzersiz ID'ler atar ve takip eder
4. **Görselleştirme**: Araçları kutular ve ID numaraları ile işaretler
5. **Kaydetme**: İşlenmiş videoyu çıktı dosyası olarak kaydeder

## 📋 Gereksinimler

```bash
pip install -r requirements.txt
```

### Ana Bağımlılıklar:
- `ultralytics==8.4.12` - YOLO modeli için
- `opencv-python==4.13.0.92` - Video işleme için
- `torch==2.10.0` - Derin öğrenme framework'ü
- `numpy==2.4.2` - Sayısal hesaplamalar için

## 🚀 Kurulum

1. **Repositoryyi klonlayın**:
   ```bash
   git clone https://github.com/your-username/yolo-vehicle-tracking.git
   cd yolo-vehicle-tracking
   ```

2. **Gerekli paketleri yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

3. **YOLO modelini indirin**:
   - `yolov8n.pt` dosyası zaten proje içinde bulunmaktadır

## 🎮 Kullanım

1. **Video dosyanızı hazırlayın**:
   - Video dosyanızı proje klasörüne koyun
   - `main.py` dosyasındaki `video_path` değişkenini güncelleyin

2. **Programı çalıştırın**:
   ```bash
   python main.py
   ```

3. **Sonuçları görün**:
   - Gerçek zamanlı tespit penceresi açılacak
   - `output.avi` dosyası olarak işlenmiş video kaydedilecek
   - `q` tuşu ile programı sonlandırabilirsiniz

## ⚙️ Parametreler

```python
# Güven eşiği (0.0 - 1.0)
conf = 0.3  # %30 güven eşiği

# IoU eşiği (Intersection over Union)
iou = 0.5   # %50 örtüşme eşiği

# Takip algoritması
tracker = 'bytetrack.yaml'
```

### Parametre Açıklamaları:

- **conf**: Tespit güven eşiği. Yüksek değerler daha az ama kesin tespitler verir
- **iou**: Örtüşme eşiği. Aynı nesnenin birden fazla kez tespit edilmesini önler
- **persist**: Nesnelerin takibini frameler arasında sürdürür
- **tracker**: ByteTrack algoritması konfigürasyonu

## 📊 Model Bilgileri

- **Model**: YOLOv8n (nano versiyonu)
- **Boyut**: Hızlı işleme için optimize edilmiş
- **Sınıflar**: COCO veri setindeki 80 sınıf (araçlar dahil)
- **Desteklenen Nesneler**: Araba, kamyon, motosiklet, bisiklet, otobüs vb.

## 🎯 Performans İpuçları

- **Video Kalitesi**: Yüksek çözünürlüklü videolar daha iyi sonuç verir
- **Işık Koşulları**: İyi aydınlatma conditions sonuçları iyileştirir
- **Kamera Açısı**: Araçların net görünebileceği açılar tercih edilmelidir
- **Hareket**: Aşırı hızlı kamera hareketlerinden kaçının

## 🛠️ Geliştirme

### Farklı Modeller Deneme:
```python
model = YOLO('yolov8s.pt')  # Small (daha yavaş ama daha doğru)
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large (en doğru ama en yavaş)
```

### Sadece Belirli Sınıfları Takip Etme:
```python
results = model.track(frame, classes=[2, 3, 5, 7])  # Sadece araç sınıfları
```

## 🐛 Sorun Giderme

### Yaygın Problemler:

1. **CUDA Hatası**: GPU kullanımı için PyTorch CUDA versiyonunu yükleyin
2. **Model Yüklenmeme**: İnternet bağlantınızı kontrol edin, model otomatik indirilecek
3. **Video Açılmama**: Video dosya yolunu ve formatını kontrol edin
4. **Düşük FPS**: Daha hafif model (yolov8n) kullanın veya video çözünürlüğünü düşürün

## 📈 Gelecek Geliştirmeler

- [ ] Gerçek zamanlı web kamerası desteği
- [ ] Çoklu video dosyası işleme
- [ ] Araç sayma ve istatistikler
- [ ] GUI arayüzü
- [ ] REST API desteği
- [ ] Docker containerization

## 🤝 Katkı

Bu proje eğitim amaçlı geliştirilmiştir. Geliştirmeler ve öneriler için:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'i push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📸 Ekran Görüntüleri

*Proje çalıştırıldığında araçlar renkli kutular içinde ID numaralarıyla birlikte gösterilir.*

## 🔗 Kaynaklar

- [Ultralytics YOLO Dokümantasyonu](https://docs.ultralytics.com/)
- [ByteTrack Algoritması](https://github.com/ifzhang/ByteTrack)
- [OpenCV Dokümantasyonu](https://docs.opencv.org/)

## ⭐ Bu Projeyi Beğendiyseniz

Bu projeyi yararlı bulduysanız yıldız vermeyi unutmayın! ⭐

---

*Bu proje BTK Görüntü İşleme kursu kapsamında eğitim amaçlı geliştirilmiştir.*