import os
import shutil

class GameTitle():
    """This class will create a title for the game
    and center it on the console.
    """

    def __init__(self) -> None:
        self._terminal_size = shutil.get_terminal_size().columns
        # self.game_title = ""

    def clearConsole(self) -> None:
        """Clear console according the OS
        Returns: nothing
        """
        if os.name in ('nt', 'dos'):
            os.system('cls')
        else:
            os.system('clear')

    def PrintGameTitle(self, game_title) -> None:
        """Print a center title in console
        Parameters:
            game_title: string of the game title
        Returns:
            nothing
        """
        tittle = f'{game_title}  - \U0001f601  \n'
        print(tittle.center(self._terminal_size))

