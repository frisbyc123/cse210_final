from game.actor import Actor
from game.point import Point

class Background(Actor):
    """
    Instance of Actor.  Stores the actor type as "boss"
    """

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "background"
    
