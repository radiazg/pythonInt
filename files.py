def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as numbers_file:
        for line in numbers_file:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Ricardo", "Sebastian", "Laura", "Pepe", "Andrés"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as names_file:
        for name in names:
            #escribe item de la lista en el archivo
            names_file.write(name)
            #escribe un salto de líne
            names_file.write("\n")


def run():
    write()
    read()


if __name__ == '__main__':
    run()