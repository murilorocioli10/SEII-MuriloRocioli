'''O socket possui influencia ao tratar de servidores
com grande quantidade de requisicoes e chamadas'''

#Importando modulos
import socket       #modulo de sockets
import threading    #modulo de threads
import time         #modulo de tempo e data

PORT = 5050         #porta de acesso
FORMATO = 'utf-8'   #formato para codificacao
SERVER = "192.168.0.109"    #IP servidor 
ADDR = (SERVER, PORT)       #endereco do servidor

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #declarando client
client.connect(ADDR)


def handle_mensagens(): #gerenciar de mensagens
    while(True):
        msg = client.recv(1024).decode()    
        mensagem_splitada = msg.split("=")  
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))   #envia o formato de decodificacao

def enviar_mensagem():  #envia a mensagem
    mensagem = input()  #mensagem lida pelo terminal
    enviar("msg=" + mensagem)   #metodo de envio da mensagem

def enviar_nome():      #envia nome (client)
    nome = input('Digite seu nome: ')   #leitura via terminal
    enviar("nome=" + nome)  #envio do nome

def iniciar_envio():    #realiza inicio do envio da mensagem
    enviar_nome()       #envia o nome do cliente
    enviar_mensagem()   #envia mensagem


def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

iniciar()
