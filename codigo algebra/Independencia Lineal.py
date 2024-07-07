import numpy as np
v1 = np.array([1, 0])
v2 = np.array([1, 1])
v3 = np.array([2, -1])
matriz = np.array([v1, v2, v3])
rango = np.linalg.matrix_rank(matriz)
if rango < len(matriz):
    print("El conjunto S es linealmente dependiente.")
else:
    print("El conjunto S no es linealmente independiente.")


