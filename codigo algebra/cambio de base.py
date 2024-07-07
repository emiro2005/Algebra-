import numpy as np

B = np.array([[-1, 4], [4, -1]])

x_B = np.array([-2, 3])

x_estandar = np.dot(B, x_B)

print("Vector en la base estándar:", x_estandar)
