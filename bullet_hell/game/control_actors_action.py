from game.constants import PADDLE_Y
from game.constants import MAX_X, PADDLE_WIDTH
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

    # Changes the paddle's velocity based on what keyboard input we are receiving.
    # Also has code to prevent the paddle from moving off screen, but it doesn't work.
    def execute(self, cast):
        direction = self.input_service.get_direction()
        paddle = cast["paddle"][0]
        if paddle._position.get_x() != MAX_X - PADDLE_WIDTH and paddle._position.get_x() != 0:
            paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))
        elif paddle._position.get_x() == MAX_X - PADDLE_WIDTH:
            paddle.set_position(Point(MAX_X - PADDLE_WIDTH, PADDLE_Y))
        elif paddle._position.get_x() == 0:
            paddle.set_position(Point(0, PADDLE_Y))