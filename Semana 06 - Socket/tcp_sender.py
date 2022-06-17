import socket #importa o modulo socket
import sys    #importa o modulo sys

TCP_IP = "127.0.0.1"    #IP servidor TCP
FILE_PORT = 5005        #porta arquivo
DATA_PORT = 5006        #porta dados
buf = 1024              #tamanho buffer
file_name = sys.argv[1] #define o nome do arquivo através da leitura via terminal


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #inicialização do socket
    sock.connect((TCP_IP, FILE_PORT)) #conexao do socket com o localhost
    sock.send(file_name)              #envia o nome do arquivo
    sock.close() #finaliza o socket instanciado


    print("Sending %s ..." % file_name) #printa o status de envio do socket


    f = open(file_name, "rb") #abre o arquivo para leitura em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicialização do socket
    sock.connect((TCP_IP, DATA_PORT))   #realiza a conexão com o host
    data = f.read()                     #armazena os dados lidos no arquivo
    sock.send(data)                     #envia os dados presentes no arquivo
finally:
    sock.close()    #encerra a conexão
    f.close()       #fecha o arquivo
