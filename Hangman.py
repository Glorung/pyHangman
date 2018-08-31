from Resolver import HangmanResolver
from Display import HangmanDisplay

import os, sys

import glob

import random

from pprint import pprint

def var_dump(var, prefix=''):
    """
    You know you're a php developer when the first thing you ask for
    when learning a new language is 'Where's var_dump?????'
    """
    my_type = '[' + var.__class__.__name__ + '(' + str(len(var)) + ')]:'
    print(prefix, my_type, sep='')
    prefix += '    '
    for i in var:
        if type(i) in (list, tuple, dict, set):
            var_dump(i, prefix)
        else:
            if isinstance(var, dict):
                print(prefix, i, ': (', var[i].__class__.__name__, ') ', var[i], sep='')
            else:
                print(prefix, '(', i.__class__.__name__, ') ', i, sep='')


class Hangman:

    def __init__(self, display):
        # Game settings
        self._dictionary_directory = "dictionary"
        self._hangman_directory = "hangman_img"

        # User settings
        self._name = "User"
        self._input = 0

        self.imgs = {}
        self.dics = {}
        self.openHangman()
        self.openDictionnary()

        self.word = ""
        self.rndWord()

        # Level settings
        self.resolver = HangmanResolver(self.word)
        self.display = HangmanDisplay(display)

    # Methods
    def update(self):

        # Resolver
        if (not(self.resolver.isWon()) and not(self.resolver.isLost())):
            self.resolver.update(self.input)

        # Display
        if (self.resolver.isWon()):
            self.display.update()
            self.display.titleBar(["", "Bien joue !", "Appuyer sur ESC pour quitter"])
            self.display.middleBar()
            self.display.hangman(8 - self.resolver._user_life, self.imgs)
            self.display.hidenWord(self.resolver._displayed_text)
        elif (self.resolver.isLost()):
            self.display.update()
            self.display.titleBar(["", "Perdu !", "Appuyer sur ESC pour quitter"])
            self.display.middleBar()
            self.display.hangman(8 - self.resolver._user_life, self.imgs)
            self.display.hidenWord(self.resolver._word_to_find)
        else:
            self.display.update()
            self.display.titleBar()
            self.display.middleBar()
            self.display.hangman(8 - self.resolver._user_life, self.imgs)
            self.display.hidenWord(self.resolver._displayed_text)
            self.display.userInputGood(self.resolver._user_good_try)
            self.display.userInputWrong(self.resolver._user_wrong_try)

    # Dir opener
    def openDictionnary(self):
        dir_dic = glob.glob('./' + self._dictionary_directory + '/*.dic')

        for dic in dir_dic:
            new_file = open(dic, "r")
            self.dics.update({dic.split('.')[0] : new_file.read().split('\n')})
            new_file.close()

    def openHangman(self):
        dir_img = glob.glob('./' + self._hangman_directory + '/*.hangman')

        for img in dir_img:
            new_file = open(img, "r")
            self.imgs.update({img : new_file.read()})
            new_file.close()

    def rndWord(self):
        themeChosen = self.dics['']
        i = random.randint(0, len(themeChosen))
        pprint(themeChosen)
        self.word = themeChosen[i]

    # Get/Set
    def _get_input(self):
        return self._input

    def _set_input(self, new_value):
        self._input = new_value

    input = property(_get_input, _set_input)
