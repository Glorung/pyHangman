class HangmanResolver:

    def __init__(self, word_to_find):
        self._word_to_find = word_to_find
        self._displayed_text = ""
        self._user_wrong_try = ""
        self._user_good_try = ""

        self._user_life = 8

        self.create_displayed_word()

    def __str__(self):
        return self._word_to_find

    def __len__(self):
        return len(_word_to_find)

    # Convert word_to_find to a displayed text like: this -> _ _ _ _
    def create_displayed_word(self):
        self._displayed_text = ""
        i = 0

        while (i < len(self._word_to_find)):

            # Show the letter if the user tryed it or put an _
            j = self._user_good_try.find(self._word_to_find[i])
            if (j >= 0):
                self._displayed_text += " "
                self._displayed_text += self._user_good_try[j]
            else:
                self._displayed_text += " _"
            i = i + 1

    def isWon(self):
        if (self._displayed_text.find("_") == -1):
            return 1
        return 0

    def isLost(self):
        if (self._user_life <= 0):
            return 1
        return 0

    # Test the key pressed by the user
    def update(self, key):
        if (key):
            if (self._user_wrong_try.find(key) == -1 and self._user_good_try.find(key) == -1):
                if (self.isInWord(key)):
                    self._user_good_try += key
                else:
                    self._user_wrong_try += key
                    self._user_life += -1
        self.create_displayed_word()

    def isInWord(self, key):
        if (self._word_to_find.find(key) == -1):
            return 0
        else:
            return 1
