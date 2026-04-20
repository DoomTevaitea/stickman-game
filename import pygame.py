import pygame
import os
import sys

# Initialisation de pygame
pygame.init()

# Définition des couleurs et des dimensions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)
size = (1500, 900)
GROUND_LEVEL = 900 - 150

# Création de la fenêtre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stickman Animation avec Vidéo en Arrière-Plan")

# Définir si les animations de fond doivent être chargées (0 = non, 1 = oui)
load_background_anim = 1  # Changez cette valeur à 0 si vous ne voulez pas charger les animations de fond

frames = []
if load_background_anim == 1:
    # Charger les frames de la vidéo
    frames = [pygame.image.load(f'image/decomposition fond/frame{i}.jpg') for i in range(1, 329)]

# Fonction pour créer des images animées
def create_rect_images(color, count, width, height):
    images = []
    for i in range(count):
        image = pygame.Surface((width, height))
        image.fill(color)
        pygame.draw.rect(image, BLACK, image.get_rect(), 2)
        images.append(image)
    return images

# Création des animations
height = 70
width = 30
walk_images = create_rect_images(GREY, 6, width, height)
run_images = create_rect_images(RED, 6, width, height)
jump_image = create_rect_images(BLUE, 1, width, height)[0]

# Chargement des sons
walk_sound = pygame.mixer.Sound('sons/walk_sound.wav')
run_sound = pygame.mixer.Sound('sons/run_sound.wav')
jump_sound = pygame.mixer.Sound('sons/jump_sound.wav')
air_sound = pygame.mixer.Sound('sons/air_sound.wav')
land_sound = pygame.mixer.Sound('sons/land_sound.wav')

# Variables pour gérer l'animation
x, y = 100, GROUND_LEVEL - height  # Position de départ ajustée
velocity_y = 0
gravity = 0.5
on_ground = True
in_air = False
clock = pygame.time.Clock()
walk_index = 0
run_index = 0
WALK_SPEED = 5
RUN_SPEED = 10
speed = WALK_SPEED  # Vitesse initiale définie pour la marche

# Définir les obstacles
obstacles = [
    pygame.Rect(0, GROUND_LEVEL - 100, 1500, 50),  # sol
    pygame.Rect(0, GROUND_LEVEL - 100, 200, 300),  # les 2 ponts
    pygame.Rect(1300, GROUND_LEVEL - 100, 200, 300),
    pygame.Rect(300, GROUND_LEVEL - 300, 200, 50),
    pygame.Rect(650, GROUND_LEVEL - 400, 200, 50),
    pygame.Rect(1000, GROUND_LEVEL - 300, 200, 50)
]

# Création des canaux pour les sons
walk_channel = pygame.mixer.Channel(1)
run_channel = pygame.mixer.Channel(2)
jump_channel = pygame.mixer.Channel(3)
air_channel = pygame.mixer.Channel(4)
land_channel = pygame.mixer.Channel(5)

# Boucle principale
running = True
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Assurer que des frames sont disponibles avant de les afficher
    if frames:  # Vérifie si la liste des frames n'est pas vide
        screen.blit(frames[frame_count % len(frames)], (0, 0))
        frame_count = (frame_count + 1) % len(frames)

    # Gestion des entrées clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        x -= speed
        if not run_channel.get_busy():
            run_channel.play(run_sound)
        is_running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        is_walking = not is_running
        speed = RUN_SPEED if is_running else WALK_SPEED
    elif keys[pygame.K_d]:
        x += speed
        if not walk_channel.get_busy():
            walk_channel.play(walk_sound)
        is_running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        is_walking = not is_running
        speed = RUN_SPEED if is_running else WALK_SPEED
    else:
        is_running = False
        is_walking = False
        walk_channel.stop()
        run_channel.stop()

    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = -15
        on_ground = False
        in_air = True
        if not jump_channel.get_busy():
            jump_channel.play(jump_sound)

    # Appliquer la gravité et gérer les collisions
    velocity_y += gravity
    y += velocity_y
    colliding_obstacle = None
    for obstacle in obstacles:
        if pygame.Rect(x, y, width, height).colliderect(obstacle):
            if velocity_y > 0:
                y = obstacle.top - height
                velocity_y = 0
                on_ground = True
                in_air = False
                if not land_channel.get_busy():
                    land_channel.play(land_sound)
            elif velocity_y < 0:
                y = obstacle.bottom
                velocity_y = 0

    # Dessiner les obstacles et le personnage
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREY, obstacle)
    current_image = jump_image if not on_ground else run_images[run_index] if is_running else walk_images[walk_index] if is_walking else walk_images[0]
    screen.blit(current_image, (x, y))
    if is_running:
        run_index = (run_index + 1) % len(run_images)
    if is_walking:
        walk_index = (walk_index + 1) % len(walk_images)

    pygame.display.flip()
    clock.tick(60)  # Contrôle de la vitesse d'animation

pygame.quit()
