from comunication import Client

client = Client()

try:
    client.conn()
    print("Conectado al servidor")
    while True:
        email = input("Ingresa un email (o escribe 'salir' para terminar): ")
        if email.lower() == "salir":
            print("Desconectando...")
            break
        client.sendMsg(email)
        response = client.recv()
        print(f"Respuesta del servidor: {response}\n")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
