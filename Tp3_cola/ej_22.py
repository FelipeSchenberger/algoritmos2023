personajes = [
    {'nombre':'Steve Rogers','superheroe':'Capitan America','sexo':'M'},
    {'nombre':'Peter Parker','superheroe':'Spider-Man','sexo':'M'},
    {'nombre':'Kate Bishop','superheroe':'Ojo de halcon','sexo':'F'},
    {'nombre':'Carol Danvers','superheroe':'Capitana Marvel','sexo':'F'},
    {'nombre':'Stephen Strange','superheroe':'Doctor Strange','sexo':'M'},
    {'nombre':'Scott Lang','superheroe':'Ant-Man','sexo':'M'}
]
nombres_sexo_f = []
nombres_sexo_m = []
empiezan_con_s = []


for persona in personajes:
    if persona['superheroe'] == 'Capitana Marvel':
        nombre = persona['nombre']
        
    if persona['sexo'] == 'F':
        nombre_sexo_f = persona['nombre']
        nombres_sexo_f.append(nombre_sexo_f)
    
    if persona['sexo'] == 'M':
        nombre_sexo_m = persona['nombre']
        nombres_sexo_m.append(nombre_sexo_m)
    
    if persona['nombre'] == 'Scott Lang':
        superheroe = persona['superheroe']

    if persona['nombre'].startswith('S') or persona['superheroe'].startswith('S'):
        empieza_con_s = persona['nombre'],persona['superheroe'],persona['sexo']
        empiezan_con_s.append(empieza_con_s)

    if persona['nombre'] == 'Carol Danvers':
        carol = persona['superheroe']

print(f'a) {nombre}')
print(f'b) {nombres_sexo_f}')
print(f'c) {nombres_sexo_m}')
print(f'd) {superheroe}')
print(f'e) {empiezan_con_s}')
print(f'f) Carol Danvers se encuentra en la cola y su nombre de superheroe es {carol}')
