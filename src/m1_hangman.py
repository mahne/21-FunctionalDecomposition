"""
Hangman.

Authors: Ethan Mahn and Nasser Hegar.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()
import random


def get_word(list):
    min = int(input('Minimum length?'))
    blanks = []
    while True:
        r = random.randrange(0,len(list))
        if len(list[r])>=min:
            for k in range(len(list[r])):
                blanks+=['_']
            return list[r],blanks

def get_guess(word,blanks,tries):
    letter = input("What letter do you want to try? ")
    #print(guess)
    correct = test_guess(word,letter)

    if (correct):
        print('Good Guess')
        guesses = fill_blanks(word,blanks,letter)
    else:
        guesses = ''
        print('Sorry! There are no ' + letter + ' letters in the secret word.')
        tries-=1
    win_or_lose(word, guesses,tries)

    return

def win_or_lose(word,guesses,tries):
    win = len(word)
    for k in range(len(word)):
        if guesses[k] == word[k]:
            win -= 1
            if win == 0:
                print("You Win!")
    if win != 0 and tries == 0:
        print("You Lose! :(")




def fill_blanks(word,blanks,letter):

    for k in range(len(word)):
        if blanks[k] == '_':
            if letter == word[k]:
                blanks[k] = letter

    print(str(blanks))
    return blanks



def test_guess(word,letter):
    for k in range(len(word)):
        if word[k] == letter:
            return True
    return False


def main():
    print('Game has started.')
    tries = 5
    word,blanks = get_word(words)
    print(word,blanks)
    while True:
        get_guess(word,blanks,tries)
        print

















main()