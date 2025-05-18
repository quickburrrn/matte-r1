import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Eksempeldata (tid, verdi)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])

# Regresjon
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Funksjonen
def lin_reg(x):
    return slope * x + intercept

# Plotting
plt.scatter(x, y, label="Data")
plt.plot(x, lin_reg(x), color='red', label=f"y = {slope:.2f}x + {intercept:.2f}")
plt.title("Lineær regresjon")
plt.legend()
plt.grid()
plt.show()
