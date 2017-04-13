import io
import time
import picamera
import R2Protocol
from PIL import Image

stream = io.BytesIO()
with picamera.PiCamera() as camera:
	camera.capture(stream, format='jpeg')
stream.seek(0)
image = stream.getvalue()
with open("file.txt", 'wb') as f:
	f.write(image)

encoded = R2Protocol.encode("Pi", "NUC", "ID", stream.getvalue()) 

decoded = R2Protocol.decode(encoded)
with open("file1.txt", 'wb') as f:
	f.write(decoded["data"])

