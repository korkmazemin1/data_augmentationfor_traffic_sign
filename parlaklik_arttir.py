import cv2
import numpy as np
from label_copier import label_copier
from datetime import datetime

def parlaklik_arttir(image, cikti_path, label_path,gamma=7):
    if image is None:
        raise ValueError("Image not found or unable to load.")

    invGamma = 1.0 / gamma

    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    
    adjusted_image = cv2.LUT(image, table)

    output_path = f"{cikti_path}\\{datetime.now().strftime('%H_%M_%S_%f')}_parlaklik.jpg"
    label_copier(label_path,output_path)
    cv2.imwrite(output_path, adjusted_image)



