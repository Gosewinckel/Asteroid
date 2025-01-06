import pygame
from constants import *
import player
import circleshape
import asteroidfield
import asteroid
import shot

def main():
    # game start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    frames = pygame.time.Clock()
    dt = 0
    # groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updateable, drawable)    
    spaceship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updateable, drawable)
    asteroidfield.AsteroidField.containers = (updateable,)
    hazards = asteroidfield.AsteroidField()

    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updateable, drawable)

    # game loop 
    while True:
        screen.fill("black")
        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.collision(spaceship):
                print("Game over!")
                pygame.quit()
        
        #end of iteration
        dt = frames.tick(60)/1000
        pygame.display.flip()
        
        #quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    
if __name__ == "__main__":
    main()