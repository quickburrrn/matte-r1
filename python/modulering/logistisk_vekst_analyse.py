# Dette er en oppgave hvor man skal lage en logisisk modell med et datasett
from pylab import *
from scipy.optimize import curve_fit

# Målinger fra Troltinden på Anderøya
måned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
makstemp = [2.9, 3.7, 3.6, 8.6, 9.5, 18.6, 24.5, 18.0, 15.8, 12.2, 7.3, 3.8]

# Definerer funksjonen T
def T(x, A, phi, d):
    return A*sin(0.524*x + phi) + d

# Bestemmer konstantene
[A, phi, d] = curve_fit(T, måned, makstemp)[0] # curve_fit(funk.navn, x-var, y-var)
print('A =', round(A, 2))
print('phi =', round(phi, 2))
print('d =', round(d, 2))
print(f'T(x) = {A:.2f}*sin(0.524*x + {phi:.2f}) + {d:.2f}')

plot(måned, makstemp, 'o')
xlabel('Måned')
ylabel('Makstemp (C)')
x = linspace(0, 12, 1000)
plot(x, T(x, A, phi, d), 'r')
show()