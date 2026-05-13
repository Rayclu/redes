def numeros_primos(n):
    if n!=0:

        if n==2:
            print(f"{n} es un numero primo")
        elif n%n == 0 and n% 1 == 0 and n%2 !=0 :
            print(f"{n} es un numero primo")
        else:
            print(f"{n} no es primo") 
    else:
        print("su numero es 0")

def main(): 
    num = int(input("ingrese un número: "))
    numeros_primos(num)
main()