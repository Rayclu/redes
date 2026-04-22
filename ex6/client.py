from comunication import Client
while True:
    msg = input("Ingrese un nuevo rango de números\n")
    try:
        Cl = Client()
        Cl.conn()
        Cl.sendMsg(msg)
        res = Cl.recv()
        print(res)
        print(f"La respuesta del servidor es: \t")

    except Exception as e:
        print(e)
        Cl.close()
    finally:
        if input("Si no desea ingresar más rangos tipee salir...").lower() == "salir":
            Cl.close()
            break