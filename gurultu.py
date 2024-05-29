import cv2
import numpy as np
from label_copier import label_copier
from datetime import datetime

def gurultu(image, cikti_path,label_path):
   
    if image is None:
        raise ValueError("Image not found or unable to load.")
    
    row, col, ch = image.shape
    mean = 0.65

    
    sigma = 0.60

    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype('uint8')
    # Add the Gaussian noise to the image
    noisy_image = cv2.add(image, gauss)
    # Clip the values to be in the valid range and convert to uint8
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # Save the noisy mage
    output_path = f"{cikti_path}\\{datetime.now().strftime('%H_%M_%S_%f')}_noise.jpg"
    label_copier(label_path,output_path)
    cv2.imwrite(output_path, noisy_image)

