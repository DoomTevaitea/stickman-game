import pygame

def load_sounds():
    sounds = {
        'walk': pygame.mixer.Sound('walk_sound.wav'),
        'run': pygame.mixer.Sound('run_sound.wav'),
        'jump': pygame.mixer.Sound('jump_sound.wav'),
        'air': pygame.mixer.Sound('air_sound.wav'),
        'land': pygame.mixer.Sound('land_sound.wav')
    }
    return sounds

def create_channels():
    channels = {
        'walk': pygame.mixer.Channel(1),
        'run': pygame.mixer.Channel(2),
        'jump': pygame.mixer.Channel(3),
        'air': pygame.mixer.Channel(4),
        'land': pygame.mixer.Channel(5)
    }
    return channels
