def analyse_texte(texte):
    # Compter les mots en séparant le texte par les espaces
    mots = texte.split()
    
    # Compter le nombre de caractères
    caracteres = len(texte)
    
    # Retourner le dictionnaire avec les résultats
    return {"nombre_de_mots": len(mots), "nombre_de_caracteres": caracteres}
# Tests
print(analyse_texte("Bonjour tout le monde"))
print(analyse_texte("Bonjour IISE"))