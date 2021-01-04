from nodo import Nodo
import numpy as np

# Puzle Lineal con busqueda en amplitud
def puzzle_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        compara = nodo.get_datos() == solucion
        if compara.all():
            # solucion encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()
            posibles_direcciones = ["D", "I", "U", "A"]
            for direccion in posibles_direcciones:
                try:
                    nuevo_hijo = intercambio_array(dato_nodo, direccion)    # Cambia nodos_visitados!! Por que!!??
                    hijo_nodo = Nodo(nuevo_hijo)
                    if not hijo_nodo.en_lista(nodos_visitados) and not hijo_nodo.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo_nodo)
                except:
                    pass


def intercambio_array(array, direccion):
    '''Hace el cambio entre dos posiciones del array pasado, solo puede hacer un cero en el array.
    Direcciones posible D = Derecha, I = Izquierda, U = arriba, A = abajo '''
    indice1 = np.where(array == 0)[0][0]    # Buscamos el cero
    indice2 = np.where(array == 0)[1][0]

    if direccion == "D":
        array[indice1][indice2] = array[indice1][indice2+1]
        array[indice1][indice2+1] = 0
    elif direccion == "I":
        array[indice1][indice2] = array[indice1][indice2-1]
        array[indice1][indice2-1] = 0
    elif direccion == "U":
        array[indice1][indice2] = array[indice1-1][indice2]
        array[indice1-1][indice2] = 0
    elif direccion == "A":
        array[indice1][indice2] = array[indice1+1][indice2]
        array[indice1+1][indice2] = 0
    else:  print("Error: fallo en intercambio_array. Letra mal pasada")

    return array


if __name__ == "__main__":
    estado_inicial = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    solucion = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    nodo_solucion = puzzle_BFS(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    compara = nodo.get_padre() == None
    while compara != True:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)


