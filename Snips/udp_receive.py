import socket

UDP_IP = ""
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(16) # buffer size is 1024 bytes
    print "Data:", data