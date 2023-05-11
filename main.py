# Function that calculates the number of vowels in a word
def get_vowels_numbers(word):
    # Create a vowel counter
    nb_vowels = 0
    # For each letter of the word, check if it is indeed a vowel
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # If everything is ok (if it is indeed a vowel), we add one to the counter
            nb_vowels += 1

    # At the end of the function, return the vowel counter
    return nb_vowels


word = input("Entrer un mot: ")
vowels_count = get_vowels_numbers(word)
print("Il y a ", vowels_count, " voyelles dans le mot ", word, " !")
