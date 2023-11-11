from grafo2 import Grafo
from random import randint

print ("\nEJERCICIO 14:")
grafo = Grafo(dirigido=False)
print ("\nA")
grafo.insert_vertice("banioUno")#
grafo.insert_vertice("banioDos ")#
grafo.insert_vertice("cochera")#
grafo.insert_vertice("cocina")#
grafo.insert_vertice("comedor")#
grafo.insert_vertice("habitacionUno")#
grafo.insert_vertice("habitacionDos")#
grafo.insert_vertice("patio")#
grafo.insert_vertice("salaDeEstar")#
grafo.insert_vertice("terraza")#
grafo.insert_vertice("quincho")#
print ("Cargados")

print ("\nB:")
grafo.insert_arist("banioUno","banioDos", randint(1, 30))#
grafo.insert_arist("banioUno", "habitacionUno", randint(1, 15))#tres
grafo.insert_arist("banioUno", "salaDeEstar", randint(1, 20))

grafo.insert_arist("banioDos", "habitacionDos", randint (1, 20))#dos + 1 que tiene con banioUno
grafo.insert_arist("banioDos","terraza", randint(1, 10))

grafo.insert_arist("habitacionUno", "salaDeEstar", randint(1, 15)) #cuatro + 1 que tiene con banioUno
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))
grafo.insert_arist("habitacionUno", "comedor", randint(1, 20))
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))

grafo.insert_arist("habitacionDos", "terraza", randint (1, 15))
grafo.insert_arist("habitacionDos", "quincho", randint (1, 35))#tres + 2 que tiene en (1 en habitacionuno, 1 en banioDos)
grafo.insert_arist("habitacionDos", "patio", randint(1, 30))

grafo.insert_arist("salaDeEstar", "patio", randint(1, 15))#uno + 2 que tiene en (1 en habitacionUno y 1 en banioUno)

grafo.insert_arist("patio", "quincho", randint(1, 10))#uno + 2 que tiene en (1 en salabeEstar y 1 en habitacionDos)

grafo.insert_arist ("quincho", "cochera", randint(1, 30))#uno + 2 que tiene en (1 en habitacionDos y 1 en patio)

grafo.insert_arist("terraza", "cochera", randint(1, 30))#uno + 2 que tiene en (1 en banioDos y 1 en habitacionDos)

grafo.insert_arist("cochera", "comedor", randint(1, 20))#uno + 2 que tiene en (1 en terraza, 1 en quincho)

grafo.insert_arist("cocina", "patio", randint(1, 20))
grafo.insert_arist("cocina", "comedor", randint(1, 10))#tres
grafo.insert_arist("cocina", "salaDeEstar", randint (1, 20))
#comedor ya tiene 3 (1 en cocina, 1 en cochera, 1 en habitacionUno)

print ("Cargados")
print ("\nC:")
number = []
for i in range(1, 31):
    number.append(str(i))

acu = 0
for arbol in grafo.kruskal():
    for nodo in arbol.split(';'):
        acu += int(nodo.split('-')[-1])

print(f"Se necesitaran {acu} metros.")

print("\nD: ")
ori = 'habitacionUno'
des = 'salaDeEstar'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des)):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value [2]