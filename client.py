import socket
import Variaveis as v


def client_thread():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.15.5'
    port = 5500
    conexao.connect((host, port))
    print('conected')
    msg = ' '
    while True:
        rec = conexao.recv(1024)
        if v.tela_d:
            msg = 'd'
            conexao.send(msg.encode('utf-8'))
        elif v.tela_e:
            msg = 'e'
            conexao.send(msg.encode('utf-8'))
        elif v.tela_f:
            msg = 'f'
            conexao.send(msg.encode('utf-8'))
        if rec == b'a':
            v.tela_a = True
        elif rec == b'b':
            v.tela_b = True
        elif rec == b'c':
            v.tela_c = True
        conexao.send(msg.encode('utf-8'))

