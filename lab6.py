import math
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

x = int(input("Please enter a number: "))


print(f"factorial of {x} is {factorial(x)}")


step_sine = lambda n, x: ((-1) ** n) * ((x ** (2 * n + 1)) / factorial(2 * n + 1))


def sine_x(x, n):
    x = math.radians(x)
    sine_sum = 0
    for i in range(n):
        sine_sum += step_sine(i, x)
    return sine_sum

x = float(input("enter the value of x (in degrees): "))
n = int(input("enter the number of terms (n): "))
print(f"sin({x}) calculated using {n} terms: {sine_x(x, n)}")


h_sum = 0


def harmonic_series(n):
    global h_sum
    if n == 1:
        h_sum += 1
    else:
        h_sum += 1 / n
        harmonic_series(n - 1)


n = int(input("enter the value of n for harmonic series: "))
harmonic_series(n)
print(f"the harmonic series sum for n={n} is {h_sum}")
