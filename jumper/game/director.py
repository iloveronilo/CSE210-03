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
        self._indices = []
        self._index = 0
        self._tries = 0
        self._guess_word = self._sliced_word.slicer()
        self._covered_word = "_" * len(self._guess_word)

    def startGame(self):
        """Starts the game by running the main game loop"""
        while not self._guessed and self._tries < 6:
            self._display()
            self._wordTracker()
            self._gameOver()

    def _display(self):
        """Display in the console the flow of the
        game for inputs and outputs.
        """
        self._game_title.clearConsole()
        self._game_title.PrintGameTitle("Jumper")
        # self._tries = 6

    # Logic of the game
    def _wordTracker(self):
        """This Method will evaluate the word and the letter
        that the user what to guess from the jumper
        Also it update the jumper graph
        """
        self._parachuteTracker.parachuteChooser(self._tries)
        self._uncovered_word = list(self._covered_word)
        self._is_playing = True
        print(f"Uncovered word: {''.join(self._guess_word)}")
        self._user_guess = input("\nPlease guess a letter or the word: ").upper()
        if len(self._user_guess) == 1 and self._user_guess.isalpha():
            if self._user_guess not in self._guess_word:
                print(f"Sorry, {self._user_guess} is not in the word")
                self._tries += 1
                print(self._tries)
            else:
                print(f"Awesome, {self._user_guess} is in the word")
                for letter in self._guess_word:
                    if self._user_guess == letter:
                        self._indices.append(self._index)
                        self._index += 1
                    else:
                        self._index += 1
                for i in range(len(self._covered_word)):
                    if i in self._indices:
                        self._uncovered_word[i] = self._user_guess
                self._covered_word = "".join(self._uncovered_word)
                self._indices = []


    # Method to remove
    def _gameOver(self):
        if self._tries == 6:
            self._guessed = True
            # self._display()
            print("""
            
             ____    _    __  __ _____    _____     _______ ____  
            / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
           | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
           | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
            \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\\
                                                                

            """)
