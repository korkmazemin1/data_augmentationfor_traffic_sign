import cv2
import numpy as np
from label_copier import label_copier
from datetime import datetime

def blurlandir(image, kernel_size,cikti_path,label_path):
    if image is None:
        raise ValueError("Görüntü dosyası bulunamadı!")
    # Gaussian Blur uygula
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    output_path = f"{cikti_path}\\{datetime.now().strftime('%H_%M_%S_%f')}_blur.jpg"
    label_copier(label_path,output_path)
    cv2.imwrite(output_path, blurred_image)
    return blurred_image 

