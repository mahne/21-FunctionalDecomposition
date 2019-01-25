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


def main():
    print('Game has started.')
    while True:
        tries = 5
        word,blanks = get_word(words)
        end = False
        while end == False:
            print_current(blanks, tries)
            blanks,tries,end = get_guess(word,blanks,tries,end)
        if input('play again? (y/n)') != 'y':
            end = False
            break
    print('Thanks for playing Hangman!')


def get_word(list):
    min = int(input('Minimum length?'))
    blanks = []
    while True:
        r = random.randrange(0,len(list))
        if len(list[r])>=min:
            for k in range(len(list[r])):
                blanks+=['-']
            return list[r],blanks

def get_guess(word,blanks,tries,end):
    letter = input("What letter do you want to try? ")
    correct = test_guess(word,letter)

    if (correct):
        print('Good Guess')
        fill_blanks(word,blanks,letter)
    else:
        print('Sorry! There are no ' + letter + ' letters in the secret word.')
        tries-=1
    end = win_or_lose(word,blanks,tries,end)
    return blanks,tries,end

def win_or_lose(word,blanks,tries,end):
    win = len(word)
    for k in range(len(word)):
        if blanks[k] == word[k]:
            win -= 1
            if win == 0:
                print("You Win!")
                end = True
    if win != 0 and tries == 0:
        print("You Lose! :(")
        print ('The secret word was: ',word)
        end = True
    return end

def print_current(blanks,tries):
    display = ''
    for k in range(len(blanks)):
        display += blanks[k]
    print(display)
    print('You have ',tries,' guesses left.')


def fill_blanks(word,blanks,letter):

    for k in range(len(word)):
        if blanks[k] == '-':
            if letter == word[k]:
                blanks[k] = letter
    return blanks



def test_guess(word,letter):
    for k in range(len(word)):
        if word[k] == letter:
            return True
    return False




















main()