#!usr/bin/env bash

#Script that runs image recognition on a given image

cd "C:\Users\CornellCup\models\tutorials\image\imagenet"

source activate tensorflow

if [ $# -ge 1 ]; then
	#python classify_image.py --image_file=$1 2>"C:\Users\CornellCup\Desktop\image_recog.log 1>"C:\Users\CornellCup\Desktop\IMAGE_CLASS.txt"
	time python classify_image.py --image_file=$1 2>"C:\Users\CornellCup\Documents\image-recog\image_recog.log" 1>"C:\Users\CornellCup\Documents\image-recog\IMAGE_CLASS.txt"
else
	#python classify_image.py 2>"C:\Users\CornellCup\Desktop\image_recog.log" 1>"C:\Users\CornellCup\Desktop\IMAGE_CLASS.txt"
	time python classify_image.py 2>"C:\Users\CornellCup\Documents\image-recog\image_recog.log" 1>"C:\Users\CornellCup\Documents\image-recog\IMAGE_CLASS.txt"

fi

source deactivate tensorflow

exit 0
