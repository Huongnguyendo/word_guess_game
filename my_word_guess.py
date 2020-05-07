import csv
import random

word_list = []
with open('secret_words.csv', newline='') as file:
    for row in csv.reader(file):
        word_list.append(row[0])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

player_name = input("Please enter player's name: ")
print(f"Welcome {player_name}! Let's play word guess!")

def play_again():
    answer = input('Would you like to play again? Press "y" for yes ').lower()
    if answer == 'y':
        guess_the_word()
    else:
        pass

def guess_the_word():
    letter_list = []
    tries = 8
    secret_word = random.choice(word_list)

    print("Your secret word has", str(len(secret_word)), "letters")
    print("*" * len(secret_word))

    solved = False

    while solved == False and tries > 0:
        print(f"You have {tries} tries left!")
        guess = input("Please input a letter: ").lower()

        if guess not in alphabet:
            print("Please input a valid letter: ") 
        elif guess in letter_list:
            print("You have already guessed this letter!")
        elif guess not in letter_list:
            if guess in secret_word:
                letter_list.append(guess)
                print("Letter is in secret word!")
            else:
                letter_list.append(guess)
                tries -= 1 
                print("Letter is not in secret word!")
        
        display_status = ""

        for letter in secret_word:
            if letter in letter_list:
                display_status += letter
            else:
                display_status += "*"
        print(display_status)

        if display_status == secret_word:
            print(f"You have guessed the word. It's {secret_word}")
            solved = True
        elif tries == 0:
            print(f"You ran out of tries. Secret word is {secret_word}")

    play_again()

guess_the_word()
        

        
