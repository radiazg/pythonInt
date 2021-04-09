def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name":"Ricardo", "last_name":"Diaz"}

    super_list = [
        {"first_name":"Ricardo", "last_name":"Diaz"},
        {"first_name":"Juan", "last_name":"Diaz"},
        {"first_name":"Sebastian", "last_name":"Diaz"},
        {"first_name":"Laura", "last_name":"Higuita"}
    ]

    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "foating_nums":[1.1, 2.3, 5.5, 6.2, 9.5]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')
    
    for i in super_list:
        print(i["first_name"], " - ", i["last_name"])



if __name__ == '__main__':
    run()