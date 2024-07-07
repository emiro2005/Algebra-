import sympy as sp
def suma(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def multiplicacion(c, v):
    return (c * v[0], c * v[1], 0)

def espacio():
    
    x1, y1, z1, x2, y2, z2, x3, y3, z3, c, d = sp.symbols('x1 y1 z1 x2 y2 z2 x3 y3 z3 c d')

    
    v1 = (x1, y1, z1)
    v2 = (x2, y2, z2)
    v3 = (x3, y3, z3)
    v0 = (0, 0, 0)

    
    suma_v1_v2 = suma(v1, v2)
    if not suma_v1_v2:
        print("Falló la cerradura bajo la suma")
        return False

    
    if suma(v1, v2) != suma(v2, v1):
        print("Falló la conmutatividad de la suma")
        return False

   
    if suma(v1, suma(v2, v3)) != suma(suma(v1, v2), v3):
        print("Falló la asociatividad de la suma")
        return False

   
    if suma(v1, v0) != v1:
        print("Falló la existencia del elemento neutro")
        return False

    
    opuesto_v1 = (-v1[0], -v1[1], -v1[2])
    if suma(v1, opuesto_v1) != v0:
        print("Falló la existencia del elemento opuesto")
        return False

    
    if multiplicacion(c, v1) is None:
        print("Falló la cerradura bajo la multiplicación por un escalar")
        return False

    
    if multiplicacion(c, suma(v1, v2)) != suma(multiplicacion(c, v1), multiplicacion(c, v2)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma vectorial")
        return False

  
    if multiplicacion(c + d, v1) != suma(multiplicacion(c, v1), multiplicacion(d, v1)):
        print("Falló la distributividad de la multiplicación escalar respecto a la suma escalar")
        return False

   
    if multiplicacion(c * d, v1) != multiplicacion(c, multiplicacion(d, v1)):
        print("Falló la asociatividad de la multiplicación escalar")
        return False

    
    if multiplicacion(1, v1) != (v1[0], v1[1], 0):
        print("Falló la existencia del elemento unidad")
        return False

    return True


print(espacio()) 

