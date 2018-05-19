import os
import random
import string


WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 8


class Word:

    def __init__(self):
        self.word = ''
        self.lettersGuessed = []

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        try:
            inFile = open(WORDLIST_FILENAME, 'r', 0)
        except IOError:
            print '{} cannot open'.format(WORDLIST_FILENAME)
            exit()
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        if len(wordlist) < 1:
            print '{} does not have words'.format(WORDLIST_FILENAME)
            exit()
        print "  ", len(wordlist), "words loaded."
        self.word = random.choice(wordlist).lower()

    def isWordGuessed(self):
        for letter in self.word:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self):
        guessed = ''
        for letter in self.word:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return available

    def differentLetters(self):
        return len(set(self.word))


def hangman(words):

    guesses = MAX_GUESSES

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(words.word), ' letters long.'
    print 'Has', words.differentLetters(), 'different letters'
    print '-------------'

    while words.differentLetters() > guesses:
        print 'The number of different letters is greater than the number of attempts'
        print 'Do you want one new word?\ny- yes\nn- no'
        input = raw_input()
        if input == 'y':
            words.loadWords()
        elif input == n:
            break
        else:
            print 'Invalid option'

    while  words.isWordGuessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        available = words.getAvailableLetters()
        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')

        if len(letter) != 1 or letter.isalpha() == False:
            print 'Oops! "{}" is not a letter! Please guess a new letter.'.format(letter)
        elif letter in words.lettersGuessed:
            guessed = words.getGuessedWord()
            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in words.word:
            words.lettersGuessed.append(letter)
            guessed = words.getGuessedWord()
            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            words.lettersGuessed.append(letter)
            guessed = words.getGuessedWord()
            print 'Oops! That letter is not in my word: ', guessed
        print '------------'

        letter = raw_input()
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        if words.isWordGuessed():
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', words.word, '.'


if __name__ == "__main__":
    words = Word()
    words.loadWords()
    hangman(words)
