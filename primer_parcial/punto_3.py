'''
Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
cual se almacenaban en una pila en cada misión de caza que
emprendió (con la siguiente información planeta visitado, a quien
capturado, costo de la recompensa), resolver las siguientes
actividades:
a. Mostrar los planetas visitados en el orden hizo las misiones.
b. Determinar cuántos créditos galácticos recaudo en total.
c. Determinar el número de la misión en que capturo a Han Solo
y en que planeta fue, suponga que dicha misión está cargada.'''

from pila1 import Pila

bitacora = Pila()

bitacora.push(('Planeta1', 'Capturado1', 226))
bitacora.push(('Planeta2', 'Capturado2', 129))
bitacora.push(('Planeta3', 'Capturado3', 676))
bitacora.push(('Planeta4', 'Capturado4', 123))
bitacora.push(('Planeta5', 'Han Solo', 830))  

#a
print('Planetas visitados en el orden de las misiones:')
while bitacora.size() > 0:
    mision = bitacora.pop()
    planeta = mision[0]
    print(planeta)
print()

#b
bitacora = Pila()  
suma_creditos = 0

bitacora.push(('Planeta1', 'Capturado1', 226))
bitacora.push(('Planeta2', 'Capturado2', 129))
bitacora.push(('Planeta3', 'Capturado3', 676))
bitacora.push(('Planeta4', 'Capturado4', 123))
bitacora.push(('Planeta5', 'Han Solo', 830))

while bitacora.size() > 0:
    mision = bitacora.pop()
    creditos = mision[2]
    suma_creditos += creditos
print('Total de créditos galácticos recaudados:', suma_creditos)
print()

#c
bitacora = Pila() 
numero_mision = 0
planeta_captura = ''

bitacora.push(('Planeta1', 'Capturado1', 226))
bitacora.push(('Planeta2', 'Capturado2', 129))
bitacora.push(('Planeta3', 'Capturado3', 676))
bitacora.push(('Planeta4', 'Capturado4', 123))
bitacora.push(('Planeta5', 'Han Solo', 830))

while bitacora.size() > 0:
    numero_mision += 1
    mision = bitacora.pop()
    planeta = mision[0]
    capturado = mision[1]
    
    if capturado == 'Han Solo':
        planeta_captura = planeta
        break

print('Misión en la que capturó a Han Solo:', numero_mision)
print('Planeta donde capturó a Han Solo:', planeta_captura)