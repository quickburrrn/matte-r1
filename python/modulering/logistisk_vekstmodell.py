import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Eksempeldata: tid og populasjon
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([2, 5, 15, 40, 70, 90, 98])

# Logistisk modell
def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# Tilpasning
params, _ = curve_fit(logistic, x, y, p0=[100, 1, 3])
L, k, x0 = params

# Plotting
plt.scatter(x, y, label="Data")
plt.plot(x, logistic(x, L, k, x0), color='purple', label=f"Logistisk modell")
plt.title("Logistisk vekst")
plt.legend()
plt.grid()
plt.show()
