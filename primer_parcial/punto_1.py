#Desarrollar una función recursiva que permita contar cuantas veces
#aparece una determinada palabra, en un vector de palabras.

palabras = ['Hola', 'Cielo', 'Mundo', 'Hola', 'Cielo', 'Hola']

def contar_palabra_recursiva(palabras, palabra, contador=0):
    if len(palabras) == 0:
        return contador
    if palabras[0] == palabra:
        contador += 1
    return contar_palabra_recursiva(palabras[1:], palabra, contador)

palabra_buscada = 'Hola'
resultado = contar_palabra_recursiva(palabras, palabra_buscada)
print(f"La palabra '{palabra_buscada}' aparece {resultado} veces en la lista.")
