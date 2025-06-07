import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
import audio

# Game states
GAME_PLAYING = 0
GAME_OVER = 1

def draw_text(screen, text, size, color, x, y, center=True):
    """Helper function to draw text on screen"""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    else:
        screen.blit(text_surface, (x, y))

def draw_game_over_screen(screen, score):
    """Draw the game over screen"""
    # Semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    # Game Over text
    draw_text(screen, "GAME OVER", 72, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    
    # Final score
    draw_text(screen, f"Final Score: {score}", 48, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
    
    # Instructions
    draw_text(screen, "Press R to play again or ESC to quit", 36, (200, 200, 200), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

def reset_game():
    audio.start_background_music()

    """Reset all game objects for a new game"""
    # Clear all sprite groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Recreate player
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Recreate asteroid field
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    asteroid_field = AsteroidField()

    # Set bullet containers
    Bullet.containers = (bullets, updatables, drawables)

    return updatables, drawables, asteroids, bullets, player, asteroid_field

def main():
    pygame.init()
    pygame.font.init()  # Initialize font module
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    game_state = GAME_PLAYING
    score = 0
    clock = pygame.time.Clock()

    # Initialize game objects
    updatables, drawables, asteroids, bullets, player, asteroid_field = reset_game()

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if game_state == GAME_OVER:
                    if event.key == pygame.K_r:
                        # Restart game
                        game_state = GAME_PLAYING
                        score = 0
                        updatables, drawables, asteroids, bullets, player, asteroid_field = reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        return

        # Clear screen
        screen.fill((0, 0, 0))

        if game_state == GAME_PLAYING:
            # Update game objects
            updatables.update(dt)

            # Check collision between player and asteroids
            for asteroid in asteroids:
                if asteroid.is_colliding(player):
                    print("Game over!")
                    print(f"Final Score: {score}")
                    audio.stop_background_music()
                    audio.play_game_over_sound()
                    game_state = GAME_OVER
                    break
            
            # Check collision between bullets and asteroids
            for asteroid in asteroids:
                for bullet in bullets:
                    if bullet.is_colliding(asteroid):
                        asteroid.split()
                        bullet.kill()
                        score += 1

            # Draw all game objects
            for drawable in drawables:
                drawable.draw(screen)

            # Draw current score during gameplay
            draw_text(screen, f"Score: {score}", 36, (255, 255, 255), 100, 30, center=False)

        elif game_state == GAME_OVER:
            # Still draw the game objects in background
            for drawable in drawables:
                drawable.draw(screen)

            # Draw game over screen on top
            draw_game_over_screen(screen, score)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
