# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    # print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    result = True
    for c in secret_word:
        result = result and (c in letters_guessed)
    return result

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    and prints out all the characters you haven't guessed yet
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    word = []
    for c in lower(secret_word):
        if c in letters_guessed:
            word.append(c)
        else:
            word.append('-')
    remaining_letters = ['(']
    for c in ascii_lowercase:
        if c in letters_guessed:
            remaining_letters.append('-')
        else:
            remaining_letters.append(c)
    remaining_letters.append(')')
    print join(remaining_letters,''), "secret word: ", join(word,'')

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    while (mistakes_made < MAX_GUESSES):
        print_hangman_image(mistakes_made)
        # print (MAX_GUESSES - mistakes_made), "guesses left"
        print_guessed()

        letter = raw_input("What letter do you guess, or guess the whole word? ")
        letter = lower(letter)
        if (len(letter) == 1):
            if (letter in letters_guessed):
                print "You already guessed that letter. Try again."
            else:
                letters_guessed.append(letter)
                if (letter in secret_word):
                    print "That's right!", letter, "is in the secret word."
                    if word_guessed():
                        print "You got it! Congratulations!"
                        mistakes_made = MAX_GUESSES                 
                else:
                    print "Wrong!", letter, "is not in the secret word."
                    mistakes_made += 1
        else: # guessing whole word
            mistakes_made = MAX_GUESSES # you only get one guess at the word
            if word_guessed():
                print "You got it! Congratulations!"
            else:
                print "Sorry, that's not the right word."

    print "The secret word is", secret_word
    print "Game Over!!"

    return None

play_hangman()
