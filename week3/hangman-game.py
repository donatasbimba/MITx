# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    nope = 0
    for z in secretWord:
        if z not in lettersGuessed:
            nope = 1
            return False
            break
    if nope == 0:
        return True
    
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedword = ["_ "] * (len(secretWord))
    L_secretWord = list(secretWord)
    for a in lettersGuessed:
        for i in range(len(L_secretWord)):
            if a == L_secretWord[i]:
                guessedword[i] = a
                
    return(''.join(guessedword))
            
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters_available = list(alphabet)
    for a in lettersGuessed:
        if a in letters_available:
            letters_available.remove(a)
    return(''.join(letters_available))
            
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade = 0
    lettersGuessed = []
    print("The word you have to guess has ", str(len(secretWord)), "letters")
    
    print("You have 8 guesses. Or else you will be HANGED")
    while mistakesMade <= 8:
        print("You have ", str(8 - mistakesMade), "guesses left")       
        print("Letters Available ", getAvailableLetters(lettersGuessed))
        guess = input("Enter the letter: ")
        if guess in lettersGuessed:
            print("Oops, you already tried that!")
        elif guess not in lettersGuessed:
            lettersGuessed += guess
            print(lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("You got it! It is ", str(secretWord), "You Won!")
                break
            elif guess in secretWord:
                print("Good!", getGuessedWord(secretWord, lettersGuessed))
                
            elif guess not in secretWord:
                mistakesMade += 1 
                print("Wrong!", getGuessedWord(secretWord, lettersGuessed))
                if mistakesMade > 8:
                    print("You LOST! Prepare your neck")
                    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
