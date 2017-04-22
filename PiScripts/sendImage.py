import io
import time
import picamera
import R2Protocol
import socket
from PIL import Image

#TCP protocol 
#TCP_IP = '127.0.0.1'
TCP_IP = '192.168.4.123'
TCP_PORT = 5005
BUFFER_SIZE = 1024


while(True):
	#Getting image
	stream = io.BytesIO()
	with picamera.PiCamera() as camera:
		camera.capture(stream, format='jpeg')
	stream.seek(0)
	image = stream.getvalue()
	
	encoded = R2Protocol.encode("Pi", "NUC", "ID", image)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		#print(s.__closed)
		s.connect((TCP_IP, TCP_PORT))
		s.send(encoded)
		s.close()
	except ConnectionRefusedError:
		print("Connection not open")


