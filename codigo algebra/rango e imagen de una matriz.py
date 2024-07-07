import numpy as np


matriz = np.array([[1, 2, 3]])

rango = np.linalg.matrix_rank(matriz)


_, columnas_independientes = np.linalg.qr(matriz)


print("Rango:", rango)
print("Imagen de la matriz:", columnas_independientes)
