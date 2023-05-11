# Bonus: function that counts the number of letters in a word
def get_letters_numbers(word, h=None):
    nb_letters = 0

    for letter in word:

        if letter in ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z'
                      ]:
            nb_letters += 1
    # Pay attention to the indentation
    return nb_letters


word = input("Entrer un mot: ")
words_count = get_letters_numbers(word)
print("Il y a ", words_count, " lettres dans le mot ", word, " !")
