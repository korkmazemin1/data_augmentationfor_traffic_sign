
# 🚀 Advanced Image Processing Toolkit

This repository provides a powerful Python script for batch-processing images with various transformations like blurring, clouding, brightness enhancement, and noise addition. It efficiently reads a list of image paths from a text file and applies augmentations in parallel using multithreading to accelerate the workflow.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/0*u1vqIq2_vupUkGzK.jpeg" alt="Image Processing Showcase" width="700"/>
</p>

---

## ✨ Features

-   **Multiple Transformations**: Apply blur, cloud effects, brightness adjustments, and noise to your images.
-   **Parallel Processing**: Leverages `ThreadPoolExecutor` for high-speed, concurrent image processing.
-   **Batch Operations**: Easily process thousands of images by providing a simple text file with their paths.
-   **Progress Tracking**: A clean `tqdm` progress bar keeps you updated on the script's progress.
-   **Command-Line Interface**: Simple and clear CLI for specifying input and output directories.

---

## 📋 Requirements

-   Python 3.x
-   OpenCV (`opencv-python`)
-   NumPy
-   tqdm

---

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/your-repository.git](https://github.com/yourusername/your-repository.git)
    cd your-repository
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt` file, you can run: `pip install opencv-python numpy tqdm`)*

3.  **Ensure your modules are available:**
    Make sure your transformation modules (`parlaklik_arttir`, `bulutlandir`, `blurlandir`, and `gurultu`) are in the same directory or accessible within your Python environment.

---

## 🚀 Usage

Run the script from your terminal using the following command structure.

```bash
python process_images.py --txt_file_path <path_to_your_list.txt> --output_path <path_to_output_directory>
````

### Example

This command will read image paths from `images_list.txt` and save the processed images into the `processed_images` directory.

```bash
python process_images.py --txt_file_path images_list.txt --output_path processed_images
```

-----

## 🔧 How It Works

#### 1\. Argument Parsing

The script uses `argparse` to handle the command-line arguments for the input file path and the output directory.

```python
import argparse

parser = argparse.ArgumentParser(description='Process a list of images from a text file.')
parser.add_argument('--txt_file_path', type=str, required=True, help='Path to the .txt file containing image paths')
parser.add_argument('--output_path', type=str, required=True, help='Path to the directory to save processed images')
args = parser.parse_args()
```

#### 2\. Reading Image Paths

It opens the `.txt` file specified and reads all image paths line by line.

```python
with open(args.txt_file_path, 'r') as infile:
    paths = [line.strip() for line in infile.readlines()]
```

#### 3\. Image Processing Function

The core `process_image` function reads each image and applies the series of imported transformation functions.

```python
def process_image(path):
    label_path = path  # Assuming .txt label path
    image_path = path.replace(".txt", ".jpg") # Convert to image path
   
    image = cv2.imread(image_path)
    if image is None:
        return # Skip if image not found

    # Apply transformations
    blurlandir(image, 15, cikti_path, label_path)
    bulutlandir(image, cikti_path, label_path)
    parlaklik_arttir(image, cikti_path, label_path)
    gurultu(image, cikti_path, label_path)
```

#### 4\. Parallel Processing

`ThreadPoolExecutor` is used to map the `process_image` function across all paths, processing them concurrently for maximum efficiency. `tqdm` provides a user-friendly progress bar.

```python
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

with ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(process_image, paths), total=len(paths), desc="Processing Images"))
```

-----

## 🎨 Transformation Functions

Ensure the following functions are correctly defined in their respective modules. Each function should handle the image processing logic and save the output.

  - `parlaklik_arttir`: Increases the brightness of the image.
  - `bulutlandir`: Applies a synthetic cloud effect.
  - `blurlandir`: Applies a blur effect (e.g., Gaussian blur).
  - `gurultu`: Adds noise (e.g., salt-and-pepper or Gaussian noise) to the image.

<!-- end list -->

```
```
