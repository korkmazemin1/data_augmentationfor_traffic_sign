# Image Processing Script

This repository contains a Python script for processing images using various transformations like blurring, clouding, brightness enhancement, and noise addition. The script reads a list of image paths from a provided text file and applies these transformations in parallel using multithreading.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- tqdm

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python numpy tqdm
    ```

3. Make sure you have the `parlaklik_arttir`, `bulutlandir`, `blurlandir`, and `gurultu` modules in the same directory or installed in your Python environment.

## Usage

To run the script, use the following command in your terminal:

```sh
python process_images.py --txt_file_path <path_to_txt_file> --output_path <output_directory>
Replace <path_to_txt_file>
```
 with the path to your text file containing the list of image paths, and <output_directory> with the directory where you want to save the processed images.

Code Explanation
The script performs the following steps:

Setup Argument Parser:
The script uses argparse to handle command-line arguments for the input text file and the output directory.

```sh
import argparse

parser = argparse.ArgumentParser(description='Process a txt file path.')
parser.add_argument('--txt_file_path', type=str, help='The path to the txt file')
parser.add_argument('--output_path', type=str, help='The path to the output directory')
args = parser.parse_args()
```


Read Paths from Text File:
It reads the paths of the images from the provided text file.

```sh
txt_file_path = args.txt_file_path
cikti_path = args.output_path

with open(txt_file_path, 'r') as infile:
    paths = infile.readlines()

paths = [path.strip() for path in paths]
```

Image Processing Function:
A function process_image is defined to read and process each image. It calls the transformation functions imported from other modules.
```sh
def process_image(path):
    label_path = path
    path = path.replace(".txt", ".jpg")
    
    image = cv2.imread(path)
    blurlandir(image, 15, cikti_path, label_path)
    bulutlandir(image, cikti_path, label_path)
    parlaklik_arttir(image, cikti_path, label_path)
    gurultu(image, cikti_path, label_path)
```
Parallel Processing:
The script uses ThreadPoolExecutor to process images in parallel and displays a progress bar using tqdm.

```sh
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

with ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(process_image, paths), desc="Processing Images", total=len(paths)))
```

Transformation Functions
Ensure that the transformation functions (parlaklik_arttir, bulutlandir, blurlandir, and gurultu) are properly defined in their respective modules. Here's a brief explanation of what each function should do:

parlaklik_arttir: Increases the brightness of the image.
bulutlandir: Applies a clouding effect to the image.
blurlandir: Blurs the image.
gurultu: Adds noise to the image.
Make sure to place these functions in separate Python files or define them in the script as per your project structure.

Example
Here's an example command to run the script:

```sh
python process_images.py --txt_file_path images_list.txt --output_path processed_images
```
This command will read the image paths from images_list.txt and save the processed images to the processed_images directory.
