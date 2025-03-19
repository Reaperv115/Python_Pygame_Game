import pygame 
import random 

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500

# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 


pygame.init() 

RED = (255, 0, 0) 

size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Creating Sprite") 

all_sprites_list = pygame.sprite.Group() 

objectWidth = 20
objectHeight = 30
object_ = Sprite(RED, objectWidth, objectHeight) 
object_.rect.x = screen.get_width()/2
object_.rect.y = screen.get_height()-objectHeight

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
