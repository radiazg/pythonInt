def divisors(num):
    list_divisors = [i for i in range(1, num + 1) if num % i == 0]
    return list_divisors

def run():
    try:
        num = int(input("Escribir numero: "))
        print(divisors(num))
        print("*********Termino el programa**********")
    except ValueError:
        print("Debes ingresar un Número")

if __name__ == '__main__':
    run()