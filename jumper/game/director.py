from game.parachutetracker import ParachuteTracker
from game.wordslicer import WordSlicer
from game.gametitle import GameTitle


class Director:
    """This class will follow the flow of the game
    """

    def __init__(self) -> None:
        self._sliced_word = WordSlicer()
        self._parachuteTracker = ParachuteTracker()
        self._game_title = GameTitle()
        self._guessed = False
        self._user_guess = ""
        self._tries = 0

    def startGame(self):
        """Starts the game by running the main game loop"""
        while not self._guessed and self._tries < 6:
            self._display()
            self._wordTracker()
            self._addLetter()
            self._slicer()

    def _display(self):
        """Display in the console the flow of the
        game for inputs and outputs.
        """
        self._game_title.clearConsole()
        self._game_title.PrintGameTitle("Jumper")
        self.guess_word = self._sliced_word.slicer()
        self.covered_word = "_ " * len(self.guess_word)
        print(f"Covered word: {self.covered_word} - Uncovered word: {''.join(self.guess_word)}")
        self._parachuteTracker.parachuteChooser(self._tries)
        self._is_playing = True
        # self._tries = 6

    # Logic of the game
    def _wordTracker(self):
        """This Method will evaluate the word and the letter
        that the user what to guess from the jumper
        Also it update the jumper graph
        """
        self._user_guess = input("Please guess a letter or the word: ").upper()
        if len(self._user_guess) == 1 and self._user_guess.isalpha():
            if self._user_guess not in self.guess_word:
                print(f"Sorry, {self._user_guess} is not in the word")
                self._tries += 1
                print(self._tries)
        pass


    # Method to remove
    def _addLetter(self):
        pass
    # Method to remove
    def _slicer(self):
        pass
