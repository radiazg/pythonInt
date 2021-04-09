def divisors(num):
    assert num > 0, "Debes ingresar un numero positivo" 
    list_divisors = [i for i in range(1, num + 1) if num % i == 0]
    return list_divisors

def run():
    num = input("Escribir numero: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("*********Termino el programa**********")


if __name__ == '__main__':
    run()