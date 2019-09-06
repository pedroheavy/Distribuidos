import socket


def Main():
    host = "127.0.0.1"
    porta = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, porta))

    print("Servidor foi iniciado com sucesso")

    while True:
        dados, endereco =  sock.recvfrom(1024)
        print ("message from" + str(endereco))
        print("from connected user: " + str(dados.decode("utf-8")))
        dados = str(dados).upper()
        pro_cliente = input("-> ")
        dados_as_bytes =  str.encode(pro_cliente)
        sock.sendto(dados_as_bytes, endereco)
    sock.close()

if __name__ == '__main__':
    Main()



