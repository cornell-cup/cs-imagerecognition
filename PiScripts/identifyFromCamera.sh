#!/usr/bin/env bash

#Script that takes photo from Raspberry Pi Camera and runs image recognition on the image. The resulting classifications are stored in IMAGE_CLASS.txt

#Assumes that takePicture.py and ./image_recog are in the SAME directory
#Also assumes that takePicture.py stores the image in the same directory

echo "Capuring image..."
python takePicture.py
echo "Identifying image..."
path="$(pwd)/image.jpg"
./image_recog_pi $path

rm image.jpg
