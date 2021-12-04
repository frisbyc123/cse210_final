from game.actor import Actor
from game.point import Point

class Player(Actor):
    """
    Instance of Actor.  Stores the actor type as "player"
    """

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "player"
        self._health = 100
    
