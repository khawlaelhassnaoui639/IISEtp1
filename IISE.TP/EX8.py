def somme_varargs(*args):
    total = 0
    for arg in args:
        total += arg
    return total
# Tests
print(somme_varargs(1, 2, 3))
print(somme_varargs(10, -5, 15)) 