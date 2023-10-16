from arbol_binario import BinaryTree


datos = [
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Medusa2', 'derrotado': 'Zeus'},
    {'name': 'Tifon', 'derrotado': 'Zeus'},
    {'name': 'Leon Nimea', 'derrotado': 'Heracles'},
    {'name': 'Hydrade lerna', 'derrotado': 'Heracles'},
    {'name': 'Otro', 'derrotado': 'Heracles'},
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tore de Creta', 'derrotado': None},
    {'name': 'Talos', 'derrotado': "Apolo"},
    {'name': 'Ceto3', 'derrotado': "Apolo"},
]

criaturas_tree = BinaryTree()

for criatura in datos:
    criaturas_tree.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})
#
#criaturas.inorden_add_field()
#
criaturas_tree.inordennmm()
print()

# b
#criaturas.inorden_add_field()
#criaturas.inorden()
#print()

# c
buscado = input('Ingrese la criatura que desea buscar: ')
busca = criaturas_tree.search(buscado)

if busca:
    print('Se ha encontrado a ' + buscado)
else:
    print(buscado,'no se ha encontrado en la lista')
print()

# i
#buscado = input('Ingrese la criatura que desea buscar: ')
#criaturas.search_by_coincidence(buscado)

# j
#buscado = criaturas.search('Basilisco')
#if buscado is not None:
#    criaturas.delete_node('Basilisco')
#buscado = criaturas.search('Sirenas')
#if buscado is not None:
#    criaturas.delete_node('Sirenas')

#dic_ranking = {}
#criaturas.inorden_ranking(dic_ranking)
#
#print(dic_ranking)
#
#
#def order_por(item):
#    print(item)
#    return item[1]
#
#ordenados = list(dic_ranking.items())
#ordenados.sort(key=order_por, reverse=True)
#print(ordenados[:3])
#
#
#pos = criaturas.search()
#if pos is not None:
#    pos.other_values['capturado'] = 'Heracles'
#

#criaturas.search('tal')