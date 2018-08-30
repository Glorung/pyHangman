class HangmanResolver:

    def __init__(self, word_to_find):
        self._word_to_find = word_to_find
        self._user_word = ""
        self._user_try = ""
        self._user_good = ""

        self.__init__user_word()

    def __init__user_word(self):
        i = 0
        end = 0

        self._user_word = ""
        while (i < len(self._word_to_find)):
            j = self._user_good.find(self._word_to_find[i])

            if (j >= 0):
                self._user_word += " "
                self._user_word += self._user_good[j]
            else:
                end = 1
                self._user_word += " _"
            i = i + 1

            if (end == 1):
    def __str__(self):
        return self._word_to_find

    def __len__(self):
        return len(_word_to_find)

    def update(self, keyPressed):
        key = keyPressed
        if (key):
            if (self._user_try.find(key) == -1 and self._user_good.find(key) == -1):
                if (self.isInWord(keyPressed)):
                    self._user_good += keyPressed
                else:
                    self._user_try += keyPressed
        self.__init__user_word()

    def isInWord(self, key):
        if (self._word_to_find.find(key) == -1):
            return 0
        else:
            return 1
