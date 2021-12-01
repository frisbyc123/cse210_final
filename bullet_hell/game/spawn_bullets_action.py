from game import constants
from game.action import Action
from game.point import Point
from game.bullet import Bullet
from game.constants import IMAGE_BULLET, BULLET_HEIGHT, BULLET_WIDTH, MAX_X, MAX_Y

class SpawnBulletsAction(Action):
    
    def __init__(self, input_service):
        super().__init__()

        self.input_service = input_service

    def execute(self, cast):
        bullets = []
        bullet = Bullet()
        bullet.set_image(IMAGE_BULLET)
        bullet.set_width(BULLET_WIDTH)
        bullet.set_height(BULLET_HEIGHT)
        x = MAX_X / 2
        y = MAX_Y / 2
        position = Point(x, y)
        bullet.set_position(position)
        bullets.append(bullet)
        print("made new bullet")
        cast["bullets"] = bullets
        return cast["bullets"]