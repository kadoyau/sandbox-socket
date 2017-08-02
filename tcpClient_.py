# coding:UTF-8
import socket
# host = '127.0.0.1'
host = '192.168.0.7'
port = 3794

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host,port))

while True:
    print('Type message...')
    c_msg = input()
    if c_msg == '':
      break
    # print('Wait...')
    clientsock.sendall(bytearray(c_msg,'UTF-8')) # string->byte
    # rcvmsg = clientsock.recv(1024)
    # print('Received -> ' + rcvmsg.decode("UTF-8")) #byte->string
    # if rcvmsg == '':
    #   break
clientsock.close()
