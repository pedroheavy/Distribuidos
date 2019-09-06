import socket

# configura o tipo do socket e define o local
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 9999))

while 1:

    # pega os dados recebidos com buffer
    data, ip = socket.recvfrom(1024)

    # envia mensagem de volta
    envia_deVolta = socket.sendto(data, ip)

    print("A mensagem recebida foi: %s"%(data.decode("utf-8")))
    print("O tamanho dos dados recebidos foi %s" %(len(data)))
    print("O tamanho dos dados enviados de volta foi de %s"%(int(envia_deVolta)))
