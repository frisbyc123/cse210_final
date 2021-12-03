import os
os.environ['RAYLIB_BIN_PATH'] = "."
import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1

        if self.is_down_pressed():
            dy = 1
        
        if self.is_up_pressed():
            dy = -1
        

        direction = Point(dx, dy)
        return direction
        
    def get_fire(self):
        if self.is_x_pressed():
            return True, "player"

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def is_x_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_X)

    def window_should_close(self):
        return raylibpy.window_should_close()
