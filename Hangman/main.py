import nltk
from random import choice

# word bank
nltk.download("brown", quiet=True)          # quiet suppresses unnecessary output
word_bank = [word.lower() for word in nltk.corpus.brown.words() if word.isalpha()]
def get_difficulty():
    """
    Prompt user for difficulty mode: easy (E) or hard (H)
    :return: str, the desired difficulty
    """
    while True:
        try:
            mode = input("What difficulty do you prefer? Easy (E) or Hard (H): ").upper()
            if mode not in ["E", "H"]:
                raise ValueError("Invalid difficulty\n")
            break
        except ValueError as error:
            print(error)

    return mode

def get_word_bank(mode):
    """
    :param mode: the difficulty which determines the word length
    :return: list, the filtered word bank
    """
    filtered_words = None
    if mode == "E":
        filtered_words = [word for word in word_bank if 4 < len(word) < 11]
    elif mode == "H":
        filtered_words = [word for word in word_bank if len(word) >= 11]

    return filtered_words

def get_guess(guessed_letters):
    """
    :return: str, the character to be tried as a guess
    """
    while True:
        try:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha():
                raise ValueError("Your guess must be a letter.\n")
            if len(guess) != 1:
                raise Exception("Guess only one letter.\n")
            if guess in guessed_letters:
                raise Exception("You've guessed this letter before.\n")
            break
        except (ValueError, Exception) as error:
            print(error)

    return guess

def game_play():
    """
    main game play
    """
    print()
    mode = get_difficulty()
    filtered_words = get_word_bank(mode)

    secret_word = choice(filtered_words)
    word_length = len(secret_word)
    current_state = ["_" for _ in range(word_length)]
    print(f"The word you have to guess has {word_length} letters: {''.join(current_state)}\n")

    incorrect_guesses = list()
    guessed_letters = list()

    while "_" in current_state and len(incorrect_guesses) < 6:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(word_length):
                if secret_word[i] == guess:
                    current_state[i] = guess
        else:
            incorrect_guesses.append(guess)
            draw_hangman(len(incorrect_guesses))

        if len(incorrect_guesses) != 6:         # only print if not dead
            print(" " * 8 + "".join(current_state).center(22))
            print()

    if "_" in current_state:
        print(f"You've been hung! The word was {secret_word.upper()}\n")
    else:
        print("Congratulations! You guessed the word!\n")

def draw_hangman(count=0):
    """
    Prints the current state of the hangman game
    :param count: the number of incorrect guesses
    """
    figures = [
        # no body parts
        """                 
        -------------
        |           |
        |           |
        |           
        |           
        |           
        |           
        |           
        |____________________      
        """,

        # head
        """                 
        -------------
        |           |
        |           |
        |           O
        |           
        |           
        |           
        |           
        |____________________       
        """,

        # head, body
        """                 
        -------------
        |           |
        |           |
        |           O
        |           |
        |           |
        |           |
        |           |
        |           |
        |____________________    
        """,

        # head, body, left arm
        """                 
        -------------
        |           |
        |           |
        |           O
        |           |
        |         / |
        |       /   |
        |           |
        |           |  
        |____________________
        """,

        # head, body, left arm, right arm
        """                 
        -------------
        |           |
        |           |
        |           O
        |           |
        |         / | \\
        |       /   |   \\
        |           |
        |           |  
        |____________________
        """,

        # head, body, left arm, right arm, left leg
        """                 
        -------------
        |           |
        |           |
        |           O
        |           |
        |         / | \\
        |       /   |   \\
        |         / |
        |       /   | 
        |____________________
        """,

        # all body parts: head, body, left arm, right arm, left leg, right leg
        """                  
        -------------
        |           |
        |           |
        |           O
        |           |
        |         / | \\
        |       /   |   \\
        |         / | \\
        |       /   |   \\
        |____________________
        """
    ]
    print(figures[count])

def main():
    print("Welcome to Hangman!")
    play_again = True
    while play_again:
        game_play()

        user_input = input("Do you want to play again? Enter Y for yes: ").upper()
        play_again = True if user_input == "Y" else False

    print("Thanks for playing with us!")



if __name__ == '__main__':
    main()
