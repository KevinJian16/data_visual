from random import randint


class Die:
    def __init__(self, sides=6):
        """Initialize a die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll(self):
        """Simulate rolling the die and return a random number between 1 and the number of sides."""
        return randint(1, self.sides)
