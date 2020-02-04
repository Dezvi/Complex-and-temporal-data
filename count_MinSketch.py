import numpy as np

datos = [('A',1),('B',2),('C',5),('B',4),('E',8),('D',7),('C',8),('F',5),('G',10),('C',5),('H',3)]

print("Datos:")
print(datos)

hash_codes = [(5,6,1),(1,3,4),(2,4,5),(1,3,2),(2,4,6),(6,1,3),(2,5,3),(3,4,6)]

print("Hash:")
print(hash_codes)

index_pos = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7}

tabla = np.zeros((3,6))

total = np.zeros((8))

for dato in datos:
  for idx, fila in enumerate(tabla):
    fila[hash_codes[index_pos[dato[0]]][idx]-1] += dato[1]
  total[index_pos[dato[0]]] += dato[1]

print("Tabla:")
print(tabla)

resultados = []

for item in index_pos:
  resultados.append(min(tabla[0,hash_codes[index_pos[item]][0]-1], tabla[1,hash_codes[index_pos[item]][1]-1], tabla[2,hash_codes[index_pos[item]][2]-1]))

errores = np.asarray(resultados) - total

for idx, error in enumerate(errores):
  if(error != 0):
    print("Error en item: " + chr(65+idx) + " valor real: " + str(total[idx]) + " valor calculado: " + str(resultados[idx]))
  else:
    print("Item: " + chr(65+idx) + " perfecto" + " valor real: " + str(total[idx]) + " valor calculado: " + str(resultados[idx]))

