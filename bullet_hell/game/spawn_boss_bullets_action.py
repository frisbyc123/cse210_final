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
        self.fire_pattern = random.randint(0, 3)
        self.fire = 0
        self.fire_angle = -50
        self.fire_angle_two = 50

    def execute(self, cast):
        #self.input_service = InputService()
        self.boss = cast["boss"][0]
        self.frame = self.frame_counter.execute(cast)
      
        if self.frame % 360 == 0:
            self.fire_pattern = random.randint(0, 3)
            
        if self.fire_pattern == 0:
            if self.frame % self.fire_rate == 0:
                self.fire = random.randint(0, 1)
                if self.fire:
                    # Center Bullet
                    bullet = EnemyBullet()
                    bullet.set_image(IMAGE_BULLET)
                    bullet.set_width(BULLET_WIDTH)
                    bullet.set_height(BULLET_HEIGHT)
                    self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                    self.y = self.boss._position.get_y() + BOSS_HEIGHT
                    position = bullet._position = Point(self.x, self.y)
                    bullet.set_position(position)
                    bullet._velocity = Point(0, 10)
                    self.audio_service.play_sound(constants.SOUND_SHOOT)
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
                    self.audio_service.play_sound(constants.SOUND_SHOOT)
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
                    self.audio_service.play_sound(constants.SOUND_SHOOT)
                    self.boss_bullets.append(bullet)
                    
                    cast["boss_bullet"] = self.boss_bullets

        elif self.fire_pattern == 1:
             if self.frame % self.fire_rate == 0:
                self.fire = 1
                if self.fire:
                    bullet = EnemyBullet()
                    bullet.set_image(IMAGE_BULLET)
                    bullet.set_width(BULLET_WIDTH)
                    bullet.set_height(BULLET_HEIGHT)
                    self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                    self.y = self.boss._position.get_y() + BOSS_HEIGHT
                    position = bullet._position = Point(self.x, self.y)
                    bullet.set_position(position)
                    bullet._velocity = Point(self.fire_angle, 10)
                    self.audio_service.play_sound(constants.SOUND_SHOOT)
                    self.boss_bullets.append(bullet)
                    self.fire_angle += 1
                    if self.fire_angle >= 50:
                        self.fire_angle = -50

                    cast["boss_bullet"] = self.boss_bullets 

        elif self.fire_pattern == 2:
            if self.frame % self.fire_rate == 0:
                self.fire = 1
                if self.fire:
                    bullet = EnemyBullet()
                    bullet.set_image(IMAGE_BULLET)
                    bullet.set_width(BULLET_WIDTH)
                    bullet.set_height(BULLET_HEIGHT)
                    self.x = self.boss._position.get_x() + (BOSS_WIDTH / 2)
                    self.y = self.boss._position.get_y() + BOSS_HEIGHT
                    position = bullet._position = Point(self.x, self.y)
                    bullet.set_position(position)
                    bullet._velocity = Point(self.fire_angle_two, 10)
                    self.audio_service.play_sound(constants.SOUND_SHOOT)
                    self.boss_bullets.append(bullet)
                    self.fire_angle_two -= 1
                    if self.fire_angle_two <= -50:
                        self.fire_angle_two = 50

                    cast["boss_bullet"] = self.boss_bullets 
        elif self.fire_pattern == 3:
            pass

