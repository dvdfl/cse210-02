import random

class Card:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Card is to keep track of the guess, the card value and calculate the points for 
    it.
   
    Attributes:
        value (int): The number on the card drawn. it is initialized witha random value.
        guess (int): The guess on the next value, H for higher or L for lower.
        points (int): The number of points based on the guessed value 100 if guessed right, otherwise -75 .
    """

    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.points = 0
        self.guess = 0
        self.value = random.randint(1,13)

    def draw(self):
        """Generates a new random card value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        prev_value = self.value
        self.value = random.randint(1,6)
        

        if self.guess == "H" and self.value > prev_value:
            self.points = 100
        elif self.guess == "L" and self.value < prev_value:
            self.points = 100
        else:
            self.points = -75
