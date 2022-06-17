import socket #importa o modulo para trabalho com socket
import time   #importa o modulo para trabalho com tempo
import sys    #importa o modulo sys

UDP_IP = "127.0.0.1"        #IP do servidor UDP
UDP_PORT = 5005             #porta do servidor
buf = 1024                  #tamanho do buffer 
file_name = sys.argv[1]     #define o nome do arquivo através da leitura via terminal


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #inicialização(instancia) do socket
sock.sendto(file_name, (UDP_IP, UDP_PORT))              #envia o nome do arquivo
print("Sending %s ..." % file_name)                     #printa o status de envio

f = open(file_name, "r") #abre o arquivo para leitura
data = f.read(buf)       #lê e armazena os dados lidos


while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #envia os dados para IP e porta atribuídos
        data = f.read(buf)                     #leitura do arquivo, linha a linha
        time.sleep(0.02)                       #delay

sock.close() #finaliza conexão
f.close()    #fecha o arquivo
