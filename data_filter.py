DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    
    #usamos filter para filtrar las personas mayores de 18
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #usamos map para transformar la lista anterior y solo tomar el nombre
    adults = list(map(lambda worker: worker["name"], adults))
    
    #nueva lista de diccionario, pero con una llave mas, old=true / false
    #python 3.9 ->
    #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #python 3.5 -> 3.9
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    print("Python Devs:")
    for worker in all_python_devs:
        print(worker)

    print("Platzi Workers:")
    for worker in all_platzi_workers:
        print(worker)

    print("Adults:")
    for worker in adults:
        print(worker)

    print("Olds:")
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()