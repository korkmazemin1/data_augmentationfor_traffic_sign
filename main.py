import cv2
import numpy as np
from parlaklik_arttir import parlaklik_arttir
from bulutlandir import bulutlandir
from blurlandir import blurlandir
from gurultu import gurultu
import glob
import argparse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Setting up argument parser
parser = argparse.ArgumentParser(description='Process a txt file path.')
parser.add_argument('--txt_file_path', type=str, help='The path to the txt file')
parser.add_argument('--output_path', type=str, help='The path to the txt file')
args = parser.parse_args()

# Your code that uses txt_file_path
txt_file_path = args.txt_file_path
cikti_path=args.output_path
# Read the .txt file and add each line to a list
with open(txt_file_path, 'r') as infile:
    paths = infile.readlines()

# Clean unnecessary spaces (e.g., '\n') at the end of the lines
paths = [path.strip() for path in paths]


def process_image(path):
    label_path = path
    path = path.replace(".txt", ".jpg")
    
    image = cv2.imread(path)
    blurlandir(image, 15, cikti_path, label_path)
    bulutlandir(image, cikti_path, label_path)
    parlaklik_arttir(image, cikti_path, label_path)
    gurultu(image, cikti_path, label_path)

# Process each path with a progress bar for all paths
with ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(process_image, paths), desc="Processing Images", total=len(paths)))
