import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    log_state()

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()