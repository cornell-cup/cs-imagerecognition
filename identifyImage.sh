#!usr/bin/env bash

#Script that runs image recognition on a given image

source activate tensorflow

cd "C:\Users\CornellCup\Documents\image-recog\cs-object-identification"

python PiScripts\receiveImage.py

cd "C:\Users\CornellCup\models\tutorials\image\imagenet"

#python classify_image.py --image_file=$1 2>"C:\Users\CornellCup\Desktop\image_recog.log 1>"C:\Users\CornellCup\Desktop\IMAGE_CLASS.txt"
python classify_image.py --image_file="C:\Users\CornellCup\Documents\image-recog\cs-object-identification\image.jpeg" 2>"C:\Users\CornellCup\Documents\image-recog\image_recog.log" 1>"C:\Users\CornellCup\Documents\image-recog\IMAGE_CLASS.txt"

source deactivate tensorflow

exit 0
