'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

'''

def invert_text(text_chain:str):
    inverted_text = ""
    if type(text_chain) != str:
        return ValueError("El parámetro de entrada debe ser una cadena de texto")
    else:
        inverted_text += text_chain[::-1] + inverted_text
    return inverted_text
        


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(invert_text("Hello world!"))
