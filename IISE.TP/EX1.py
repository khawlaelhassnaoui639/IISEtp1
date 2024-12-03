def somme_liste(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

# Tests
print(somme_liste([1, 2, 3, 4]))
print(somme_liste([0, -1, 5, 3]))
