import pygame
class Weapon(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, pygame.Rect(x, y, w, h))

        