import socket as _socket

#
# ns => new socket; socket.socket crea la conexion, configurando el como será esta. 
# #

ns = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
WEEK = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves", 
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}
def serving(ip: str, port: int ): 
    print("serving....")
    #
    # Esta función es la que termina de lanzar la conexion
    # #

    ns.bind((ip, port))
    try:    
        print("Pasé bind")
        #
        # ns.bind() abre el puerto.
        # #

        ns.listen()
        print("Pasé listen.")
        #
        # El puerto se queda atento a la primer conecxión que entre.
        # #

        client, dir = ns.accept()
        print("Se aceptó bien...")
        #
        # Acepta al cliente
        # #

        ans = WEEK.get(client.recv(1024).decode())
        print(ans)
        #
        # Decodifica el mensaje
        # #
        client.send(ans.encode()) #<- envía la respuesta codificada
        #-------------------------------------------------------------------
        # Cierra todo.
        # #
        client.close() 
        ns.close()
    except: 
        print("error")
        client.close()
        ns.close()
        raise "Error"
ip = "127.0.0.1"
port = 8080

print(serving(ip, port))