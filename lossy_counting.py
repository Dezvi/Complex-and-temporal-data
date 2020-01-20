entrada = ['a','b','c','e','e','b','d','a','b','a','e','e','d','b','d','b','a','b','d','c','e','c','d','e','a','b','d','b','a','c','e','d','d','d','a','c','b','b','e','a','b','b','c','d','a','c','b','e','a','b'
]
epsilon = 0.1
b = epsilon * len(entrada)
import sys
contador = {'a':[0,0], 'b':[0,0], 'c':[0,0], 'd':[0,0], 'e':[0,0]}
for numero_intervalo in range(int(b)):
  numero_intervalo += 1
  if numero_intervalo == 1:
    print("Intervalo 1:")
    print("b = 1")
  else:
    
    print("Intervalo " + str(numero_intervalo) + ":")
  intervalo = entrada[int((numero_intervalo-1)*epsilon*100):int(numero_intervalo*epsilon*100)]
  for valor in intervalo:
    contador[valor][0] += 1
  print(contador)
  sys.stdout.write("b = " + str(numero_intervalo+1) + ", borramos: ")
  primera_vez = True
  for nombre in contador:
    valor = contador[nombre]
    frecuencia_en_intervalo = valor[0]
    numero_intervalo_aniadido = valor[1]
    if frecuencia_en_intervalo + numero_intervalo_aniadido <= numero_intervalo+1:
      if not primera_vez:
        sys.stdout.write(", ")
      primera_vez = False
      sys.stdout.write(nombre)
      contador[nombre][0] = 0
      contador[nombre][1] = numero_intervalo
  print()