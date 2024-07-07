import sympy as sp

def suma(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return (x1 + x2, y1 + y2, 2)

def multiplicacion(c, v):
    x, y, z = v
    return (c * x, c * y, 2)

def subespacio():
    x1, y1, x2, y2, c = sp.symbols('x1 y1 x2 y2 c')

    v1 = (2, 0, 2) 
    v2 = (0, 0, 2)  
    v0 = (0, 0, 2)
    
    suma_v1_v2 = suma(v1, v2)
    if suma_v1_v2[2] != 2:
        print("Falló la cerradura bajo la suma")
        return False
    
    escalar_v1 = multiplicacion(c, v1)
    if escalar_v1[2] != 2:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False    
        
    if v0 != (0, 0, 2):
        print("No contiene el vector cero")
        return False

    return False

print(subespacio())
