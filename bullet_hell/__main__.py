import os
from game.constants import BACKGROUND_X, BACKGROUND_Y, IMAGE_BACKGROUND
from game.constants import SOUND_MUSIC
from game.spawn_bullets_action import SpawnBulletsAction
from game.spawn_boss_bullets_action import SpawnBossBulletsAction
from game.constants import BOSS_HEIGHT, BOSS_WIDTH, BOSS_X, BOSS_Y
from game.constants import IMAGE_BOSS, PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_X, PLAYER_Y
from game.constants import IMAGE_PLAYER_SHIP

os.environ['RAYLIB_BIN_PATH'] = "."

from game.director import Director
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.frame_counter import FrameCounter
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.display_text_action import DisplayTextAction

from game.player import Player
from game.boss import Boss
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.background import Background

def main():
    # Initialize the Cast
    cast = {}

    # Create the boss here and add it to the list
    cast["boss"] = []
    bosses = []
    boss = Boss()
    boss.set_image(IMAGE_BOSS)
    boss.set_width(BOSS_WIDTH)
    boss.set_height(BOSS_HEIGHT)
    boss._position = Point(BOSS_X, BOSS_Y)
    boss.set_position(boss._position)
    bosses.append(boss)
    cast["boss"] = bosses


    cast["enemy"] = []
    # Initialize enemies
    enemies = []   
    cast["enemy"] = enemies

    # Initialize different bullet types
    cast["bullet"] = []
    cast["boss_bullet"] = []
    cast["bomb"] = []

    # Create a player ship here and add it to the list
    cast["player_ship"] = []
    

    player_ships = []
    player_ship = Player()
    player_ship.set_image(IMAGE_PLAYER_SHIP)
    player_ship.set_width(PLAYER_WIDTH)
    player_ship.set_height(PLAYER_HEIGHT)
    player_ship._position = Point(PLAYER_X, PLAYER_Y)
    player_ship.set_position(player_ship._position)
    player_ships.append(player_ship)
    cast["player_ship"] = player_ships

    cast["background"] = []

    backgrounds = []
    background = Background()
    background.set_image(IMAGE_BACKGROUND)
    background._position = Point(BACKGROUND_X, BACKGROUND_Y)
    background.set_position(background._position)
    backgrounds.append(background)
    cast["background"] = backgrounds



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
    spawn_bullets_action = SpawnBulletsAction()
    frame_counter = FrameCounter()
    spawn_boss_bullets_action = SpawnBossBulletsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    display_text_action = DisplayTextAction(output_service)

    # Running each action
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, spawn_bullets_action, frame_counter, spawn_boss_bullets_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action, display_text_action]

    # Start the game
    output_service.open_window("Bullet Niflheim")
    audio_service.start_audio()
    audio_service.play_sound(SOUND_MUSIC)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
