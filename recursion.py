def factorial(a):
    if a <= 0:
        return 1
    return factorial(a-1)*a
b = factorial(5)
print(b)
    