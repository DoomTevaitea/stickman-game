import pygame
from settings import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT ,IMAGE_WIDTH , IMAGE_HEIGHT
from game_functions import create_rect_images, check_collisions
from sound_manager import load_sounds, create_channels
from obstacles import create_obstacles

# Initialisation de pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stickman Animation")

# Charger les images et sons
walk_images = create_rect_images((0, 255, 0), 6, IMAGE_WIDTH, IMAGE_HEIGHT)
run_images = create_rect_images((255, 0, 0), 6, IMAGE_WIDTH, IMAGE_HEIGHT)
jump_image = create_rect_images((0, 0, 255), 1, IMAGE_WIDTH, IMAGE_HEIGHT)[0]
sounds = load_sounds()
channels = create_channels()

# Variables pour gérer l'animation
x, y = 100, 600
velocity_y = 0
gravity = 0.5
on_ground = True
in_air = False
clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour et rendu du jeu
    # (logique de déplacement, dessin des images, gestion des sons, etc.)

    pygame.display.flip()
    clock.tick(70)  # Contrôle de la vitesse d'animation

pygame.quit()
