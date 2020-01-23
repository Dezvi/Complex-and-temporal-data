class Node: 
    def __init__(self, nombre, cantidad=None, padre=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.padre = padre
        self.hijos = []
        self.profundidad = 0

def update_tree(padre, compra):
    if(compra == padre.nombre):
        padre.cantidad += 1
        return padre
    encontrado = False
    for hijo in padre.hijos:
        if hijo.nombre == compra:
            padre = hijo
            padre.cantidad += 1
            encontrado = True
    if not encontrado:
        hijo = Node(compra, 1, padre)
        padre.hijos.append(hijo)
        padre = hijo
    return padre

def arbol_vis(nodo, nivel="", nivel1=0):
    print(nivel + str(nodo.nombre) + ", " + str(nodo.cantidad))
    for hijo in nodo.hijos:
        arbol_vis(hijo, nivel+"____ ")
    return
clientes = []
clientes.append(['C','D','A','B'])
clientes.append(['B','C','A'])
clientes.append(['D','A'])
clientes.append(['E','B','A'])
clientes.append(['C','D','A'])
clientes.append(['E','B','C'])
clientes.append(['A','B','D','E'])
clientes.append(['B','C','E'])

conteo = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}

for cliente in clientes:
    for compra in cliente:
        conteo[compra] += 1 

orden_compras = {k: v for k, v in sorted(conteo.items(), key=lambda item: item[1])}

compras_ordenadas = [list] * len(clientes)

for cliente_idx, cliente  in enumerate(clientes):
    compras_ordenadas[cliente_idx] = [' ']*len(cliente)
    orden_compra_idx = 0
    for orden_compras_key in orden_compras:
        if orden_compras_key in cliente: 
          compras_ordenadas[cliente_idx][orden_compra_idx] = orden_compras_key
          orden_compra_idx += 1 

print(compras_ordenadas)

raiz = Node("null")
padre = raiz


for cliente in compras_ordenadas:
    for idx, compra_ordenada  in enumerate(cliente):
        print("Padre: " + str(padre.nombre) + ", cantidad: " + str(padre.cantidad) + ", compra: " + str(compra_ordenada))
        padre = update_tree(padre, compra_ordenada)
    padre = raiz

arbol_vis(raiz)