'''
Dada una lista con nombres de personajes de la saga de Avengers
ordenados por nombre del superhéroes, de los cuales se conoce:
nombre del superhéroe, nombre del personaje (puede ser vacio),
grupo al que (perteneces puede ser vacio), año de aparición, por
ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
Resolver las siguientes tareas:
a. Determinar si “Capitana Marvel” está en la lista y mostrar su
nombre de personaje;
b. Almacenar los superhéroes que pertenezcan al grupo
“Guardianes de la galaxia” en una cola e indicar cuantos son.
c. Mostrar de manera descendente los superhéroes que
pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
la galaxia”.
d. Listar los superhéroes que tengan nombre de personajes cuyo
año de aparición sea posterior a 1960.
e. Hemos detectado que la superhéroe “Black Widow” está mal
cargada por un error de tipeo, figura como “Vlanck Widow”,
modifique dicho superhéroe para solucionar este problema.
f. Dada una lista auxiliar con los siguientes personajes (‘Black
Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
información), agregarlos a la lista principal en el caso de no
estar cargados.
g. Mostrar todos los personajes que comienzan con C, P o S.
h. Cargue al menos 20 superheroes a la lista. '''

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')

class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def search_r(self, search_value, first, last, criterio=None):
        middle = (first + last) // 2
        if first > last:
            return None
        elif search_value == criterio_comparacion(self.__elements[middle], criterio):
            return middle
        elif search_value > criterio_comparacion(self.__elements[middle], criterio):
            return self.search_r(search_value, middle+1, last, criterio)
        else:
            return self.search_r(search_value, first, middle-1, criterio)
 
    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=True):
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]
            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def set_value(self, value, new_value, criterio=None):
        pos = self.search(value, criterio)
        if pos is not None:
            value = self.delete(value)
            self.insert(new_value, criterio)

class personajes:
    def __init__(self, superheroe, nombre, grupo, aparicion):
        self.nombre = superheroe
        self.estatura = nombre
        self.edad = grupo
        self.genero = aparicion
        
    def __str__(self):
        return f'{self.superheroe} - {self.nombre} - {self.grupo} - {self.aparicion}'
    
pj1 = personajes('Capitana Marvel', 'Carol Danvers', 'Avengers', 1968)
pj2 = personajes('Star Lord', 'Peter Quill', 'Guardianes de la galaxia', 1976)
pj3 = personajes('Hulk', 'Bruce Banner', 'Avengers', 1962)
pj4 = personajes('Vlanck Widow', 'Natasha Romanoff', 'Avengers', 1964)
pj5 = personajes('Iron Man', 'Tony Stark', 'Avengers', 1963)

lista = Lista()


capitana_marvel = "Capitana Marvel"
posicion = lista.search(capitana_marvel, criterio="nombre")
if posicion is not None:
    personaje = lista.get_element_by_index(posicion)
    print(f"El nombre de personaje de {capitana_marvel} es {personaje.nombre}.")


guardianes_galaxia = Lista()
for personaje in lista._Lista__elements:
    if personaje.grupo == "Guardianes de la galaxia":
        guardianes_galaxia.insert(personaje)

cantidad_guardianes = guardianes_galaxia.size()
print(f"Hay {cantidad_guardianes} superhéroes en el grupo 'Guardianes de la galaxia'.")


fantasticos_guardianes = Lista()
for personaje in lista._Lista__elements:
    if personaje.grupo == "Los cuatro fantásticos" or personaje.grupo == "Guardianes de la galaxia":
        fantasticos_guardianes.insert(personaje)

fantasticos_guardianes.order_by(criterio="nombre", reverse=False)
fantasticos_guardianes.barrido()


for personaje in lista._Lista__elements:
    if personaje.aparicion > 1960:
        print(personaje.nombre)


lista.set_value("Vlanck Widow", personajes("Black Widow", "", "", 0), criterio="nombre")


lista_auxiliar = [
    personajes("Black Cat", "", "", 0),
    personajes("Hulk", "", "", 0),
    personajes("Rocket Racoonn", "", "", 0),
    personajes("Loki", "", "", 0)
]

for personaje_auxiliar in lista_auxiliar:
    if lista.search(personaje_auxiliar.nombre, criterio="nombre") is None:
        lista.insert(personaje_auxiliar)


for personaje in lista._Lista__elements:
    if personaje.nombre.startswith(("C", "P", "S")):
        print(personaje.nombre)


superheroes = [
    personajes("Spider-Man", "", "", 0),
    personajes("Superman", "", "", 0),
    personajes("Wonder Woman", "", "", 0),
    personajes("Batman", "", "", 0),
    personajes("Flash", "", "", 0),
    personajes("Linterna Verde", "", "", 0),
    personajes("Aquaman", "", "", 0),
    personajes("Thor", "", "", 0),
    personajes("Hawkeye", "", "", 0),
    personajes("Black Panther", "", "", 0),
    personajes("Iron Fist", "", "", 0),
    personajes("Doctor Strange", "", "", 0),
    personajes("Wolverine", "", "", 0),
    personajes("Tormenta", "", "", 0),
    personajes("Ciclope", "", "", 0),
    personajes("Green Arrow", "", "", 0),
    personajes("Profesor X", "", "", 0),
    personajes("Rocket", "", "", 0),
    personajes("Bestia", "", "", 0),
    personajes("Luke Cage", "", "", 0),
    personajes("Punisher", "", "", 0)
]

for heroe in superheroes:
    if heroe.nombre not in ["Captain Marvel", "Iron Man", "Hulk", "Black Widow", "Star Lord"]:
        lista.insert(heroe)


print(f"La lista contiene {lista.size()} superhéroes.")




