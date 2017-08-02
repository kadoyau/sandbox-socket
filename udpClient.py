import socket

# host = '127.0.0.1'
host = '192.168.7.2'
port = 3794
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Type message...'
while True:
    send_msg = raw_input()
    serversock.sendto(send_msg, (host, port))
    if(send_msg=="0"):
        break
