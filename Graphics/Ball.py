import pygame
from random import randint

BLACK = (0,0,0)
WIDTH = 1280
HEIGT = 720

class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
        
    def reset(self):
        self.rect.x = WIDTH/2
        self.rect.y = HEIGT/2
        self.velocity = [randint(4,8),randint(-8,8)]