
#
# Curses keys
#
# ESC: 27
#

import curses

class HangmanDisplay:

    def __init__(self, display_curses):
        self._display = display_curses

        # Init curses colors

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)

        # Init the display size attributes
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

    def titleBar(self, more = 0):
        title = " Le jeu du pendu "
        begin_height = self._height // 4 - 1;
        begin_width = (self._center_width // 2) - (len(title) // 2) - 1;
        self._display.addstr(begin_height, begin_width, title, curses.A_REVERSE)

        if (more != 0):
            i = 0
            for line in more:
                begin_height = self._height // 4 + i;
                begin_width = (self._center_width // 2) - (len(line) // 2) - 1;
                self._display.addstr(begin_height, begin_width, line, curses.A_REVERSE)
                i = i + 1

    def middleBar(self):
        i = 0
        j = self._center_width

        while (j < self._width - 1):
            while (i < self._height):
                self._display.addstr(i, j, " ", curses.color_pair(3))
                i = i + 1
            i = 0
            j = j + 1

    def hangman(self, level, imgs):
        begin_height = int(self._height * 1 / 3) - 1
        begin_width = int(self._width * 5 / 8)

        text_to_see = (imgs["./hangman_img/" + str(level) + ".hangman"])
        text_to_see_array = text_to_see.split('\n')
        for line in text_to_see_array:
            self._display.addstr(begin_height, begin_width, line, curses.color_pair(3))
            begin_height += 1

    def hidenWord(self, word):
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
