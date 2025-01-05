import pygame
from constants import *
import player
import circleshape







def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    frames = pygame.time.Clock()
    dt = 0
    
    spaceship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        screen.fill("black")
        spaceship.draw(screen)
        
        
        #end of iteration
        dt = frames.tick(60)/1000
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    







if __name__ == "__main__":
    main()