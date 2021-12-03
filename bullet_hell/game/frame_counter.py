from game.action import Action


class FrameCounter(Action):
    """
    Used to control the actors from keyboard inputs.  
    """

    # Initialization #
    def __init__(self):
        super().__init__()
        self.frame = 0

    def execute(self, cast):
        self.frame += 1
        #print(f"Frame count: {self.frame}")
        return self.frame

