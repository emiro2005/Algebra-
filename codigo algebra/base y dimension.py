import numpy as np
v1 = np.array([0, 0])
v2 = np.array([1, 2])
v3 = np.array([2, 4])
matriz = np.column_stack([v1, v2, v3])
rango = np.linalg.matrix_rank(matriz)
base = [v2, v3] if rango == 2 else [v2]
print("Base:", base)
print("Dimensión:", rango)
