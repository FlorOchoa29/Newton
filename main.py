import math
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# ENTRADA DE FUNCIONES
# -------------------------

f1_str = 'x**2+y**2-4*x-6*y+11'
f2_str = 'x**2+y**2-6*x-8*y+21'

def parse_expr(expr):
    """Convierte notación matemática a Python: x^2 -> x**2, 4x -> 4*x"""
    import re
    expr = expr.replace('^', '**')
  
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    return expr

def f1(x, y):
    return eval(parse_expr(f1_str), {"x": x, "y": y, "math": math})

def f2(x, y):
    return eval(parse_expr(f2_str), {"x": x, "y": y, "math": math})

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

x0 = 2.0
y0 = 1.0
tol = 0.001
x1, y1 = x0, y0

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

        if abs(J) < 1e-12:
            print("Error: Jacobiano ≈ 0")
            break

        x1 = x0 - ((f1_val * D - f2_val * B) / J)
        y1 = y0 - ((f2_val * A - f1_val * C) / J)

        print(f"{i+1:<5} {x0:<7.4f} {y0:<7.4f} {f1_val:<7.4f} {f2_val:<7.4f} "
              f"{A:<7.4f} {B:<7.4f} {C:<7.4f} {D:<7.4f} {J:<7.4f}")

        error = max(abs(x1 - x0), abs(y1 - y0))

        x0, y0 = x1, y1

        if error < tol:
            print("\nConvergencia alcanzada.")
            break

    except Exception as e:
        print("Error:", e)
        break

print("\nResultado final:")
print("X =", round(x1, 4))
print("Y =", round(y1, 4))

# -------------------------
# GRÁFICA
# -------------------------

x_vals = np.linspace(0, 6, 200)
y_base = y1

y1_vals = [f1(xv, y_base) for xv in x_vals]
y2_vals = [f2(xv, y_base) for xv in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y1_vals, label='f1(x, y*)')
plt.plot(x_vals, y2_vals, label='f2(x, y*)')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter([x1], [0], color='red', zorder=5, label=f'Solución ({round(x1,4)}, {round(y1,4)})')

plt.title("Método de Newton - Sistema de ecuaciones")
plt.xlabel("x")
plt.ylabel("f(x, y*)")
plt.legend()
plt.grid()
plt.show()