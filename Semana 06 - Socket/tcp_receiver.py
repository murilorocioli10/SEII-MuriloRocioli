import socket   #importa o modulo do socket


TCP_IP = "127.0.0.1"    #IP servidor TCP
FILE_PORT = 5005        #porta arquivo
DATA_PORT = 5006        #porta dados
timeout = 3             #tempo limite para requisição
buf = 1024              #tamanho buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #inicialização do socket
sock_f.bind((TCP_IP, FILE_PORT))    #associação do socket com localhost
sock_f.listen(1)    #abertura para solicitação de conexões


sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicialização do socket dos dados
sock_d.bind((TCP_IP, DATA_PORT))  #associação(bind) do socket com  localhost
sock_d.listen(1)    #abertura para solicitação de conexões


while True:
    conn, addr = sock_f.accept()    #atribuicao da conn e do address ao aceitar a conexao com o client
    data = conn.recv(buf)           #armazena o nome do arquivo
    if data:    #verifica se o nome do arquivo não é nulo
        print("File name:", data)   #imprime o nome do arquivo
        file_name = data.strip()    #remove espaços do nome do arquivo

    f = open(file_name, 'wb') #instancia o arquivo

    conn, addr = sock_d.accept() #atribuicao da conn e do address ao aceitar a conexao com o client
    while True:
        data = conn.recv(buf) #armazena os dados salvos com o tamanho do buffer
        if not data:          #se os dados forem vazios (nulos) sai do laço
            break
        f.write(data)         #armazena os dados no arquivo

    print("%s Finish!" % file_name) #imprime a finalização da escrita do arquivo
    f.close()                 #fecha o arquivo
