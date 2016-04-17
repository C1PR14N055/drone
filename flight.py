from MultiWii import MultiWii
from threading import Thread

import time, socket, sys, os

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
	print "Starting to receive data..."

	while runThread:
		dataStr, addr = sock.recvfrom(18)
		#print "Data:", dataStr
		data = [int(dataStr[0:4]), int(dataStr[4:8]), int(dataStr[8:12]), int(dataStr[12:16])]
		print data
		cmd = int(dataStr[16:17])
		print cmd
		if 0 == cmd:
			if not board.isArmed():
				board.arm()
			board.sendCMD(8, MultiWii.SET_RAW_RC, data);
		elif 1 == cmd:	
			board.sendCMD(8, MultiWii.SET_RAW_RC, data);
		elif 2 == cmd and board.isArmed():
			board.disarm()
		elif 3 == cmd:
			if board.isArmed():
				board.disarm()
			os.system("sudo shutdown now")	 		

def isDeviceConnected():
	resp = os.system("timeout 1 ping -c 1 192.168.1.32")

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