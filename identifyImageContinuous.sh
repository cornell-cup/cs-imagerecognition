#!usr/bin/env bash

#Script that runs image recognition on a given image

source activate tensorflow

while [ true ]
do
	cd "C:\Users\CornellCup\Documents\image-recog\cs-object-identification"
	python "PiScripts\receiveImage.py"
	cd "C:\Users\CornellCup\models\tutorials\image\imagenet"
	python classify_image.py --image_file="C:\Users\CornellCup\Documents\image-recog\cs-object-identification\image.jpeg" 2>"C:\Users\CornellCup\Documents\image-recog\cs-object-identification\image_recog.log" 1>"C:\Users\CornellCup\Documents\image-recog\cs-object-identification\image_class.txt"
	
done

source deactivate tensorflow

exit 0
