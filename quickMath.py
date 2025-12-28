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
    problem_surface = font.render(problem_text, True, 'White')
    screen.blit(problem_surface, (350,200))
    

    time_surface = font.render(str(problem.current_time), True, 'Red')
    screen.blit(time_surface, (10,10))
    for index, choice in enumerate(problem.choices):
        choice_surface = font.render(str(choice), True, 'White')
        screen.blit(choice_surface, (350, 300+index * 50))
def draw_game(screen, game):
    score_surface = font.render(str(game.current_score), True, 'White')
    screen.blit(score_surface, (700,10))
    draw_problem(screen, game.current_problem)


test_game = Game()
 
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                test_game.submit_answer(0)
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                test_game.submit_answer(1)
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                test_game.submit_answer(2)
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
               test_game.submit_answer(3)
    # Fill background
    screen.fill(('black'))
    draw_game(screen, test_game)
     
    test_game.current_problem.update_time()
    test_game.check_time_up()
    # Update Display
    pygame.display.flip()

    # Limit fps
    clock.tick(60)