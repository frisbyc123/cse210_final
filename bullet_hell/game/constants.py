import os

MAX_X = 1280
MAX_Y = 720
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_PLAYER_SHIP = os.path.join(os.getcwd(), "./bullet_hell/assets/player_filler.png")
IMAGE_BOSS = os.path.join(os.getcwd(), "./bullet_hell/assets/boss_filler.png")
IMAGE_BULLET = os.path.join(os.getcwd(), "./bullet_hell/assets/bullet_filler.png")
IMAGE_ENEMY_BULLET = os.path.join(os.getcwd(), "./bullet_hell/assests/enemy_bullet_filler.png")
IMAGE_BOMB = os.path.join(os.getcwd(), "./bullet_hell/assests/bomb_filler.png")

SOUND_SHOOT = os.path.join(os.getcwd(), "./bullet_hell/assets/mixkit-short-laser-gun-shot-1670.wav")
SOUND_MUSIC = os.path.join(os.getcwd(), "./batter/assets/game_music.wav")

SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_DX = 8
BALL_DY = BALL_DX * -1

# Player constants
PLAYER_X = MAX_X / 2
PLAYER_Y = MAX_Y - 25
PLAYER_WIDTH = 50 
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5 

# Boss constants
BOSS_WIDTH = 700
BOSS_HEIGHT = 70
BOSS_X = MAX_X / 2 - BOSS_WIDTH / 2
BOSS_Y = MAX_Y / 10

# Bullet constants
BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_SPEED = 10

# Bomb Constants
BOMB_WIDTH = 7
BOMB_HEIGHT = 7
BOMB_SPEED = 5
