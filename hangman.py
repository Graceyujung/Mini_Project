import random

# create a list of words from which the game will randomly choose a word for the player to guess.
fruits_list = ["Apple", "Banana", "Pineapple", "Pear", "Mango", "Grape",
            "Durian", "Watermelon", "Kiwi", "Starwberry", "Orange", "Apricot"
            "Cherry", "Peach", "Pomelo", "Clementine", "Satsuma"]
name_list = ["Aspyn", "Carlos", "Dana", "Alfredo", "Yasuko", "Emilio",
             "Shigeo", "Suguru", "Marcelo", "Sebastian", "Grace", "Cristian",
             "Hiroaki", "Elvis", "Mai", "Prachyut", "Dan", "Hina", "Majo", "Kiarash"]
dogs_list = ["Chihuahua", "Pomeranian", "Dachshund", "Beagle", "Bulldog"
             "Mastiff", "Boxer", "Dalmatian", "Greyhound", "Eskimo", "Wofhound",
             "Whippet", "Poodle", "Husky", "Labrador", "Terrier", "Shiba"]

# define randomWord as a global variable
randomWord = ""

def choose_theme():
    global randomWord
    while True:
        print("Choose a theme of words:")
        print("1. Fruits")
        print("2. Names")
        print("3. Dog Breeds")

        choice = input("Enter the number of your choice (1-3): ").strip()

        if choice == '1':
            randomWord = random.choice(fruits_list).lower()
            menu()
            break
        elif choice == '2':
            randomWord = random.choice(name_list).lower()
            menu()
            break
        elif choice == '3':
            randomWord = random.choice(dogs_list).lower()
            menu()
            break
        else:
            print("Invalid choice. Please select a valid number (1-3).")

def menu():
    global randomWord
    print("\nWelcome to Hangman!")
    guessed_letters = []  # track guessed letters
    attempts = 6

    while attempts > 0:
        display(guessed_letters)
        print(f"Incorrect guesses remaining: {attempts}")
        g = input("Guess a letter: ").lower()

        if g.isalpha() and len(g) == 1:
            if g not in guessed_letters: # check if the letter hasn't been guessed
                guessed_letters.append(g)
                print(f"Guessed letters: {', '.join(guessed_letters)}")
                if play(g): # check if the guess is correct
                    print(f"Good job! '{g}' is in the word.")
                else:
                    attempts -= 1
                    print(f"Sorry, '{g}' is not in the word. Please try again.")
            else:
                print("You've already guessed that letter. Please try again.")
        else:
            print("Invalid input. Please select a valid alphabet.\n")
            continue

        # if all letters have been guessed
        if all(l in guessed_letters for l in randomWord):
            print("\nCongratulations! You've guessed the word:", randomWord.upper())
            break
    else:
        print("\nGame Over! You've run out of attempts.")
        print("The word was", randomWord.upper())

    new_game()


def display(guessed_letters):
    print("\nCurrent word: ", end="")
    for l in randomWord:
        if l in guessed_letters:
            print(l.upper(), end=" ")
        else:
            print("_", end=" ")
    print()

def play(g):
    return g in randomWord # return True if g is in randomWord

def new_game():
    while True:
        response = input("Try again? (Y, N): ").upper()
        if response == 'Y':
            print()
            choose_theme() # call menu to start a new game
            break
        elif response == 'N':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid option. Please enter a valid option (Y or N).")

if __name__ == "__main__":
    choose_theme()
