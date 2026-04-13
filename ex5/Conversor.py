from comunication import Server

conversor_server = Server()

def converter(ft: list) -> str:
    temperature_format: str = str(ft.pop()).capitalize()
    print(temperature_format)
    print(ft)
    final_temerature = [int("".join(ft)), temperature_format]
    print(temperature_format)
    print(final_temerature)
    def CelToFar(temperature: int) -> int:
        return int((temperature*(9/5))+32)
    def FarToCel(temperature: int) -> int:
        return int((temperature-32)*(5/9))
    def Err():
        raise "Invalid Format"
    match temperature_format:
        case "F":
            return str(FarToCel(final_temerature[0]))
        case "C":
            return str(CelToFar(final_temerature[0]))
        case _:
            return Err()

conversor_server.listen()
try:
    cl_res, cl_sock = conversor_server.process(converter)
    print(cl_res)
    cl_sock.send(cl_res.encode())
except Exception as e:
    print(e)
    conversor_server.close()