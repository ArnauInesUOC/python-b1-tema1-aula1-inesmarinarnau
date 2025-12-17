'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

'''

def count_vowels(text_chain:str):
    number_vowels = 0
    if type(text_chain) != str:
        raise ValueError("El parámetro de entrada debe ser únicamente string")
    for characters in text_chain:
        if characters in "aeiouAEIOU":
            number_vowels += 1
    return number_vowels
    
    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(count_vowels("Hello world, this is an example."))
