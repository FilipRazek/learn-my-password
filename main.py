"""
    Simple program to learn a password, or a similarly long string of characters.
    The program will ask for the password, and then ask for the successive characters.
    Each time the user enters an incorrect character, the program will start again.
    The program will end when the user enters the correct password.
"""
import os, random

def clear_screen():
    os.system('cls')

def learn_word(hint, word):
    def output_welcome_message():
        clear_screen()
        print("Guess the word! Hint:", hint)
        
    output_welcome_message()

    learning_index = 0
    while learning_index < len(word):
        user_input = input(f"Enter the next character(s): {word[:learning_index]}")
        for character in user_input:
            if character == word[learning_index]:
                learning_index += 1
                print("Correct!")
            else:
                print(f"Incorrect! after {word[:learning_index]}, you guessed {character}, but the correct answer was {word[learning_index]}")
                learning_index = 0
                input("Press Enter to retry")
                output_welcome_message()
                break

    print(f'Congratulations! You have learned the word "{word}"')
    input("Press Enter to continue")

words_to_learn = {
}

items = list(words_to_learn.items())
random.shuffle(items)
for hint, word_to_learn in items:
    learn_word(hint, word_to_learn)