import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Eksempeldata
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 4.2, 7.3, 12.2, 20.1])

# Modell: a * e^(b*x)
def exp_model(x, a, b):
    return a * np.exp(b * x)

# Tilpasning
params, _ = curve_fit(exp_model, x, y)
a, b = params

# Plotting
plt.scatter(x, y, label="Data")
plt.plot(x, exp_model(x, a, b), color='green', label=f"y = {a:.2f}e^({b:.2f}x)")
plt.title("Eksponentiell regresjon")
plt.legend()
plt.grid()
plt.show()