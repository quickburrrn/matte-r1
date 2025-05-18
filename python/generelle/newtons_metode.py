# Finner nullpunktet til en funksjon med newtons metode

def f(x):
    # Dette er funksjonen som du skal finne nullpunkt til
    return x**2 - 2

def df(x):
    # Deriver funksjonen og skriv det her
    return 2*x

def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

rot = newton(f, df, x0=1)
print(f"Nullpunkt: {rot:.10f}")  # ca. √2