import numpy as np
import matplotlib.pyplot as plt

# Definições do problema
a, b = 0, 1        # Intervalo
ya, yb = 0, 0      # Condições de contorno
h = 0.25           # Passo
n = int((b - a)/h) # Número de subintervalos
x = np.linspace(a, b, n+1)

# Matriz e vetor do sistema
A = np.zeros((n-1, n-1))
d = np.zeros(n-1)

for i in range(1, n):
    xi = a + i*h
    
    # coeficientes da equação transformada
    # y'' - 3x*y' + y = x
    # diferença finita central
    p = -3*xi/2
    q = 1
    r = xi
    
    # coeficientes para matriz tridiagonal
    A[i-1, i-1] = -2/h**2 + q
    if i-1 > 0:
        A[i-1, i-2] = 1/h**2 - p/(2*h)
    if i < n-1:
        A[i-1, i] = 1/h**2 + p/(2*h)
    
    d[i-1] = r

# Resolve o sistema
y_internal = np.linalg.solve(A, d)

# Junta condições de contorno
y = np.concatenate(([ya], y_internal, [yb]))

# Exibe resultados
for xi, yi in zip(x, y):
    print(f"x={xi:.2f}, y={yi:.5f}")

# Gráfico
plt.plot(x, y, 'o-', label="Solução Numérica (DF)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Equação diferencial - Diferenças Finitas")
plt.legend()
plt.grid(True)
plt.show()
