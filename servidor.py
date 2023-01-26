import socket # importar la libreria Server

# asignar la direccion y el puerto del servidor
# no inicializar el puerto en valores menores a 1024
host = socket.gethostname() 
port = 5000  

# creacion del socket y asignacion de la direccion y el puerto al socket
server_socket = socket.socket()  
server_socket.bind((host, port))  

# configurar cuantos clientes puede aceptar el servidor al mismo tiempo
server_socket.listen(2)

conn, address = server_socket.accept()  # aceptar nuevas conexiones
print("conectado desde: " + str(address))

while True:
    # obtiene la informacion, si tiene un valor mayor a 1024 bytes la descartara
    data = conn.recv(1024).decode()

    if not data:
        #si no hay datos termina el ciclo
        break
    print("data del cliente: " + str(data))
    data = input(' -> ')
    conn.send(data.encode())  # envia informacion al cliente

conn.close()  # termina la conexion 

