import socket
import Variaveis as v
from time import sleep


def client_thread():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5505
    conexao.connect((host, port))
    print('conected')

    while True:
        msg = conexao.recv(1024)
        if v.tela_d:
            msg = 'd'
            conexao.send(msg.encode('utf-8'))
            print(msg)
        if msg == b'a':
            v.tela_a = True
        sleep(0.5)

