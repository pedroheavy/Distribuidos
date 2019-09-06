import socket

#Cria o socket udp
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Algo deu errado ao conectar ao socket")
    exit()

while 1:
    message = input("> ")
    if message == 'sair':
        break
    # passa pra byte
    message = message.encode()

    try:
        # envia a mensagem
        socket.sendto(message, ("3.92.227.210", 9999))

        # pega a resposta do servidor
        data, ip = socket.recvfrom(1024)
        mensagem_recebida = data.decode("utf-8")
        print("A mensagem enviada foi: " + mensagem_recebida)

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()
