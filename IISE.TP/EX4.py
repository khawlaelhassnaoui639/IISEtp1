def compte_occurences(liste):
    # Initialisation d'un dictionnaire vide
    occurrences = {}
    
    # Parcours de chaque mot dans la liste
    for mot in liste:
        # Si le mot est déjà dans le dictionnaire, on incrémente sa valeur
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            # Sinon, on l'ajoute avec une valeur de 1
            occurrences[mot] = 1
    
    return occurrences
# Tests
print(compte_occurences(["chat", "chien", "chat", "oiseau", "chat"]))  