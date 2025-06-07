import pygame

pygame.mixer.init()

# music
pygame.mixer.music.load("assets/music/orbital_colossus.mp3")
pygame.mixer.music.set_volume(0.5)

# game over
game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
game_over_sound.set_volume(1.0)

# shoot sound
shoot_sound = pygame.mixer.Sound("assets/sounds/shoot.wav")
shoot_sound.set_volume(0.5)

# explosion sound
explosion_big_sound = pygame.mixer.Sound("assets/sounds/big_explode.wav")
explosion_big_sound.set_volume(0.5)

explosion_medium_sound = pygame.mixer.Sound("assets/sounds/medium_explode.wav")
explosion_medium_sound.set_volume(0.5)

explosion_small_sound = pygame.mixer.Sound("assets/sounds/small_explode.wav")
explosion_small_sound.set_volume(0.5)

def start_background_music():
    pygame.mixer.music.play(-1, 0.0) # -1 loops

def stop_background_music():
    pygame.mixer.music.stop()

def play_game_over_sound():
    game_over_sound.play()

def play_shoot_sound():
    shoot_sound.play()

def play_explosion_sound(size):
    if size == "big":
        explosion_big_sound.play()
    elif size == "medium":
        explosion_medium_sound.play()
    else:
        explosion_small_sound.play()
