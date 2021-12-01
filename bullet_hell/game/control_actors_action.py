from game.constants import PLAYER_Y
from game.constants import MAX_X, PLAYER_WIDTH
from game import input_service
from game import constants
from game.action import Action
from game.point import Point
from game.input_service import InputService

class ControlActorsAction(Action):
    """
    Used to control the actors from keyboard inputs.  
    """

    # Initialization #
    def __init__(self, input_service):
        super().__init__()

        self.input_service = input_service

    def execute(self, cast):
        direction = self.input_service.get_direction()
        player = cast["player_ship"][0]
        fire = self.input_service.get_fire()
        if player._position.get_x() != MAX_X - PLAYER_WIDTH and player._position.get_x() != 0:
            player.set_velocity(direction.scale(constants.PLAYER_SPEED))
        elif player._position.get_x() == MAX_X - PLAYER_WIDTH:
            player.set_position(Point(MAX_X - PLAYER_WIDTH, PLAYER_Y))
        elif player._position.get_x() == 0:
            player.set_position(Point(0, PLAYER_Y))