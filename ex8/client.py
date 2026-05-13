from comunication import Client

def show_menu():
    """Display available commands"""
    print("\n=== Comandos disponibles ===")
    print("  frase        - Recibir una frase al azar")
    print("  agregar,texto - Agregar una nueva frase")
    print("  contar       - Ver la cantidad de frases")
    print("  listar       - Ver todas las frases con número")
    print("  salir        - Cerrar la conexión")
    print("===========================\n")

client = Client()
try:
    print("Conectado al servidor")
    show_menu()
    client.conn()
    while True:
        entry = input("Ingrese un comando: ").strip()
        if not entry:
            print("Entry not found")
            continue
        if entry == "salir":
            print("Cerrando conexión...")
            break

        if entry.startswith("agregar,"):
            # Validate that text is not empty
            text = entry[8:].strip()
            if not text:
                print("Error: El texto no puede estar vacío")
                continue
            client.sendMsg(entry)
        else:
            client.sendMsg(entry)

        res = client.recv()
        print("Respuesta:", res)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
