import Resolver
import Display

import os, sys

class Hangman:

    def __init__(self, display):
        # Temporary var
        self.words = ["Salut", "Omelette", "Du", "Fromage"]
        self.word = "omelette"

        # Game settings
        self._difficulty = 0
        self._dictionary_directory = "dictionary"
        self._Hangman_directory = "hangman_img"

        # User settings
        self._name = "User"
        self._input = 0

        # Level settings
        self._level = 0

        self.resolver = Resolver.HangmanResolver(self.word)
        self.display = Display.HangmanDisplay(display)

    # Methods
    def update(self):

        # Resolver
        self.resolver.update(self.input)

        # Display
        self.display.update()
        self.display.titleBar()
        self.display.middleBar()
        self.display.hangman(0)
        self.display.userTry(self.resolver._user_word)
        self.display.userInputGood(self.resolver._user_good)
        self.display.userInputWrong(self.resolver._user_try)

    # Get/Set
    def _get_input(self):
        return self._input

    def _set_input(self, new_value):
        self._input = new_value

    input = property(_get_input, _set_input)
