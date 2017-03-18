#!/usr/bin/env bash

#Script that takes photo from Raspberry Pi Camera and runs image recognition on the image. The resulting classifications are stored in IMAGE_CLASS.txt

#Assumes that takePicture.py and ./image_recog are in the SAME directory

python takePicture.py

./image_recog_pi /home/pi/image.jpg

