import os
os.environ['RAYLIB_BIN_PATH'] = "."

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
#from game.brick import Brick
#from game.ball import Ball
#from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["enemy"] = []
    # Create enemies here and add them to the list
    enemies = []   
    cast["enemy"] = enemies

    #for brick in cast["bricks"]:
    #    print(f"x position {brick._position.get_x()}")
    #    print(f"y position {brick._position.get_y()}")

    cast["bullet"] = []
    # Create a bullets here and add it to the list
    bullets = []
    #ball = Ball()
    #ball.set_image(IMAGE_BALL)
    #ball.set_width(BALL_WIDTH)
    #ball.set_height(BALL_HEIGHT)
    #x = MAX_X / 2
    #y = MAX_Y / 2
    #position = Point(x, y)
    #ball.set_position(position)
    #balls.append(ball)
    cast["bullet"] = bullets
    
    cast["player_ship"] = []
    # TODO: Create a player ship here and add it to the list

    player_ships = []
    #player_ship = player_ship()
    #paddle.set_image(IMAGE_PADDLE)
    #paddle.set_width(PADDLE_WIDTH)
    #paddle.set_height(PADDLE_HEIGHT)
    #position = Point(PADDLE_X, PADDLE_Y)
    #paddle.set_position(position)
    #paddles.append(paddle)
    cast["player_ship"] = player_ships


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    move_actors_action = MoveActorsAction(output_service)
    handle_off_screen_action = HandleOffScreenAction()
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Bullet Hell")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
