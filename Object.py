import pygame
import math
Black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self,color, x_coor,y_coor, radius,screen):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([x_coor,y_coor])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        #Draw the ball
        pygame.draw.circle(self.image, color, [x_coor//2, y_coor//2],radius)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.center = (self.screen.get_height()//2,0+radius)#Pos at time = 0
        self.dy = 2*self.rect.centery-self.rect.centery+9.81*1/60



    def update(self):
        self.rect.centery += self.dy
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.dy *= -1

