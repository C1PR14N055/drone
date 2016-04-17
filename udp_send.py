import socket, struct

UDP_IP = "192.168.1.1"
UDP_PORT = 12345
#MESSAGE = "Hello, World!"


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#while True:
#x = raw_input("SEND: ")
data = [1001, 1002, 1003, 1004]
x = struct.pack('hhhh', 1001, 1002, 1003, 1004)
sock.sendto(x, (UDP_IP, UDP_PORT))
