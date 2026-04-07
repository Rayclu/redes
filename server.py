import socket as _sock

socket: str = ["127.0.0.1","8080"] 
def server(socket):
    _sock.socket(_sock.AF_INET, _sock.SOCK_STREAM)
    type(_sock)
    _sock.bind((int(socket[0]), int(socket[1])))
    _sock.listen(1)
    cliente, direccion = _sock.accept()

    print(" Esperando conexiones...")
    # Aceptar un cliente (ESTA LÍNEA SE QUEDA ESPERANDO)
    print(f" Cliente conectado desde {direccion}")

    # PARTE 1: Recibir mensaje del cliente
    mensaje = cliente.recv(1024).decode()
    print(f" Mensaje recibido: &#39;{mensaje}&#39;")
    # PARTE 2: Enviar respuesta al cliente
    respuesta = f" Recibí tu mensaje: &#39;{mensaje}&#39;. Todo OK!"
    cliente.send(respuesta.encode())
    print(f" Respuesta enviada: &#39;{respuesta}&#39;")
    # Cerrar todo
    cliente.close()
    _sock.close()

server(socket)



