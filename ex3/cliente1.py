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
# Conectar al servidor
cliente.connect((IP, PUERTO))

try:
    while(True):
        day = input("Enter any day")

        # Enviar mensaje al servidor
        print(day)
        cliente.send(day.encode())

        # Recibir respuesta del servidor
        respuesta = cliente.recv(1024).decode()
        print("La respuesta es:", respuesta)
        """flag = input("Would you want to send another day? <yes/no>")
        print(flag)
        if flag != "yes":
            break"""

except KeyboardInterrupt:
    cliente.close()
