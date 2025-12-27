from datetime import timedelta

# represent 1 minute
minute = timedelta(minutes=1)
class Game:
    def __init__(self, current_score=0, current_level=0, current_time=minute):
        self.current_score = current_score
        self.current_level = current_level
        self.current_time = current_time