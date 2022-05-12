from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Card): Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score of the player. Initial values is 300
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_guess()
            self.do_updates()
            self.do_outputs()
            self.get_continue_playing()

    def get_guess(self):
        """Ask the user for the guessed value.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card is {self.card.value}")
        guess = input("Higher or Lower? [H/L] ")
        self.card.guess = guess.upper()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        self.card.draw()

        self.score += self.card.points

        self.is_playing = (self.score > 0)

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
      
        print(f"\nNext card was: {self.card.value}")
        print(f"Your score is: {self.score}\n")

        if self.score <= 0:
            print("\nYou lost :(\nTry again\n")

    def get_continue_playing(self):
        """Ask the user if they want to keep playing.

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return
            
        keep_playing = input("Keep playing? [y/n] ")
        self.is_playing = (keep_playing == "y")
