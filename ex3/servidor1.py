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
    #
    # Esta función es la que termina de lanzar la conexion
    # #
    try:
        print("try")
        ns.bind((ip, port))
        ns.listen()
        client, dir = ns.accept()
        while(True):
            print("While")
            #print("Pasé bind")
            #
            # ns.bind() abre el puerto.
            # #

            #print("Pasé listen.")
            #
            # El puerto se queda atento a la primer conecxión que entre.
            # #

            
            print("Se aceptó bien...")
            #
            # Acepta al cliente
            # #
            idx: any = client.recv(1024).decode()
            print("idx es:",idx, type(idx))
            ans: str = WEEK[int(idx)]
            print(ans)
            #
            # Decodifica el mensaje
            # #
            print("ans es:",type(ans))
            client.send(ans.encode()) #<- envía la respuesta codificada
            print("Se envió")
            #-------------------------------------------------------------------
            # Cierra todo.
            # #
    except KeyboardInterrupt:
        client.close() 
        ns.close()
    finally: 
        print("error")
        client.close()
        ns.close()
        return -1
ip = "127.0.0.1"
port = 8080

print(serving(ip, port))