from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """
    Moves actors according to their velocity.
    """
    def __init__(self, output_service):

        self._output_service = output_service

    def execute(self, cast):
        for group in cast.values():
                    for actor in group:
                        if not actor.get_velocity().is_zero():
                            self._move_actor(actor)
    
    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        x = (x + dx) #% constants.MAX_X
        y = (y + dy) #% constants.MAX_Y
        
        position = Point(x, y)
        actor.set_position(position)
