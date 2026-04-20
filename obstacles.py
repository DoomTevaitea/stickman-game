import pygame
from settings import GROUND_LEVEL, SCREEN_WIDTH

def create_obstacles():
    return [
        pygame.Rect(0, GROUND_LEVEL - 100, SCREEN_WIDTH, 50),  # sol
        pygame.Rect(0, GROUND_LEVEL - 100, 200, 300),          # les 2 ponts
        pygame.Rect(1300, GROUND_LEVEL - 100, 200, 300),       #
        pygame.Rect(300, GROUND_LEVEL - 300, 200, 50),
        pygame.Rect(650, GROUND_LEVEL - 400, 200, 50),
        pygame.Rect(1000, GROUND_LEVEL - 300, 200, 50)
    ]
