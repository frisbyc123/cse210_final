from game.actor import Actor
from game.point import Point

class Bomb(Actor):
    """
    Instance of Actor.  Stores the actor type as "bomb"
    """

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "bomb"
        self._velocity = Point(0, 5)
        self._timer = 0