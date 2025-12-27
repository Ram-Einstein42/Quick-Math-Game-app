import pygame, sys
from game import *
from problem import *
import random

 

# Initialize
pygame.init()

# Font
font = pygame.font.SysFont("arial", 40)

# Screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Quick Math")

# Clock
clock = pygame.time.Clock()

def draw_problem(screen, problem):
    problem_text = f"{problem.num1} {problem.operation} {problem.num2}"
    problem_surface = font.render(problem_text, True, 'Red')
    screen.blit(problem_surface, (350,200))

    for index, choice in enumerate(problem.choices):
        choice_surface = font.render(str(choice), True, 'Black')
        screen.blit(choice_surface, (350, 300+index * 50))

quick_problem = Problem(1,2,"+")
quick_problem2 = Problem(random.randint(1,50),random.randint(1,50), random.choice(["+","-","/","*"]))
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Fill background
    screen.fill((30, 30, 30))
    draw_problem(screen, quick_problem2)

    # Update Display
    pygame.display.flip()

    # Limit fps
    clock.tick(60)