from game.actor import Actor
from game.point import Point

class Boss(Actor):
    """
    Instance of Actor.  Stores the actor type as "boss"
    """

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "boss"
        self._velocity = Point(2, 0)
        self._health = 1000
    
