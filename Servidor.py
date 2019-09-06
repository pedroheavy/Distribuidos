import socket

from pip._vendor.distlib.compat import raw_input


def Main():
    host = "localhost"
    porta = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, porta))

    print("Servidor foi iniciado com sucesso")

    while True:
        dados, endereco =  sock.recvfrom(1024)
        print ("message from" + str(endereco))
        print("from connected user: " + str(dados.decode("utf-8")))
        dados = str(dados).upper()
        pro_cliente = raw_input("-> ")
        dados_as_bytes =  str.encode(pro_cliente)
        sock.sendto(dados_as_bytes, endereco)
    sock.close()

if __name__ == '__main__':
    Main()



