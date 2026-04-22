from comunication import Server

serv = Server()

def email_checker(data: str) -> bool:

    if " " in data:
        raise Exception( "Error: No se pueden tener espacios")
    
    if not data.count("@") == 1:
        parts = data.split("@")
        if not len(parts[0]) == 0:
            return ("." in parts[1]) and (not parts[1].startswith(".")) and (not parts[1].endswith("."))

    raise Exception ("Error: El email debe tener exactamente un @")

try:
    serv.listen()
    while True:
        result, client_socket = serv.process(email_checker)
        client_socket.send(result.encode())
        client_socket.close()
except KeyboardInterrupt:
    print("Servidor detenido")
    serv.close()
except Exception as e:
    print(f"Error: {e}")
    serv.close()