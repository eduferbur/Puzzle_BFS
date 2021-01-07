from nodo import Nodo
import numpy as np
import copy

# Puzle Lineal con busqueda en amplitud
def puzzle_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # nodo = nodos_frontera.pop(0)
        # # extraer nodo y añadirlo a visitados
        # nodos_visitados.append(nodo)

        nodo = nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))

        # Hasta aquí todo es igual que en el ejemplo.
        compara = nodo.get_datos() == solucion # Como es un array de Numpy, así lo comparamos
        if compara.all():
            # solucion encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            posibles_direcciones = ["D", "I", "U", "A"] # Posibles movimientos de la función intercambio_array, ver en la función
            lista_hijos = []    # Aquí vamos añadiendo los hijos que vamos creando.
            for direccion in posibles_direcciones:
                dato_nodo = copy.copy(nodo.get_datos())
                '''Hago un try porque le voy a pedir que haga todas las posibles combinaciones, 
                Si me salgo del índice de la matrix, dará un indexerror, pero seguirá la con los siguientes movimientos'''
                try:
                    un_hijo = intercambio_array(dato_nodo, direccion)
                    hijo = copy.copy(Nodo(un_hijo))
                    lista_hijos.append(hijo)
                    if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo)

                except:
                    pass
            nodo.set_hijos(lista_hijos)    # Añadimos la lista de hijos al nodo padre.


def intercambio_array(array, direccion):
    '''Hace el cambio entre dos posiciones del array pasado, solo puede hacer un cero en el array.
    Direcciones posible D = Derecha, I = Izquierda, U = arriba, A = abajo '''
    indice1 = np.where(array == 0)[0][0]    # Buscamos el cero
    indice2 = np.where(array == 0)[1][0]

    if direccion == "D":    # Intercambiamos el cero con el número a la derecha.
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

    return array    # Una vez hecho el cambio, enviamos el array modificado


if __name__ == "__main__":
    estado_inicial = np.array([[8, 3, 2], [1, 6, 4], [7, 0, 5]])
    solucion = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    nodo_solucion = puzzle_BFS(estado_inicial, solucion)
    if nodo_solucion == None:
        print("Algo falló en la función")
    else:
        # mostrar resultado
        resultado = []
        nodo = copy.copy(nodo_solucion)
        compara = nodo.get_padre() == None
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            if nodo.get_padre() == None:
                break
            else:
                nodo = nodo.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)


