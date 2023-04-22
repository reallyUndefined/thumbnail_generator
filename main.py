import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Create thumbnails for images in a folder')
parser.add_argument('-i', '--input', required=True, help='path to input image or folder')
parser.add_argument('-o', '--output', default='./output', help='path to output folder (default: output)')
parser.add_argument('-s', '--size', default=256, type=int, help='size of the thumbnails (default: 256)')
args = parser.parse_args()

input_path = args.input
output_folder = args.output
thumbnail_size = (args.size, args.size)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_thumbnail(fn):
    if fn.endswith(".jpg") or fn.endswith(".png"):
        image = Image.open(os.path.join(input_path, fn))
        image.thumbnail(thumbnail_size, Image.LANCZOS)
        thumbnail_path = os.path.join(output_folder,'thumbnail-' + fn)
        image.save(thumbnail_path)

if os.path.isfile(input_path):
    filename = os.path.basename(input_path)
    generate_thumbnail(fn=filename)
else:
    for filename in os.listdir(input_path):
        generate_thumbnail(fn=filename)