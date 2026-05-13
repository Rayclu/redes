from comunication import Server
from random import choice

def numeros_primos(n):
    n = int(n)
    if n!=0:
        if n==2:
            return f"{n} es un numero primo"
        elif n%n == 0 and n% 1 == 0 and n%2 !=0 :
            return f"{n} es un numero primo"
        else:
            return f"{n} no es primo"
    else:
        return "su numero es 0"
server = Server()

try:
    server.listen()
    while True:
        try:
            print("try:")
            result = server.process(numeros_primos)
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
