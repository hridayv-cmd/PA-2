import random

class Die:
    """A class representing a single die."""
    
    def __init__(self, sides=6):
        """Initialize the die attributes (defaults to 6 sides)."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)