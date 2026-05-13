from comunication import Server
from random import choice

def ImcCalculator(data: str) -> str:
    print("CALCULANDO.....")
    peso, altura = data.split(",")
    print("SPLITEADO")
    res = float(peso) / (float(altura) * float(altura))
    if res < 18.5: #bajo peso
        return f"{res:.1f}, peso bajo"
    elif 18.5 <= res <= 24.9: #peso normal
        return f"{res:.1f}, peso normal"
    elif 25 <= res <= 29.9: #sobrepeso
        return f"{res:.1f}, sobrepeso"
    else: #obesidad
        return f"{res:.1f}, obesidad"
    
server = Server()

try:
    server.listen()
    while True:
        try:
            print("try:")
            result = server.process(ImcCalculator)
            print(result, type(result))
            if result is None:
                print("Error en la conexión, esperando nuevo cliente...")
                raise KeyboardInterrupt
            res, cl = result
            print(f"IMC: {res}")
            cl.send(res.encode())
            cl.close()
        except KeyboardInterrupt:
            print("Servidor cerrado")
            break
        except Exception as e:
            print(f"Error: {e}")


except KeyboardInterrupt:
    print("Servidor cerrado")
finally:
    server.close()
