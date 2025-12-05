"""
Enunciado:
Implementar la función 'obtain_max(list_numbers)' que recibe 
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada 'max'

Parámetros:
- list_numbers: Lista de números enteros

Ejemplo:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Salida:
    87

"""

def obtain_max(list_numbers):
    for number in list_numbers:
        if type(number) != int:
            raise TypeError("El parámetro de entrada debe ser una lista de números enteros")
    return max(list_numbers)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(obtain_max([1, 45, 87, 21, 0, 23, 28]))