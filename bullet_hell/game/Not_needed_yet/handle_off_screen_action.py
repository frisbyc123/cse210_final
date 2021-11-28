from game.director import Director
from game.constants import BALL_HEIGHT, BALL_WIDTH
from game.constants import MAX_X, MAX_Y
from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    """
    If the ball hits the edge of the screen, it will bounce.
    It also checks if the ball has hit the bottom of the screen.  If it has,
    it will call for game over.
    """

    def __init__(self):
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0
        self.director = Director()

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_type() == "ball":
                    if actor._position.get_x() < 0 or actor._position.get_x() + BALL_WIDTH > MAX_X:
                        self.x_velocity = actor._velocity.get_x() * -1
                        self.y_velocity = actor._velocity.get_y()
                        actor.set_velocity(Point(self.x_velocity, self.y_velocity))
                    if actor._position.get_y() < 0:
                        self.x_velocity = actor._velocity.get_x()
                        self.y_velocity = actor._velocity.get_y() * -1
                        actor.set_velocity(Point(self.x_velocity, self.y_velocity))
                    if actor._position.get_y() > MAX_Y:
                        self.director._keep_playing = False
