#
# Curses keys
#
# ESC: 27
#

import curses

class HangmanDisplay:

    def __init__(self, display_curses):
        self._display = display_curses

        # Init curses

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        # Set display size attributes

        self._center_height = 0
        self._center_width = 0

        self._height = 0
        self._width = 0

        self.update()

    def update(self):
        self.clear()

        self._height, self._width = self._display.getmaxyx()

        self._center_height = self._height // 2
        self._center_width = self._width // 2

    def getKey(self):
        key = self._display.getch()

        if key < 255:
            if (key >= ord('A') and key <= ord('Z')):
                key = (key - ord('A')) + ord('a')
            if (key >= ord('a') and key <= ord('z')):
                key = chr(key)
            elif (key == 27):
                key = 27
            else:
                key = ''
        else:
            key = ''
        return key

    # Display methods
    def clear(self):
        self._display.clear()
        self._display.refresh()

    def refresh(self):
        self._display.refresh()

    def titleBar(self):
        title = " Le jeu du pendu "
        begin_height = self._height // 4 - 1;
        begin_width = (self._center_width // 2) - (len(title) // 2) - 1;
        self._display.addstr(begin_height, begin_width, title, curses.A_REVERSE)

    def middleBar(self):
        i = 0

        while (i < self._height):
            self._display.addch(i, self._center_width, "|")
            i = i + 1

    def hangman(self, level):
        level = 0

    def userTry(self, word):
        text_begin_width = (self._center_width // 2) - (len(word) // 2) - 1
        self._display.addstr(self._center_height - 1, text_begin_width, word)

    def userInputGood(self, inputs):
        title = "Vos essais juste:"
        begin_height = int(self._height * 3 / 4) - 1
        begin_width = 0

        self._display.addstr(begin_height, begin_width, title, curses.A_REVERSE)
        self._display.addstr(begin_height, begin_width + len(title), " ")
        self._display.addstr(begin_height, begin_width + len(title) + 1, inputs, curses.color_pair(2))

    def userInputWrong(self, inputs):
        title = "Vos essais faux:"
        begin_height = int(self._height * 3 / 4)
        begin_width = 0

        self._display.addstr(begin_height, begin_width, title, curses.A_REVERSE)
        self._display.addstr(begin_height, begin_width + len(title), " ")
        self._display.addstr(begin_height, begin_width + len(title) + 1, inputs, curses.color_pair(1))
