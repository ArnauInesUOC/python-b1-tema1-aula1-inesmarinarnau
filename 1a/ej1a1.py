'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

'''

def fibonacci(fibonacci_number):
    if type(fibonacci_number) != int:
        raise ValueError("El parámetro debe ser un número entero")
    elif fibonacci_number < 0:
        raise ValueError("El parámetro debe ser un número entero mayor o igual a 0")
    elif fibonacci_number == 1:
        return 1
    elif fibonacci_number == 0:
        return 0
    else:
        return fibonacci(fibonacci_number - 1) + fibonacci(fibonacci_number - 2)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(fibonacci(10))
