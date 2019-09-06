import socket

from pip._vendor.distlib.compat import raw_input


def Main():
    host = "localhost"
    porta = 5001

    servidor = ('127.0.0.1', 5000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, porta))

    mensagem = input("-> ")
    while mensagem != 'sair':
        mensagem_as_byte = str.encode(mensagem)
        sock.sendto(mensagem_as_byte, servidor)
        data, addr = sock.recvfrom(1024)
        print("Received from server: '" + str(data.decode("utf-8")) + "'")
        mensagem = input("-> ")
    sock.close()
if __name__ == '__main__':
    Main()

