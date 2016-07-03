#!/usr/bin/python

from MultiWii import MultiWii
import threading

import time, socket, sys, os, json

STREAM_VIDEO = False
STREAM_VIDEO_CMD = None
TCP_IP = None
TCP_PORT = None

runUDPThread = True
board = None

cmd = 1

def startListeningUDP():
	global runUDPThread, conn, board, TCP_IP, TCP_PORT
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((TCP_IP, TCP_PORT))
	print "UDP Listening started..."
	while runUDPThread:
		dataStr, addr = sock.recvfrom(16)
		print dataStr
		data = [int(dataStr[0:4]), int(dataStr[4:8]), int(dataStr[8:12]), int(dataStr[12:16])]
		if len(dataStr) != 15:
			print "-- INCOMPLETE, SKIPPED --"
			continue
		if (cmd == 1 and board.isArmed()) {
			board.sendCMD(8, MultiWii.SET_RAW_RC, data);
		}		

def serverTCP():
	global TCP_IP, TCP_PORT, board, cmd
	s = socket.socket()         # Create a socket object
	s.bind((TCP_IP, TCP_PORT))  # Bind to the port
	s.listen(1)                 # Now wait for client connection.
	c = None
	dataStr = "1"
	while True:
		if c is None:
	   		c, addr = s.accept()     # Establish connection with client.
	   	else:
	   		msg = board.getData(MultiWii.ATTITUDE)
	   		if msg is not None:
	   			c.send(str(msg))
	   		dataStr = str(c.recv(8))

	   	if dataStr is not None:
			cmd = int(dataStr[:1])
		else:
			cmd = 1;
		print "TCP:" + str(cmd)
		
		if 0 == cmd:
			if not board.isArmed():
				board.arm()
		elif 1 == cmd:
			pass #do nothig, just fly		
		elif 2 == cmd and board.isArmed():
			board.disarm()
		elif 3 == cmd:
			if board.isArmed():
				board.disarm()
			os.system("sudo shutdown now")	
		elif 4 == cmd:
			if board.isArmed():
				board.disarm()
			os.system("sudo reboot")
		elif 5 == cmd:
			if board.isArmed():
				board.disarm()
			c.close()
				
		else:
			print dataStr				

def init():
	for i in xrange(4):
		global board 
		board = MultiWii("/dev/ttyUSB%d" % i)
		time.sleep(0.5)
		if board.ser.isOpen():
			print "SER OPEN"
			break
	else:
		print "MultiWii not found, exiting..."
		sys.exit(0);
		pass

	global TCP_IP, TCP_PORT, STREAM_VIDEO, STREAM_VIDEO_CMD	

	try:
		f = open("x-conf.json", "r").read()
		j = json.loads(f)
		TCP_IP = j["tcp_ip"]
		TCP_PORT = int(j["tcp_port"])
		STREAM_VIDEO = j["stream_video"]
		STREAM_VIDEO_CMD = j["stream_video_cmd"]
	except:
		print "Configuration file x-conf.json missing or incomplete, exiting..."
		sys.exit(0)

	if STREAM_VIDEO == "true": #json string
		os.system("sudo pkill uv4l")
		time.sleep(0.5)
		os.system(STREAM_VIDEO_CMD)

	t = threading.Thread(target=serverTCP)
	#t.setDaemon(True)
	t.start()		

	startListeningUDP()
	
init()
