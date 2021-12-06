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
from game.audio_service import AudioService
import random

class SpawnBossBulletsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.boss_bullets = []
        self.frame_counter = FrameCounter()
        self.audio_service = AudioService()
        self.frame = 0
        self.fire_rate = 5
        self.fire_pattern = 0

    def execute(self, cast):
        #self.input_service = InputService()
        self.boss = cast["boss"][0]

        self.will_fire = random.randint(0, 10)
        if self.will_fire % 2 == 0:
            self.fire_one = 1
        else:
            self.fire_one = 0

        if self.will_fire % 3 == 0:
            self.fire_two = 1
        else:
            self.fire_two = 0

        if self.will_fire % 4 == 0:
            self.fire_three = 1
        else:
            self.fire_three = 0

        self.frame = self.frame_counter.execute(cast)
        #print(f"frame count: {self.frame}")
        
        if self.fire_one:
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
                self.audio_service.play_sound(constants.SOUND_SHOOT)
                self.boss_bullets.append(bullet)

        if self.fire_two:
            if self.frame % self.fire_rate == 0:
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
                self.audio_service.play_sound(constants.SOUND_SHOOT)
                self.boss_bullets.append(bullet)

        if self.fire_three:
            if self.frame % self.fire_rate == 0:        
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
                self.audio_service.play_sound(constants.SOUND_SHOOT)
                self.boss_bullets.append(bullet)
                
                num_bullets = len(self.boss_bullets)
                #print(f"Number of boss bullets {num_bullets}")
                cast["boss_bullet"] = self.boss_bullets
        """if frame_counter % 360 == 0:
            self.fire_pattern = random.randint(0, 3)
            if self.fire_pattern == 0:
                pass
            elif self.fire_pattern == 1:
                pass
            elif self.fire_pattern == 2:
                pass
            elif self.fire_pattern == 3:
                pass"""

