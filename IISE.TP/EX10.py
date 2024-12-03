def fusionner_dicts(dict1, dict2):
    # Créer un dictionnaire de fusion vide
    fusion = dict1.copy()  # On commence par copier dict1 pour ne pas le modifier directement
    
    # Parcourir chaque clé et valeur de dict2
    for key, value in dict2.items():
        if key in fusion:
            # Si la clé existe déjà, on additionne les valeurs
            fusion[key] += value
        else:
            # Sinon, on ajoute la clé et la valeur de dict2
            fusion[key] = value
            
    return fusion
# Tests
dict1 = {"a": 5, "b": 3, "c": 8}
dict2 = {"a": 2, "b": 4, "d": 6}

print(fusionner_dicts(dict1, dict2))  