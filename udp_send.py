import socket, struct

UDP_IP = "127.0.0.1"
UDP_PORT = 12345
#MESSAGE = "Hello, World!"


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#while True:
#x = raw_input("SEND: ")
data = [1001, 1002, 1003, 1004]
x = struct.pack('hhhh', data)
sock.sendto(x, (UDP_IP, UDP_PORT))