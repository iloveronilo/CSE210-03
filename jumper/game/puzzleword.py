import random

class PuzzleWord:
    """ This class will choose a random word from
    a list of words
    """

    def __init__(self) -> None:
        """Class constructor it will initiate
        the list of random words.
        """
        self._wordlist = []

    def randomWord(self):
        """Method that choose a random word from
        the list of words.
        Returns:
            my_random_word: string
        """
        my_random_word = random.choice(self._wordlist)
        return my_random_word