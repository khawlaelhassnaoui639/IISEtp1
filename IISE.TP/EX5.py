def factorielle(n):
    # Cas de base : la factorielle de 0 est 1
    if n == 0:
        return 1
    # Cas récursif : n * factorielle(n-1)
    else:
        return n * factorielle(n - 1)
# Tests
print(factorielle(5))