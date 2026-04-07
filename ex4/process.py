import comunication as conf
def average(client_msgs):
    ns = list(map(float, client_msgs.decode().split()))
    print("ns ->", ns)
    res = sum(ns) / len(ns)
    return res

server = conf.Server()
server.listen()
try:
    cl_res, client_socket = server.process(average)
    print(server.socket._closed)
    client_socket.send(str(cl_res).encode())
    client_socket.close()

finally:
    server.close()