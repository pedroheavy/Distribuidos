import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.100.23', 5000)
message = 'This is the message.  It will be repeated.'
message_asbyte = str.encode(message)

try:

    # Send data
    print(sys.stderr, 'sending "%s"' % message)
    sent = sock.sendto(message_asbyte, server_address)

    # Receive response
    print (sys.stderr, 'waiting to receive')
    data, server = sock.recvfrom(1024)
    print (sys.stderr, 'received "%s"' % data)

finally:
    print (sys.stderr, 'closing socket')
    sock.close()
