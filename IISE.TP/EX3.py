def intersection(ensemble1, ensemble2):
    # Créer un nouvel ensemble pour stocker l'intersection
    resultat = set()
    
    # Parcourir chaque élément du premier ensemble
    for element in ensemble1:
        # Si l'élément est aussi dans le deuxième ensemble, on l'ajoute à l'intersection
        if element in ensemble2:
            resultat.add(element)
    
    return resultat
# Tests
print(intersection({1, 2, 3}, {2, 3, 4}))  # Devrait afficher {2, 3}
print(intersection({1, 5, 7}, {7, 8, 9}))  # Devrait afficher {7}