import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

x = symbols('x')
f = x**2
g = 2*x + 3

# Løs ligningen f(x) = g(x)
løsning = solve(Eq(f, g), x)
print("Skjæringspunkter:")
for x_løs in løsning:
    y = f.subs(x, x_løs)
    print(f"x = {x_løs}, y = {y}")

# Tegn grafene
x_vals = np.linspace(-2, 4, 400)
plt.plot(x_vals, x_vals**2, label="f(x) = x²")
plt.plot(x_vals, 2*x_vals + 3, label="g(x) = 2x + 3")
plt.legend()
plt.grid(True)
plt.title("Skjæringspunkt mellom to grafer")
plt.show()