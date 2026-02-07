"""
araclarin takibi: yolo kullanımı, training yapmayalım zaten yolo default olarak tanımlıyor.

"""

from ultralytics import YOLO # ultralytics kütüphanesi, yolo modellerini kullanmak için gerekli
import cv2 # görüntü işleme kütüphanesi

# veri seti yükleme

# yolo modeli yükleme

model = YOLO('yolov8n.pt') # yolo modelini yükleme, burada 'yolov8n.pt' modeli kullanılıyor

# video giriş kaynağı

video_path = 'f1.MOV' # video dosyasının yolu

cap = cv2.VideoCapture(video_path) # video dosyasını açma

# çıkış video ayarı

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # video genişliği
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # video yüksekliği

fps = cap.get(cv2.CAP_PROP_FPS) # video fps değeri

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height)) # çıkış video dosyasını oluşturma

while cap.isOpened(): # video dosyası açık olduğu sürece
    success, frame = cap.read() # video karesini okuma
    if not success: # eğer kare okunamazsa döngüyü kır
        break
    # yolo modelini kullanarak araçları tespit etme
    results = model.track(
        frame, # giriş görüntüsü
         conf=0.3, # tespit güven eşiği 0.3 altında olan nesneleri görmezden gelme  1 en yüksek güven, 0 en düşük güven
         iou=0.5, # tespit edilen nesnelerin birbirleriyle ne kadar örtüşebileceği (Intersection over Union) eşiği, bu ikisini tek bir nesne gibi kabul etmek için kullanılır, 0.5 genellikle iyi bir başlangıç noktasıdır
        persist=True, # tespit edilen nesnelerin takibini sürdürme
        tracker='bytetrack.yaml' # takip algoritması konfigürasyonu, ByteTrack algoritması kullanılıyor

# eğer burada class koysaydık (örnek class=2 ) sadece class 2 olan nesneleri takip ederdi.

                          ) # yolo modelini kullanarak karedeki nesneleri tespit etme
    
    # kutuları ve id leri ekran üzeirne çizme
    annotadet_frame = results[0].plot() # tespit edilen nesnelerin kutularını ve id'lerini çizme

    # göster ve kayıt et
    cv2.imshow('frame', annotadet_frame) # tespit edilen nesnelerin çizildiği kareyi gösterme
    out.write(annotadet_frame) # tespit edilen nesnelerin çizildiği kareyi çıkış video dosyasına yazma

    if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' tuşuna basıldığında döngüyü kır
        break

cap.release() # video dosyasını serbest bırakma
out.release() # çıkış video dosyasını serbest bırakma
cv2.destroyAllWindows() # tüm OpenCV pencerelerini kapatma
     





