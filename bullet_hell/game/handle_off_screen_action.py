from game.constants import PLAYER_HEIGHT
from game.constants import PLAYER_WIDTH
from game.constants import BOSS_WIDTH
from game.director import Director
from game.constants import MAX_X, MAX_Y
from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    """
    Checks if bullets have left the screen. 
    If they have, they get deleted.
    """

    def __init__(self):
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_position = 0
        self.y_position = 0
        #self.director = Director()

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                #player bullet removal on screen sides
                if actor.get_type() == "player_bullet":
                    if actor._position.get_x() < 0 or actor._position.get_x() > MAX_X:
                        group.remove(actor)
                    elif actor._position.get_y() < 0 or actor._position.get_y() > MAX_Y:
                        group.remove(actor)
                #enemy bullet removal on screen sides
                elif actor.get_type() == "enemy_bullet":
                    if actor._position.get_x() < 0 or actor._position.get_x() > MAX_X:
                        group.remove(actor)
                    elif actor._position.get_y() < 0 or actor._position.get_y() > MAX_Y:
                        group.remove(actor)
                #boss edge detection.  Reverses the direction when touches an edge
                if actor.get_type() == "boss":
                    if actor._position.get_x() < 0 or actor._position.get_x() + BOSS_WIDTH > MAX_X:
                        self.x_velocity = actor._velocity.get_x() * -1
                        actor._velocity = Point(self.x_velocity, 0)
                #player edge detection.  Prevents the player from leaving window
                if actor.get_type() == "player":
                    #Left Side
                    if actor._position.get_x() <= 0:
                        self.y_position = actor._position.get_y()
                        print(f"x_position in off screen: {self.x_position}")
                        actor._position = Point(0, self.y_position)
                    #Right Side    
                    elif actor._position.get_x() + PLAYER_WIDTH > MAX_X:
                        self.y_position = actor._position.get_y()
                        self.x_position = MAX_X - PLAYER_WIDTH
                        print(f"x_position in off screen: {self.x_position}")
                        actor._position = Point(self.x_position, self.y_position)
                    #Top
                    elif actor._position.get_y() <= 0:
                        self.x_position = actor._position.get_x()
                        print(f"y_position in off screen: {self.y_position}")
                        actor._position = Point(self.x_position, 0)
                    #Bottom    
                    elif actor._position.get_y() + PLAYER_WIDTH > MAX_Y:
                        self.x_position = actor._position.get_x()
                        self.y_position = MAX_Y - PLAYER_HEIGHT
                        print(f"y_position in off screen: {self.y_position}")
                        actor._position = Point(self.x_position, self.y_position)
                        
