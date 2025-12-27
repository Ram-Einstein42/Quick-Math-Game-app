import random
import pygame


class Problem:
    def __init__(self, num1, num2, operation): 
        self.num1 = num1
        self.num2 = num2
        self.operation = operation # can be "-", "+," "/", "*" 
        self.answer = self.get_answer()
        self.choices = self.generate_choices()
        self.answer_index = self.choices.index(self.answer)
         


    def get_answer(self):

        if self.operation == "+":
            return self.num1 + self.num2
        elif self.operation == "-":
            return self.num1 - self.num2
        elif self.operation == "*":
            return self.num1 * self.num2
        elif self.operation == "/":
            return self.num1 / self.num2
        else:
            raise ValueError("invalid operation")
    
    def generate_choices(self):
        options = [self.answer, self.answer+2, self.answer+3, self.answer+4]
        random.shuffle(options)

        return options

     
