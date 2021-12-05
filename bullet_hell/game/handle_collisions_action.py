from game.constants import SOUND_BOUNCE
#from game import audio_service
from game import constants
from game.action import Action
from game.point import Point
from game.physics_service import PhysicsService
from game.player import Player
from game.boss import Boss
#from game.audio_service import AudioService
import random

class HandleCollisionsAction(Action):
    """
    Handles collisions of the between actors
    """
    
    # Initializtion #
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        #self.audio_service = AudioService()
        
    # checks if the ball and paddle have colided, then multiplies the ball's y velocity by -1 
    # Then checks if the ball has collided with a brick.  If it does, it deletes the brick and
    # bounces the ball back
    def execute(self, cast):
        self.player = cast["player_ship"][0]
        self.boss = cast["boss"][0]
        self.player_bullets = cast["bullet"]
        self.boss_bullets = cast["boss_bullet"]

        for bullet in self.boss_bullets:
            if self._physics_service.is_collision(bullet, self.player):
                self.player._health -= 10
                print(f"Player hit! Player Health: {self.player._health}")
                self.boss_bullets.remove(bullet)

        for bullet in self.player_bullets:
            if self._physics_service.is_collision(bullet, self.boss):
                self.boss._health -= 5
                print(f"Boss hit! Boss Health: {self.boss._health}")
                cast["bullet"].remove(bullet)

        if self._physics_service.is_collision(self.player, self.boss):
            self.player._health = 0
            print(f"Player hit! Player Health: {self.player._health}")