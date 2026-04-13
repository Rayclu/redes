import socket as skt
from typing import Tuple


class _ConectionConf:
    """Clase abstracta para configurar las redes"""
    def __init__(self, direccion: Tuple[str, int] = ("127.0.0.1", 8080)) -> None:
        self.direccion: Tuple[str, int] = direccion
        self.socket: skt.socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

    def close(self) -> None:
        self.socket.close()


class Server(_ConectionConf):
    def __init__(self, direccion = ("127.0.0.1", 8080)):
        super().__init__(direccion)
        self.socket.bind(direccion)

    def listen(self) -> None:
        try:
            self.socket.listen()
            print("listening")
        except:
            self.close()
    def acept(self) -> Tuple[skt.socket, Tuple[str, int]]:
        print("Ejecutando acept")
        try:
            print("Socket aceptado")
            return self.socket.accept()
        except:
            print("Se cierra el socket")
            self.close()
    def process(self, callback):
        try:
            cl, add = self.acept()
            data = cl.recv(1024)
            res = callback(data)
            return res, cl
        except:
            self.close()

class Client(_ConectionConf):
    def __init__(self, direccion: tuple[str, int] = ("127.0.0.1", 8080)):
        super().__init__(direccion)
    def conn(self) -> None:
       self.socket.connect(self.direccion)

    def sendMsg(self, datos: str) -> None:
        try:
            self.socket.send(datos.encode())
        except:
            self.close()
    def recv(self, tamaño: int = 1024) -> str:
        try:
            print("Recibiendo data en cliente")
            data = self.socket.recv(tamaño).decode()
            print(data)
            return data
        except:
            self.close()
