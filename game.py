import sys

import pygame

from scripts.entities import PhysicsEntity

from scripts.utility import load_image

class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Ducky Jump")

        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

    def run(self): 
        while True:
            self.display.fill((14,219,248))
            
            self.player.update((self.movement[2] - self.movement[3], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        self.movement[2] = True
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        self.movement[2] = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        self.movement[3] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()