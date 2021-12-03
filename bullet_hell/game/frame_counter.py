class FrameCounter():
    def __init__(self):
        super().__init__()
        self.frame = 0

    def execute(self):
        self.frame += 1

    def get_frame_count(self):
        return self.frame
