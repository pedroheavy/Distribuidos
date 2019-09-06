
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(str.encode('Fake reply'),('13.92.227.210',5000))
