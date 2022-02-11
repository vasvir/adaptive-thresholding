#!/usr/bin/python3

import sys
import os
import tempfile
import cv2
import time

def process_image(input, tmpdir):
    print("Processing image " + input, file = sys.stderr)
    img = cv2.imread(input, 0)
    img = cv2.medianBlur(img, 5)
    th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(os.path.join(tmpdir.name, os.path.basename(input)), th)

#input_dir = state = "nice" if is_nice else "not nice"
input_dir = sys.argv[1] if len(sys.argv) >= 2 else None

if input_dir is None:
    print("No input directory specified", file = sys.stderr);
    sys.exit(0);

if not os.path.isdir(input_dir):
    print("Input directory does not exist: " + input_dir, file = sys.stderr);
    sys.exit(1);

print("Processing input_dir: " + input_dir, file = sys.stderr)

files = [y for y in (os.path.join(input_dir, x) for x in os.listdir(input_dir))]
images = sorted(filter(lambda file: os.path.isfile(file) and (file.lower().endswith(".png") or file.lower().endswith(".jpg") or file.lower().endswith(".jpeg")), files), key=os.path.getmtime)

if not images:
    print("Specified directory has no images", file = sys.stderr)
    sys.exit(2);

tmpdir=tempfile.TemporaryDirectory(suffix="adth", prefix="adth")

#print(tmpdir)

for image in images:
    process_image(image, tmpdir)

pdffile = tmpdir.name + ".pdf"

print("Creating PDF file " + pdffile, file = sys.stderr);
os.system("convert " + tmpdir.name + "/* " + pdffile)

print("Executing system PDF handler", file = sys.stderr)
os.system("xdg-open " + pdffile)
time.sleep(5)

print("Removing PDF file " + pdffile, file = sys.stderr);
os.remove(pdffile)
