from game import frame_counter
from game.constants import PLAYER_WIDTH
from game import input_service
from game import constants
from game.action import Action
from game.point import Point
from game.bullet import Bullet
from game.constants import IMAGE_BULLET, BULLET_HEIGHT, BULLET_WIDTH, MAX_X, MAX_Y
from game.input_service import InputService
from game.player import Player
from game.frame_counter import FrameCounter



class SpawnBulletsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.bullets = []
        self.frame_counter = FrameCounter()
        self.frame = 0
        self.fire_rate = 10

    def execute(self, cast):
        self.input_service = InputService()
        self.player = cast["player_ship"][0]
        self.fire = self.input_service.get_fire()
        self.frame = self.frame_counter.get_frame_count()
        
        if self.fire:
            if self.frame % self.fire_rate == 0:
                bullet = Bullet()
                bullet.set_image(IMAGE_BULLET)
                bullet.set_width(BULLET_WIDTH)
                bullet.set_height(BULLET_HEIGHT)
                self.x = self.player._position.get_x() + (PLAYER_WIDTH / 2)
                print(f"x = {self.x}")
                self.y = self.player._position.get_y()
                print(f"y = {self.y}")
                position = bullet._position = Point(self.x, self.y)
                bullet.set_position(position)
                self.bullets.append(bullet)
                print("made new bullet")
                num_bullets = len(self.bullets)
                print(f"Number of bullets {num_bullets}")
                cast["bullets"] = self.bullets
