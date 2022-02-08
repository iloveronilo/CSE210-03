class ParachuteTracker:
    """This class will track and display
    the parachute on the console
    """

    def __init__(self) -> None:
        self._parachute_index = 0


    def parachute(self) -> list:
        """This method will return a list
        that will show the state of parachute
        """
        self.parachute = [
            """
            ________
              ___
             /___\\
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             /___\\
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             
             
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             
             
               X
              /|\\
              / \\

            ^^^^^^^
            """            
        ]
        return self.parachute[self._parachute_index]

    def parachuteChooser(self, index=0) -> None:
        """This Method will choose from a
        list the state of the parachute
        """
        self._parachute_index = index
        print(self.parachute())
