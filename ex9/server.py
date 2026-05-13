from comunication import Server
from random import choice


phrase_server = Server()
def play(client_play: str) -> tuple:
    def thinkPlay(serverPlay, clientPlay):
        table = {
            "piedra": {
                "gana": "tijera",
                "pierde": "papel",
            },
            "tijera": {
                "gana": "papel",
                "pierde": "piedra",
            },
            "papel": {
                "gana": "piedra",
                "pierde": "tijera",
            }
        }

        match serverPlay:
            case "piedra":
                selected_option = table["piedra"]
                if not clientPlay in selected_option:
                    return "empate"
                if not clientPlay == selected_option["gana"]:
                    return "servidor pierde"
                return "cliente gana"
            case "papel":
                selected_option = table["papel"]
                if not clientPlay in selected_option:
                    return "empate"
                if not clientPlay == selected_option["gana"]:
                    return "servidor pierde"
                return "cliente gana"
            case "tijera":
                selected_option = table["tijera"]
                if not clientPlay in selected_option:
                    return "empate"
                if not clientPlay == selected_option["gana"]:
                    return "servidor pierde"
                return "cliente gana"
            case _:
                raise Exception("Invalid Option in thinkPlay")
    options = ["piedra", "papel", "tijera"]
    server_play = choice(options)
    res = thinkPlay(server_play, client_play)
    print(res)
    return (f"CLiente: {client_play}", f"Server: {server_play}", f"Resultado: {res}")
try:
    phrase_server.listen()
    while True:
        try:
            cl, add = phrase_server.acept()
            # Mantener la conexión abierta para múltiples mensajes
            while True:
                try:
                    data = cl.recv(1024).decode()
                    if not data:  # Cliente desconectó
                        print("no hay data")
                        break
                    res = phrase_server.process(play)
                    print("Procesado")
                    cl.send(str(res).encode())
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    print(f"Error procesando mensaje: {e}")
                    break
            cl.close()
        except KeyboardInterrupt:
            print("Servidor cerrado")
            break
        except Exception as e:
            print(f"Error: {e}")

except KeyboardInterrupt:
    print("Servidor cerrado")
finally:
    phrase_server.close()
