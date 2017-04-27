import io
import time
import datetime
import picamera
import R2Protocol
import socket
from PIL import Image

#TCP protocol 
#TCP_IP = '127.0.0.1'
TCP_IP = '192.168.4.40'
TCP_PORT = 5005
BUFFER_SIZE = 1028


while(True):
	#Getting image
	#stream = io.BytesIO()
	#with picamera.PiCamera() as camera:
	#	camera.capture(stream, format='jpeg')
	#stream.seek(0)
	#image = stream.getvalue()
	
	#encoded = R2Protocol.encode("Pi", "NUC", "ID", image)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		#s.settimeout(0)
		#print(s.__closed)
		s.connect((TCP_IP, TCP_PORT))
		#Getting image
		#s.settimeout(None)
		stream = io.BytesIO()
		with picamera.PiCamera() as camera:
			camera.capture(stream, resize=( 640,360), format='jpeg')
		stream.seek(0)
		image = stream.getvalue()
		encoded = R2Protocol.encode("Pi", "NUC", "ID", image)
		s.send(encoded)
		s.close()
		time.sleep(2)
	except socket.timeout:
		print("Connection not open")


