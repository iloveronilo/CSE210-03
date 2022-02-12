from game.parachutetracker import ParachuteTracker
from game.wordslicer import WordSlicer


class Director:
    """This class will follow the flow of the game
    """

    def __init__(self) -> None:
        self._sliced_word = WordSlicer()
        self._parachuteTracker = ParachuteTracker()
        self._guessed = True

    def startGame(self):
        """Starts the game by running the main game loop"""
        while self._is_playing:
            self._display()
            self._wordTracker()
            self._addLetter()
            self._slicer()

    def _display(self):
        """Display in the console the flow of the
        game for inputs and outputs.
        """
        self.guess_word = self._sliced_word.slicer()
        self.covered_word = "_ " * len(self.guess_word)
        print(f"Covered word: {self.covered_word} - Uncovered word: {''.join(self.guess_word)}")
        self._is_playing = False

    def _wordTracker(self):
        pass

    def _addLetter(self):
        pass

    def _slicer(self):
        pass
