import numpy as np

def L_a(v):
    x, y = v
    return np.array([x + y, x - y])

def es_transformacion_lineal(L, dimension):

    u = np.random.rand(dimension)
    v = np.random.rand(dimension)
    if not np.allclose(L(u + v), L(u) + L(v)):
        return False
    

    c = np.random.rand()
    if not np.allclose(L(c * u), c * L(u)):
        return False
    
    return True
print("L(x, y) = (x + y, x - y) es transformación lineal:", es_transformacion_lineal(L_a, 2))
