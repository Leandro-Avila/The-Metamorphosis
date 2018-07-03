import socket, client
import Variaveis as v


def server():
    host = '192.168.15.5'
    port = 5500
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.bind((host, port))
    conexao.listen(1)
    msg = ' '
    print('aguardando conexão!')
    c, cliente = conexao.accept()
    print('conectado')
    while True:
        c.send(msg.encode('utf-8'))
        if v.tela_a:
            msg = 'a'
            c.send(msg.encode('utf-8'))
        elif v.tela_b:
            msg = 'b'
            c.send(msg.encode('utf-8'))
        elif v.tela_c:
            msg = 'c'
            c.send(msg.encode('utf-8'))
        rec = c.recv(1024)
        if rec == b'd':
            v.tela_d = True
        elif rec == b'e':
            v.tela_e = True
        elif rec == b'f':
            v.tela_f = True


