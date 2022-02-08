from game.parachutetracker import ParachuteTracker
from game.wordslicer import WordSlicer


class Director:
    """This class will follow the flow of the game
    """

    def __init__(self) -> None:
        self._parachuteTracker = ParachuteTracker()
        self._is_playing = True
        self._wordSlicer = WordSlicer()

    def startGame(self):
        """Starts the game by running the main game loop"""
        while self._is_playing:
            self._display()
            self._wordTracker()
            self._addLetter()
            self._slicer()

    def _display(self):
        pass

    def _wordTracker(self):
        pass

    def _addLetter(self):
        pass

    def _slicer(self):
        pass
