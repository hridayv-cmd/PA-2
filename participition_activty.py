import random

class Die:
    """A class representing a single die."""
    
    def __init__(self, sides=6):
        """Initialize the die attributes (defaults to 6 sides)."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)
    
    # 1. Make a 6-sided die and roll it 10 times 
print("--- Rolling a 6-sided die 10 times ---")
six_sided_die = Die() # Uses the default value of 6
for _ in range(10):
    print(six_sided_die.roll_die(), end=" ")
print("\n") # New line for spacing