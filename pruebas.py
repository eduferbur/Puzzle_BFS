import numpy as np
# COMPARACIÓN DE DOS ARRAYS
x = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
y = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
comparacion = x == y  # Crea una matrix comparando 1 a 1: [[ True  True  True]...

if (comparacion.all()):     print('Los arrays son iguales')
else:                       print("Algo es diferente")

if (comparacion.any()):     print("Algun numero es igual")
else:                       print("Todos los nros son diferentes")

array_a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(array_a[1][1])    # out: 7

resultado = np.where(x == 0)
print("eeee", np.where(x == 0)[1][0])
