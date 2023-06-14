from lista1 import Lista

class personajes:
    def __init__(self, superheroe, nombre, grupo, aparicion):
        self.superheroe = superheroe
        self.nombre = nombre
        self.grupo = grupo
        self.aparicion = aparicion

    def __str__(self):
        return f'{self.superheroe} - {self.nombre} - {self.grupo} - {self.aparicion}'

pj1 = personajes('Star Lord', 'Peter Quill', 'Guardianes de la galaxia', 1976)
pj2 = personajes('Capitana Marvel', 'Carol Danvers', 'Avengers', 1968)
pj3 = personajes('El Hombre Elastico', 'Reed Richards', 'Los Cuatro Fantasticos', 1961)
pj4 = personajes('Vlanck Widow', 'Natasha Romanoff', 'Avengers', 1964)
pj5 = personajes('Hulk', 'Bruce Banner', 'Avengers', 1962)

lista_personajes = Lista()

lista_personajes.insert(pj1, 'superheroe')
lista_personajes.insert(pj2, 'superheroe')
lista_personajes.insert(pj3, 'superheroe')
lista_personajes.insert(pj4, 'superheroe')
lista_personajes.insert(pj5, 'superheroe')
print()

if lista_personajes.search('Capitana Marvel', 'superheroe') is not None:
    print("Capitana Marvel está en la lista")
    personaje = lista_personajes.get_element_by_index(lista_personajes.search('Capitana Marvel', 'superheroe'))
    print("Nombre de personaje:", personaje.nombre)
else:
    print("Capitana Marvel no está en la lista")
print()

cola_guardianes = Lista()
for personaje in lista_personajes._Lista__elements:
    if personaje.grupo == "Guardianes de la galaxia":
        cola_guardianes.insert(personaje, 'superheroe')

print("Cantidad de superhéroes en el grupo 'Guardianes de la galaxia':", cola_guardianes.size())
print()

cuatro_fantasticos = Lista()
guardianes_galaxia = Lista()
cuatro_fantasticos.insert(pj3, 'grupo')
guardianes_galaxia.insert(pj1, 'grupo')
cuatro_fantasticos.order_by('superheroe', reverse=True)
guardianes_galaxia.order_by('superheroe', reverse=True)
print("Superhéroes de Los Cuatro Fantásticos en orden descendente:")
cuatro_fantasticos.barrido()
print("Superhéroes de Guardianes de la Galaxia en orden descendente:")
guardianes_galaxia.barrido()
print()

print("Superhéroes con año de aparición posterior a 1960:")
for personaje in lista_personajes._Lista__elements:
    if personaje.aparicion > 1960:
        print(personaje)
print()

for i in range(lista_personajes.size()):
    if lista_personajes.get_element_by_index(i).superheroe == 'Vlanck Widow':
        lista_personajes.get_element_by_index(i).superheroe = "Black Widow"
        print("Nombre de 'Black Widow' corregido.")

personajes_auxiliares = [
    personajes('Black Cat', 'Felicia Hardy', 'Avengers', 1979),
    personajes('Rocket Racoonn', 'Rocket', 'Guardianes de la galaxia', 1982),
    personajes('Loki', 'Loki Laufeyson', 'Avengers', 1949)
]
print()

for personaje_auxiliar in personajes_auxiliares:
    if lista_personajes.search(personaje_auxiliar.superheroe, 'superheroe') is None:
        lista_personajes.insert(personaje_auxiliar, 'superheroe')

print("Personajes que comienzan con C, P o S:")
for personaje in lista_personajes._Lista__elements:
    if personaje.nombre[0] in ['C', 'P', 'S']:
        print(personaje)
print()

personajes_adicionales = [
    personajes('Spider-Man', 'Peter Parker', 'Avengers', 1962),
    personajes('Superman', 'Clark Kent', 'Justice League', 1938),
    personajes('Wonder Woman', 'Diana Prince', 'Justice League', 1941),
    personajes('Batman', 'Bruce Wayne', 'Justice League', 1939),
    personajes('Thor', 'Thor Odinson', 'Avengers', 1962),
    personajes('Black Panther', 'T\'Challa', 'Avengers', 1966),
    personajes('Wolverine', 'Logan', 'X-Men', 1974),
    personajes('Flash', 'Barry Allen', 'Justice League', 1956),
    personajes('Green Lantern', 'Hal Jordan', 'Justice League', 1959),
    personajes('Aquaman', 'Arthur Curry', 'Justice League', 1941),
    personajes('Captain America', 'Steve Rogers', 'Avengers', 1941),
    personajes('Doctor Strange', 'Stephen Strange', 'Avengers', 1963),
    personajes('Hawkeye', 'Clint Barton', 'Avengers', 1964),
    personajes('Black Widow', 'Natasha Romanoff', 'Avengers', 1964),
    personajes('Cyclops', 'Scott Summers', 'X-Men', 1963),
    personajes('Jean Grey', 'Jean Grey', 'X-Men', 1963),
    personajes('Rogue', 'Anna Marie', 'X-Men', 1981),
    personajes('Storm', 'Ororo Munroe', 'X-Men', 1975),
    personajes('Beast', 'Hank McCoy', 'X-Men', 1963),
    personajes('Nightcrawler', 'Kurt Wagner', 'X-Men', 1975)
]

for personaje_adicional in personajes_adicionales:
    if lista_personajes.search(personaje_adicional.superheroe, 'superheroe') is None:
        lista_personajes.insert(personaje_adicional, 'superheroe')

   

