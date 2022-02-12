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

# def main():
#     my_word = WordSlicer()
#     sliced_word = my_word.slicer()
#     print(sliced_word)

# if __name__ == "__main__":
#     main()