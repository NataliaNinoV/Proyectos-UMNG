import socket  #Client

#inicia la direccion y el puerto del servidor 
host = socket.gethostname()  #127.0.0.1
port = 5000  

#inicializa el sockect y lo conecta al servidor
client_socket = socket.socket()  
client_socket.connect((host, port)) 

message = input(" -> ")  # toma un dato por teclado para ser enviado al servidor

while message.lower().strip() != 'adios':
    client_socket.send(message.encode())  # envia el mensaje
    data = client_socket.recv(1024).decode()  # recibe la respuesta

    print('informacion del servidor: ' + data)  # muestra la informacion obtenida

    message = input(" -> ")  # tado por teclado si es adios cierra la conexion

client_socket.close()  # termina la conexion 

