import pygame 
import random 

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
colorKey = (255, 255, 255)
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500


class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.surface = pygame.Surface([width, height])
		self.image = pygame.image.load("space invaders player.png")
		if self.image.get_alpha():
			self.image.convert_alpha()
		else:
			self.image.convert(self.image)
			self.surface.set_colorkey(colorKey)
		pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()


pygame.init() 

white = (255, 255, 255) 

size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Creating Sprite") 

all_sprites_list = pygame.sprite.Group() 

objectWidth = 5
objectHeight = 10
object_ = Sprite(white, objectWidth, objectHeight) 
object_.rect.x = screen.get_width()/2
object_.rect.y = screen.get_height()/2

all_sprites_list.add(object_) 

exit = True
clock = pygame.time.Clock() 

while exit: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = False

	#all_sprites_list.update() 
	screen.fill(SURFACE_COLOR) 
	all_sprites_list.draw(screen) 
	pygame.display.flip() 
	clock.tick(60) 

pygame.quit() 
