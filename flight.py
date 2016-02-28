from pyMultiWii import MultiWii
from threading import Thread

import time, socket, sys

USE_TCP_PLEASE = False
TCP_PORT = 12345
UDP_IP = "192.168.1.143"
UDP_PORT = 12345

runThread = True
board = None

def startReceivingUDP():
	global runThread
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', UDP_PORT))

	while runThread:
		dataStr, addr = sock.recvfrom(16)
		#print "Data:", dataStr
		data = [int(dataStr[0:4]), int(dataStr[4:8]), int(dataStr[8:12]), int(dataStr[12:16])]
		print data
		board.sendCMD(8, MultiWii.SET_RAW_RC, data);



def init():
	for i in range(4):
		global board 
		board = MultiWii('/dev/ttyUSB%d' % i)
		time.sleep(0.5)
		if board.ser.isOpen():
			break
	else:
		sys.exit(0);			

	if USE_TCP_PLEASE:
		startTCPServer()
	else: startReceivingUDP()		
	


init()