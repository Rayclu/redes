from comunication import Client
import json

cl = Client()
cl.conn()
while True:
    if input('Tipee "salir" si quiere dejar de convertir temperaturas!').lower() == "salir":
        break
    temperature: str = input("Enter any temperature with that format '<temperature><MeditionUnit(Celcius as C or Farenheit as F)>': ")
    cl.sendMsg(temperature)
    res = cl.recv()
    print(f"{temperature}=={res}")
cl.close()