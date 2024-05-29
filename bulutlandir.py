import cv2
import numpy as np
from label_copier import label_copier
from datetime import datetime

def bulutlandir(image,cikti_path,label_path):
    # Bulutlu hava efekti için parlaklık ve kontrastı ayarlayın
    alpha = 0.8  # Kontrast kontrolü (0.0-1.0 arası)
    beta = -20  # Parlaklık kontrolü (-100 ile 100 arası)
    cloudy_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    # Hafif mavi tonları eklemek için
    blue_overlay = np.full(image.shape, (255, 255, 230), dtype='uint8')  # Daha hafif bir mavi renk
    cloudy_image = cv2.addWeighted(cloudy_image, 0.85, blue_overlay, 0.15, 0)

    # Hafif bir bulanıklık uygulayın
    cloudy_image = cv2.GaussianBlur(cloudy_image, (7, 7), 0)
    output_path = f"{cikti_path}\\{datetime.now().strftime('%H_%M_%S_%f')}_bulut.jpg"
    label_copier(label_path,output_path)
    cv2.imwrite(output_path, cloudy_image)
    # İşlenmiş resmi kaydet
    
# Kullanım örneği

