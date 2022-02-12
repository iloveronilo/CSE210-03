from game.puzzleword import PuzzleWord


class WordSlicer:
    """Class will take a word and slice it into
    letter
    """

    def __init__(self) -> None:
        self._word = PuzzleWord().randomWord()

    def slicer(self) -> list:
        """This Method will take a word and slice it
        into a list of letters
        """
        self.sliced_word = list(self._word)
        return self.sliced_word
