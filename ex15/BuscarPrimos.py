"""a) Devuelva una lista con todos los que sean primos."""

def numeros_primos(n):
    """    
    if n!=0:

        if n==2:
            print(f"{n} es un numero primo")
            return True
        elif n%n == 0 and n% 1 == 0 and n%2 !=0 and n%3!=0:
            print(f"{n} es un numero primo")
            return True
        else:
            print(f"{n} no es primo")
            return False 
    """
    """if n==4:
        print(f"El numero {n} no es primo")
        return False"""
    cont=0
    primo=int(n**(1/2))
    i=1
    if n==2:
        print("El número 2 es primo.")
        return n, True
    while i<=n:
        if primo%i==0:
            cont+=1        
        i+=1
        print(cont)
    
    if cont>=3:
        print(f"El número {n} no es primo")
        return n, False
    else:
        print(f"El numero {n} es primo")
        return n, True
    
def primos(num):
    ListaPrimos=[]
    key="si"
    while key=="si":
        if numeros_primos(num)==True:
            ListaPrimos.append(num)
        key=input("Quiere seguir ingresando numeros?<si/no>")
        num=int(input("ingrese otro numero"))
    return ListaPrimos

def main(): 
    num = int(input("ingrese un número: "))
    print(primos(numeros_primos(num)))


main()