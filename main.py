# Fonction qui calcule le nombre de voyelle dans un mot
def get_vowels_numbers(word):
    # Créer un compteur de voyelles
    nb_vowels = 0
    # Pour chaque lettre du mot, vérifiez s'il s'agit bien d'une voyelle
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # Si tout est ok, on ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, renvoyer le compteur
    return nb_vowels

word = input("Entrer un mot: ")
vowels_count = get_vowels_numbers(word)
print("Il y a ", vowels_count, " voyelles dans le mot ", word, " !")

