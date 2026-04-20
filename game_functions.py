import pygame
from settings import BLACK, GROUND_LEVEL

def create_rect_images(color, count, width, height):
    images = []
    for i in range(count):
        image = pygame.Surface((width, height))
        image.fill(color)
        pygame.draw.rect(image, BLACK, image.get_rect(), 2)  # Dessiner une bordure noire
        images.append(image)
    return images

def check_collisions(x, y, width, height, obstacles, velocity_y):
    new_y = y + velocity_y
    colliding_obstacle = None
    for obstacle in obstacles:
        predicted_rect = pygame.Rect(x, new_y, width, height)
        if predicted_rect.colliderect(obstacle):
            colliding_obstacle = obstacle
            break
    return new_y, colliding_obstacle
