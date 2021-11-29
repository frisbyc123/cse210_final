import os

MAX_X = 1280
MAX_Y = 720
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_PLAYER_SHIP = os.path.join(os.getcwd(), "./bullet_hell/assets/player_filler.png")
IMAGE_BOSS = os.path.join(os.getcwd(), "./bullet_hell/assets/boss_filler.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PLAYER_X = MAX_X / 2
PLAYER_Y = MAX_Y - 25

PLAYER_WIDTH = 50 
PLAYER_HEIGHT = 50

BOSS_X = MAX_X / 2
BOSS_Y = MAX_Y / 10

BOSS_WIDTH = 700
BOSS_HEIGHT = 70

PLAYER_SPEED = 10

