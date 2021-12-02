from game import input_service
from game import constants
from game.action import Action
from game.point import Point
from game.bullet import Bullet
from game.constants import IMAGE_BULLET, BULLET_HEIGHT, BULLET_WIDTH, MAX_X, MAX_Y
from game.input_service import InputService
from game.player import Player


class SpawnBulletsAction(Action):
    
    def __init__(self, input_service):
        super().__init__()
        self.bullets = []
        #self.input_service = input_service

    def execute(self, cast):
        self.input_service = InputService()
        self.player = Player()
        self.fire = self.input_service.get_fire()
        self.x = self.player._position.get_x()
        print(f"x = {self.x}")
        self.y = self.player._position.get_y()
        print(f"y = {self.y}")
        if self.fire:
            bullet = Bullet()
            bullet.set_image(IMAGE_BULLET)
            bullet.set_width(BULLET_WIDTH)
            bullet.set_height(BULLET_HEIGHT)
            position = Point(self.x, self.y)
            bullet.set_position(position)
            self.bullets.append(bullet)
            print("made new bullet")
            num_bullets = len(self.bullets)
            print(f"Number of bullets {num_bullets}")
            cast["bullets"] = self.bullets