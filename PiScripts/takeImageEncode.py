import io
import time
import picamera
import R2Protocol
import socket
from PIL import Image

#Getting image
stream = io.BytesIO()
with picamera.PiCamera() as camera:
	camera.capture(stream, format='jpeg')
stream.seek(0)
image = stream.getvalue()

encoded = R2Protocol.encode("Pi", "NUC", "ID", image)


