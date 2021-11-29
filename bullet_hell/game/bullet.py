from game.actor import Actor
from game.point import Point

class Bullet(Actor):
    """
    Instance of Actor.  Stores the actor type as "bullet"
    """

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "bullet"