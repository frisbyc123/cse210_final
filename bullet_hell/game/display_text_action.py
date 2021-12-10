from game.constants import MAX_X
from game.constants import MAX_Y
from game.action import Action
import time

class DisplayTextAction(Action):

    def __init__(self, output_service):

        self._output_service = output_service

    def execute(self, cast):
        self.player = cast["player_ship"][0]
        self.boss = cast["boss"][0]

        self.boss_text = str(self.boss._health)
        self.player_text = str(self.player._health)
        self.player_text_two = "Player Health: "
        self.boss_text_two = "Boss Health: "
        self.game_over_text = "GAME OVER"
        self.player_died_text = "PLAYER DIED"
        self.boss_died_text = "BOSS DIED"
        self._output_service.clear_screen()

        self._output_service.draw_text(5, MAX_Y - 50, self.player_text_two, True)
        self._output_service.draw_text(153, MAX_Y - 50, self.player_text, True)
        self._output_service.draw_text(22, MAX_Y - 30, self.boss_text_two, True)
        self._output_service.draw_text(153, MAX_Y - 30, self.boss_text, True)

        if self.player._health <= 0:
            self._output_service.draw_text((MAX_X / 2) - 100, MAX_Y / 2, self.game_over_text, True)
            self._output_service.draw_text((MAX_X / 2) - 100, MAX_Y / 2 - 25, self.player_died_text, True)

        if self.boss._health <= 0:
            self._output_service.draw_text((MAX_X / 2) - 100, MAX_Y / 2, self.game_over_text, True)
            self._output_service.draw_text((MAX_X / 2) - 100, MAX_Y / 2 - 25, self.boss_died_text, True)



