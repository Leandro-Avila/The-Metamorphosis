import socket, client
import Variaveis as v
from time import sleep


def server(c, cliente):
    host = '127.0.0.1'
    port = 5505
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.bind((host, port))
    conexao.listen(1)
    print("conectado com", cliente)
    while True:
        c, cliente = conexao.accept()
        msg = c.recv(1024)
        if not msg:
            conexao.close()
        if v.tela_a:
            msg = 'a'
            conexao.send(msg.encode('utf-8'))
            print(msg)
        if msg == b'd':
            v.tela_d = True
        sleep(0.5)


