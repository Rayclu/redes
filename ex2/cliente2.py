"""
Cliente TCP simple para comunicación de red.
Conecta a un servidor en localhost:8080 y envía un mensaje.
"""

import socket


# Crear socket TCP/IP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuración del servidor
IP = "127.0.0.1"  # Dirección IP del servidor (localhost)
PUERTO = 8080  # Puerto del servidor


def sendDay(day: int): 
    try:
        # Conectar al servidor
        cliente.connect((IP, PUERTO))

        # Enviar mensaje al servidor
        cliente.send(day.encode())

        # Recibir respuesta del servidor
        respuesta = cliente.recv(1024).decode()
        flag = input("Would you want to send another day?")
        return cliente.close() if not flag.lower() is "yes" else sendDay(input("Enter any day"))
    finally:
        cliente.close()
        return -1

sendDay(input("Enter any day"))




