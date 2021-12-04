from game.director import Director
from game.constants import MAX_X, MAX_Y
from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    """
    Checks if bullets have left the screen. 
    If they have, they get deleted.
    """

    def __init__(self):
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0
        #self.director = Director()

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_type() == "player_bullet":
                    if actor._position.get_x() < 0 or actor._position.get_x() > MAX_X:
                        group.remove(actor)
                    if actor._position.get_y() < 0 or actor._position.get_y() > MAX_Y:
                        group.remove(actor)
                elif actor.get_type() == "enemy_bullet":
                    if actor._position.get_x() < 0 or actor._position.get_x() > MAX_X:
                        group.remove(actor)
                    if actor._position.get_y() < 0 or actor._position.get_y() > MAX_Y:
                        group.remove(actor)

