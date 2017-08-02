# coding:UTF-8
import socket
host = '127.0.0.1'
port = 3794
# ソケットの作成
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ソケットとIPアドレスの関連づけ
serversock.bind((host,port))
# クライアントとの接続の準備
serversock.listen(1)
print('Waiting for connections...')

# クライアントとの接続
clientsock, client_address = serversock.accept()

while True:
    rcvmsg = clientsock.recv(1024)
    print('Received -> ' + rcvmsg.decode("UTF-8"))
    if rcvmsg.decode("UTF-8") == '':
        break
    # print('Type message...')
    # s_msg = input()
    # if s_msg == '':
    #   break
    # print('Wait...')
    # clientsock.sendall(bytearray(s_msg,'UTF-8')) # string->byte
clientsock.close()
