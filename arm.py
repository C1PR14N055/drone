from MultiWii import MultiWii

def __init__():
	board = MultiWii("/dev/ttyUSB0")
	if board.ser.isOpen():
		board.arm()

__init__()		






