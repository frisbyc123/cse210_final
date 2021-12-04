from game.constants import IMAGE_BULLET
from game.constants import IMAGE_ENEMY_BULLET
from game.constants import BOSS_WIDTH, BOSS_HEIGHT
from game import frame_counter
from game.constants import PLAYER_WIDTH
from game import input_service
from game import constants
from game.action import Action
from game.point import Point
from game.enemy_bullet import EnemyBullet
from game.constants import BULLET_HEIGHT, BULLET_WIDTH, MAX_X, MAX_Y
from game.input_service import InputService
from game.player import Player
from game.frame_counter import FrameCounter
import random

class SpawnBossBulletsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.boss_bullets = []
        self.frame_counter = FrameCounter()
        self.frame = 0
        self.fire_rate = 5

    def execute(self, cast):
        #self.input_service = InputService()
        self.boss = cast["boss"][0]
        self.fire = random.randint(0, 1)
        self.frame = self.frame_counter.execute(cast)
        #print(f"frame count: {self.frame}")
        
        if self.fire:
            if self.frame % self.fire_rate == 0:
                # Center Bullet
                bullet = EnemyBullet()
                bullet.set_image(IMAGE_BULLET)
                bullet.set_width(BULLET_WIDTH)
                bullet.set_height(BULLET_HEIGHT)
                self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                #print(f"boss x = {self.x}")
                self.y = self.boss._position.get_y() + BOSS_HEIGHT
                #print(f"boss y = {self.y}")
                #self.x = MAX_X / 2
                #self.y = MAX_Y / 2
                position = bullet._position = Point(self.x, self.y)
                bullet.set_position(position)
                bullet._velocity = Point(0, 10)
                self.boss_bullets.append(bullet)
                
                # Right Bullet
                bullet = EnemyBullet()
                bullet.set_image(IMAGE_BULLET)
                bullet.set_width(BULLET_WIDTH)
                bullet.set_height(BULLET_HEIGHT)
                self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                self.y = self.boss._position.get_y() + BOSS_HEIGHT
                position = bullet._position = Point(self.x, self.y)
                bullet.set_position(position)
                bullet._velocity = Point(10, 10)
                self.boss_bullets.append(bullet)
                
                # Left Bullet
                bullet = EnemyBullet()
                bullet.set_image(IMAGE_BULLET)
                bullet.set_width(BULLET_WIDTH)
                bullet.set_height(BULLET_HEIGHT)
                self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                self.y = self.boss._position.get_y() + BOSS_HEIGHT
                position = bullet._position = Point(self.x, self.y)
                bullet.set_position(position)
                bullet._velocity = Point(-10, 10)
                self.boss_bullets.append(bullet)
                
                num_bullets = len(self.boss_bullets)
                #print(f"Number of boss bullets {num_bullets}")
                cast["boss_bullets"] = self.boss_bullets
