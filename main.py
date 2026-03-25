import math
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# ENTRADA DE FUNCIONES
# -------------------------

f1_str = input("Ingrese f1(x,y): ")
f2_str = input("Ingrese f2(x,y): ")

def f1(x, y):
    return eval(f1_str, {"x": x, "y": y, "math": math})

def f2(x, y):
    return eval(f2_str, {"x": x, "y": y, "math": math})

# -------------------------
# DERIVADAS NUMÉRICAS
# -------------------------

def deriv_x(f, x, y, h=1e-5):
    return (f(x + h, y) - f(x, y)) / h

def deriv_y(f, x, y, h=1e-5):
    return (f(x, y + h) - f(x, y)) / h

# -------------------------
# DATOS INICIALES
# -------------------------

x0 = float(input("Ingrese valor inicial de x: "))
y0 = float(input("Ingrese valor inicial de y: "))
tol = float(input("Ingrese la tolerancia: "))

# -------------------------
# MÉTODO DE NEWTON
# -------------------------

print("\nIter   X       Y       F1      F2      A       B       C       D       J")
print("-------------------------------------------------------------------------------")

for i in range(20):

    try:
        f1_val = f1(x0, y0)
        f2_val = f2(x0, y0)

        A = deriv_x(f1, x0, y0)
        B = deriv_y(f1, x0, y0)
        C = deriv_x(f2, x0, y0)
        D = deriv_y(f2, x0, y0)

        J = (A * D) - (B * C)

        if J == 0:
            print("Error: Jacobiano = 0")
            break

        x1 = x0 - ((f1_val * D - f2_val * B) / J)
        y1 = y0 - ((f2_val * A - f1_val * C) / J)

        print(f"{i+1:<5} {x0:<7.4f} {y0:<7.4f} {f1_val:<7.4f} {f2_val:<7.4f} {A:<7.4f} {B:<7.4f} {C:<7.4f} {D:<7.4f} {J:<7.4f}")

        error = max(abs(x1 - x0), abs(y1 - y0))

        if error < tol:
            print("\nConvergencia alcanzada.")
            break

        x0, y0 = x1, y1

    except Exception as e:
        print("Error:", e)
        break

print("\nResultado final:")
print("X =", round(x1, 4))
print("Y =", round(y1, 4))


# Valores de x 
x_vals = np.arange(0, 6, 1)

# Listas
y1_vals = []
y2_vals = []

y_base = y1

for x_val in x_vals:
    try:
        y1_vals.append(f1(x_val, y_base))
        y2_vals.append(f2(x_val, y_base))
    except:
        y1_vals.append(None)
        y2_vals.append(None)

# Graficar puntos 
plt.plot(x_vals, y1_vals, marker='o')
plt.plot(x_vals, y2_vals, marker='o')

# Punto solución
plt.scatter(x1, y1, s=80)

plt.title("Gráfica")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.show()