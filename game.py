from problem import *
class Game:
    def __init__(self, current_score=0, current_level=0):
        self.current_score = current_score
        self.current_level = current_level
        self.current_problem = self.generate_problem()
    
    def generate_problem(self):
        return Problem(random.randint(1,50),random.randint(1,50), random.choice(["+","-","/","*"]))

    def submit_answer(self, guess_index):
        if guess_index == self.current_problem.answer_index:
            self.current_score += 100
            self.current_problem = self.generate_problem()
        else:
            self.current_score -= 50
            self.current_problem = self.generate_problem()

    def check_time_up(self):
        if self.current_problem.current_time <= 0:
            self.current_score -= 50
            self.current_problem = self.generate_problem()

