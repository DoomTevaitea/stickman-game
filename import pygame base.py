import pygame
import os

# Initialisation de pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200,200,200)


# Définition des dimensions de la fenêtre
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
GROUND_LEVEL = SCREEN_HEIGHT - 150

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stickman Animation")

# Simulation des images d'animation avec des rectangles
def create_rect_images(color, count, width, height):
    images = []
    for i in range(count):
        image = pygame.Surface((width, height))
        image.fill(color)
        pygame.draw.rect(image, BLACK, image.get_rect(), 2)  # Dessiner une bordure noire
        images.append(image)
    return images

walk_images = create_rect_images((0, 255, 0), 6, 50, 100)  # Rectangles verts pour la marche
run_images = create_rect_images((255, 0, 0), 6, 50, 100)   # Rectangles rouges pour la course
jump_image = create_rect_images((0, 0, 255), 1, 50, 100)[0]  # Rectangle bleu pour le saut

# Chargement des sons
walk_sound = pygame.mixer.Sound('sons/walk_sound.wav')  # Remplacer par le chemin correct de votre fichier son
run_sound = pygame.mixer.Sound('sons/run_sound.wav')    # Remplacer par le chemin correct de votre fichier son
jump_sound = pygame.mixer.Sound('sons/jump_sound.wav')  # Son pour le saut initial
air_sound = pygame.mixer.Sound('sons/air_sound.wav')    # Son pour le temps passé en l'air
land_sound = pygame.mixer.Sound('sons/land_sound.wav')  # Remplacer par le chemin correct de votre fichier son

# Variables pour gérer l'animation
x, y = SCREEN_WIDTH // 2, GROUND_LEVEL
velocity_y = 0
gravity = 0.5
on_ground = True
in_air = False
clock = pygame.time.Clock()
walk_index = 0
run_index = 0
speed = 5
is_running = False
is_walking = False

# Ajout des obstacles
obstacles = [
    pygame.Rect(0, GROUND_LEVEL --100,SCREEN_WIDTH , 50), #sol
    pygame.Rect(0, GROUND_LEVEL - 100, 200, 300),
    pygame.Rect(1300, GROUND_LEVEL - 100, 200, 300)
]

# Création des canaux pour les sons
walk_channel = pygame.mixer.Channel(1)
run_channel = pygame.mixer.Channel(2)
jump_channel = pygame.mixer.Channel(3)
air_channel = pygame.mixer.Channel(4)
land_channel = pygame.mixer.Channel(5)

# Boucle principale
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    is_walking = False
    is_running = False

    if keys[pygame.K_q]:
        x -= speed
        is_running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        is_walking = not is_running
    elif keys[pygame.K_d]:
        x += speed
        is_running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        is_walking = not is_running
    
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = -15
        on_ground = False
        in_air = True
        if not jump_channel.get_busy():
            jump_channel.play(jump_sound)

    # Appliquer la gravité
    velocity_y += gravity
    y += velocity_y

    # Vérifier si le stickman touche le sol
    if y >= GROUND_LEVEL:
        if not on_ground:  # Jouer le son d'atterrissage seulement lorsque le stickman touche le sol
            land_channel.play(land_sound)
            in_air = False
            air_channel.stop()  # Arrêter le son d'air lorsqu'il atterrit
        y = GROUND_LEVEL
        velocity_y = 0
        on_ground = True

    # Gérer les collisions avec les obstacles
    stickman_rect = pygame.Rect(x, y, 50, 100)
    for obstacle in obstacles:
        if stickman_rect.colliderect(obstacle):
            if velocity_y > 0:  # Collisions en tombant
                y = obstacle.top - 100
                velocity_y = 0
                on_ground = True
                in_air = False
                air_channel.stop()  # Arrêter le son d'air lorsqu'il atterrit sur un obstacle
    
    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREY, obstacle)

    # Dessiner l'animation et jouer les sons
    if not on_ground:
        screen.blit(jump_image, (x, y))
        walk_channel.stop()
        run_channel.stop()
        if not air_channel.get_busy() and in_air:
            air_channel.play(air_sound)
    elif is_running:
        screen.blit(run_images[run_index], (x, y))
        run_index = (run_index + 1) % len(run_images)
        speed = 10
        if not run_channel.get_busy():
            run_channel.play(run_sound)
        walk_channel.stop()  # Arrêter le son de marche
        jump_channel.stop()  # Arrêter le son de saut
    elif is_walking:
        screen.blit(walk_images[walk_index], (x, y))
        walk_index = (walk_index + 1) % len(walk_images)
        speed = 5
        if not walk_channel.get_busy():
            walk_channel.play(walk_sound)
        run_channel.stop()  # Arrêter le son de course
        jump_channel.stop()  # Arrêter le son de saut
    else:
        screen.blit(walk_images[0], (x, y))  # Afficher la première image de marche à l'arrêt
        walk_channel.stop()
        run_channel.stop()
        jump_channel.stop()
        air_channel.stop()
    
    pygame.display.flip()
    clock.tick(50)  # Contrôle de la vitesse d'animation

pygame.quit()