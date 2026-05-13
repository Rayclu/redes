from comunication import Server
from random import choice


class NServer(Server):
    def __init__(self, direccion=("127.0.0.1", 8080)):
        super().__init__(direccion)
        self.phrases = set()
    
    def add(self, phrase: str) -> str:
        """Add a new phrase"""
        if not phrase:
            raise Exception("La frase no puede estar vacía")
        self.phrases.add(phrase)
        return phrase

    def listPhrases(self) -> str:
        """List all phrases with numbers"""
        print("LISTANDO....")
        if not self.phrases:
            return "No hay frases disponibles"
        return "\n".join([f"{i+1}. {phrase}" for i, phrase in enumerate(self.phrases)])

    def processMsg(self, msg: str) -> str:
        """Process incoming message"""
        print("msg es -> ", msg)

        if msg.startswith("frase"):
            if not self.phrases:
                return "No hay frases disponibles"
            return choice(self.phrases)

        elif msg.startswith("agregar,"):
            text = msg[8:].strip()
            if not text:
                return "Error: El texto no puede estar vacío"
            return self.add(text)

        elif msg.startswith("contar"):
            return str(len(self.phrases))

        elif msg.startswith("listar"):
            return self.listPhrases()
        elif msg.startswith("salir"):
            raise KeyboardInterrupt

        else:
            return "Comando desconocido"


phrase_server = NServer()
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
                        break
                    res = phrase_server.processMsg(data)
                    cl.send(res.encode())
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
