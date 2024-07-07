import numpy as np
from sympy import Matrix, symbols
p1 = np.array([1, -2, 5])   
p2 = np.array([2, -3, 0])
p3 = np.array([0, 1, 3])   
v = np.array([1, 4, -3])    


A = np.column_stack((p1, p2, p3))
b = v


augmented_matrix = np.column_stack((A, b))


sympy_matrix = Matrix(augmented_matrix)
reduced_matrix = sympy_matrix.rref()[0]


rank_A = np.linalg.matrix_rank(A)
rank_augmented = np.linalg.matrix_rank(augmented_matrix)

x, y, z = symbols('x y z')
equations = A @ [x, y, z] - b

print("Sistema de ecuaciones planteado:")
for eq in equations:
    print(eq, "= 0")

print("\nMatriz aumentada:")
print(sympy_matrix)

print("\nMatriz aumentada en forma escalonada:")
print(reduced_matrix)


if rank_A == rank_augmented:
    if rank_A == A.shape[1]:
      
        solution = np.linalg.solve(A, b)
        print("\nEl sistema tiene una solución única:")
        print("x =", solution[0])
        print("y =", solution[1])
        print("z =", solution[2])
        print("Por lo tanto, v es una combinación lineal de p1, p2 y p3.")
    else:
    
        print("\nEl sistema tiene infinitas soluciones.")
        print("Por lo tanto, v es una combinación lineal de p1, p2 y p3.")
else:
 
    print("\nEl sistema no tiene solución.")
    print("Por lo tanto, v no es una combinación lineal de p1, p2 y p3.")

