import pygame
import sys
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
Shot.containers = (updatable, drawable, shots)

AsteroidField.containers = (updatable,)

clock = pygame.time.Clock()
dt = 0

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
astroidfield = AsteroidField()


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    log_state()

    updatable.update(dt)
    for asteroid in asteroids:
        if player.collides_with(asteroid):
            log_event("player_hit")
            print("Game over!")
            sys.exit()
        
        for shot in shots:
            if shot.collides_with(asteroid):
                log_event("asteroid_shot")
                shot.kill()
                asteroid.split()
        

    screen.fill((0, 0, 0))
    for sprite in drawable:
        sprite.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000  # Limit to 60 FPS
    #print(f"Delta time for this frame: {dt} seconds")

pygame.quit()
sys.exit()