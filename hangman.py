import random

words_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words_list)


def initiate_game():
    print("H A N G M A N")
    print()


def hide_word(letters, lst=[]):
    for letter in letters:
        if letter not in lst:
            letters = letters.replace(letter, "-")
    return letters


def hangman_game():
    initiate_game()
    num_of_tries = 8
    word_start = hide_word(word)
    guessed_letters = []

    while num_of_tries > 0:
        print(word_start)

        guess = input("Input a letter: ")

        if guess in word and guess not in guessed_letters:
            guessed_letters.append(guess)
            word_start = hide_word(word, guessed_letters)
            print()
            if "-" not in word_start:
                print(word_start)
                print("You guessed the word!\n"
                      "You survived!")
                break

        elif guess in guessed_letters:
            num_of_tries -= 1
            print('No improvements\n')

        else:
            num_of_tries -= 1
            if num_of_tries == 0:
                print("No such letter in the word\nYou are hanged!")
            else:
                print("No such letter in the word\n")

hangman_game()
