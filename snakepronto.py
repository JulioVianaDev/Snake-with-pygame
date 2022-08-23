from msilib.schema import Directory
import pygame
import time 
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.init()
pygame.display.set_caption('Em busca do Tomate')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock() 
snake_position = [100,50]
snake = [ [100, 50],
          [90, 50],
          [80, 50],
          [70, 50],
        ]
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
direction = 'RIGHT'            
change_to = direction
score = 0
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
