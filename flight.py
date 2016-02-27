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
		print "Data:", dataStr
		data = [int(dataStr[0:4]), int(dataStr[4:8]), int(dataStr[8:12]), int(dataStr[12:16])]
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

'''
board = MultiWii('/dev/ttyUSB0')

r = 1500
p = 1500
y = 1500
t = 1000
a1 = 1000
a2 = 1000
a3 = 1000
a4 = 1000

runTh = True

def ask(): 
	global r
	global p
	global y
	global t
	global a1
	global a2
	global a3
	global a4

	while True:
		x = raw_input("ROLL: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			r = int(x);
		else:
			print "!!! SKIPED !!!"

		x = raw_input("PITCH: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			p = int(x);
		else:
			print "!!! SKIPED !!!"

		x = raw_input("YAW: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			y = int(x);
		else:
			print "!!! SKIPED !!!"

		x = raw_input("THROTTLE: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			t = int(x);
		else:
			print "!!! SKIPED !!!"

		x = raw_input("AUX 1: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			a1 = int(x);
		else:
			print "!!! SKIPED !!!"				
		
		x = raw_input("AUX 2: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			a2 = int(x);
		else:
			print "!!! SKIPED !!!"

		x = raw_input("AUX 3: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			a3 = int(x);
		else:
			print "!!! SKIPED !!!"	

		x = raw_input("AUX 4: ");
		if (x != '' and isinstance(int(x), numbers.Number)):
			a4 = int(x);
		else:
			print "!!! SKIPED !!!"				

def send():
	global r
	global p
	global y
	global t
	global a1
	global a2
	global a3
	global a4

	global runTh

	while runTh:
		data = [r, p, y, t, a1, a2, a3, a4]
		board.sendCMD(16, MultiWii.SET_RAW_RC, data)
		time.sleep(0.05)
	
def arm():
	board.arm()

def disarm(signal, frame):
	global runTh
	runTh = False
	board.disarm()
	print "\nDisarming..."
	time.sleep(3)
	print "\nBye"
	sys.exit(0)	

signal.signal(signal.SIGINT, disarm)
arm()
th = Thread(target=send, args=())
th.start()
ask()

'''