import socket #importa o modulo para trabalho com socket
import select #importa o modulo select


UDP_IP = "127.0.0.1" #IP do servidor UDP
IN_PORT = 5005       #porta do servidor
timeout = 3          #tempo limite para requisição/solicitação


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criação do servidor UDP para trabalho com socket
sock.bind((UDP_IP, IN_PORT)) #associação(bind) do socket com  localhost


while True:
    data, addr = sock.recvfrom(1024) #recebe e armazena os dados do sender (client)
    if data:    #verifica se os dados não são nulos
        print("File name:", data)   #printa o nome do arquivo
        file_name = data.strip()    #remove espaços do nome do arquivo

    f = open(file_name, 'wb')       #abre/cria um arquivo para escrita em binário

    while True:
        ready = select.select([sock], [], [], timeout) #utiliza o método select para multiplexar a entrada e saída
        if ready[0]:
            data, addr = sock.recvfrom(1024)           #recebe e armazena os dados do sender
            f.write(data)                              #escreve/salve os dados lidos no arquivo
        else:
            print("%s Finish!" % file_name)            #printa o estado de escrita
            f.close()                                  #fecha o arquivo
            break                                      #sai do laço
