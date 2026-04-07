# cliente.py
# El programa que inicia la conversación y recibe respuesta
import socket
# Crear el socket del cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Datos del servidor al que nos conectamos
IP = "127.0.0.1";
PUERTO = 8080;
# PARTE 1: Conectarse al servidor
print("Conectando...")
cliente.connect((IP, PUERTO))
print(" Conectado!;")
# PARTE 2: Enviar mensaje
mensaje = "Hola profe! Hice la tarea desde casa."
cliente.send(mensaje.encode())
print(f" Mensaje enviado: &#39;{mensaje}&#39;")
# PARTE 3: Recibir respuesta
respuesta = cliente.recv(1024).decode()
print(f" El servidor respondió: &#39;{respuesta}&#39;")
# Cerrar conexión
cliente.close()
print(" Cliente cerrado")


