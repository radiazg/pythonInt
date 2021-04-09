#Antigua función de palindromo
""" def evaluar_palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    palabra_inversa = palabra[::-1]
    if palabra == palabra_inversa:
        return True
    else:
        return False


def run():
    palabra = input('Escribir una palabra o frase:')
    es_palindromo = evaluar_palindromo(palabra)
    if (es_palindromo):
        print(f'La palabra/frase {palabra} es un palindromo')
    else:
        print(f'La palabra/frase {palabra} no es un palindromo')


if __name__ == '__main__':
    run() """



def run():
    palabra = input('Escribir una palabra o frase:')
    palabra = palabra.replace(' ','').lower()
    palindrome = lambda string: string == string[::-1]
    es_palindromo = palindrome(palabra)
    if (es_palindromo):
        print(f'La palabra/frase {palabra} es un palindromo')
    else:
        print(f'La palabra/frase {palabra} no es un palindromo')


if __name__ == '__main__':
    run()