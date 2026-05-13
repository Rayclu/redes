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
    while True:
        entry = input("INGRESE SU ALTURA Y PESO <ej: 70,1.75>: ").strip()
        if not entry:
            print("Entry not found")
            continue
        if entry == "salir":
            print("Cerrando conexión...")
            break

        try:
            client.conn()
            client.sendMsg(entry)
            res = client.recv()
            print("Respuesta:", res)
            client.close()
            client = Client()  # Reconectar para el siguiente mensaje
        except Exception as e:
            print(f"Error en la comunicación: {e}")
            client = Client()

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
