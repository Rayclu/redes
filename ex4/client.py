from comunication import Client

cl = Client()
try:
    cl.conn()
    data: list[float] = list()
    print("Ingrese las notas: \n")
    for i in range(0, 3):
        data.append(float(input(f"Nota {i}: ")))
    print(data)
    cl.sendMsg(' '.join(map(str, data)))
    print("Calculando promedio")
    avg = cl.recv(1024)
    print(type(avg))
    cl.close()
    print('the average is: ', avg)
except:
    cl.close()