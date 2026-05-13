from comunication import Client


client = Client()
try:
    print("Conectado al servidor")
    client.conn()
    while True:
        options = ("piedra", "papel", "tijera")
        entry = input(f"Ingrese una opción <{options}>: ").strip()
        if not entry:
            print("Entry not found")
            continue
        print("pasamo entry")
        if entry == "salir":
            print("Cerrando conexión...")
            break
        print("pasamo salir")
        if not entry in options:
            client.sendMsg(entry)
            print("Mensaje enviado")
            res = client.recv()
            print("Respuesta:", res)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
