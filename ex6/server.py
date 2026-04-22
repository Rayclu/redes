from comunication import Server
from random import randint


def generate_num(msg: str) -> int:
    print("msg es -> ", msg)
    nmsg = msg.split(",")
    print(len(nmsg))
    print(type(msg))
    nmsg = list(map(int, nmsg))
    print("nmsg es -> ", nmsg)
    if(nmsg[0] < nmsg[1]):
        nnro = randint(nmsg[0], nmsg[1])
        print("nnro es -> ", nnro)
        return nnro
    raise "Invalid arguments"

random_number_server = Server()
try:
    random_number_server.listen()
    res, cl = random_number_server.process(generate_num)
    print(res)
    cl.send(str(res).encode())

except:
    random_number_server.close()