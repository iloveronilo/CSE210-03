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
        self.load_list()
        my_random_word = random.choice(self._wordlist)
        return my_random_word.upper()

    def load_list(self) -> None:
        """This Method will fill the wordlist
        from a txt file
        """
        with open("words.txt", "rt") as text_file:
            read_data = text_file.readlines()
            for line in read_data:
                clean_line = line.strip()
                self._wordlist.append(clean_line)
