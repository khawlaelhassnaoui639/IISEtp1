def max_tuple(t):
    # On vérifie si le tuple est vide pour éviter une erreur
    if len(t) == 0:
        return None  # Ou une valeur indiquant que le tuple est vide
    
    # On initialise le plus grand nombre avec le premier élément du tuple
    max_val = t[0]
    
    # On parcourt le tuple et on met à jour max_val si on trouve un élément plus grand
    for num in t:
        if num > max_val:
            max_val = num
    
    return max_val
# Tests
print(max_tuple((1, 2, 3, 4)))       # Devrait afficher 4
print(max_tuple((0, -1, 5, 3)))      # Devrait afficher 5