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
        self.rect.center = (self.screen.get_width()//2,0+radius)#Pos at time = 0
        self.prev_pos = [(self.screen.get_width()/2)-5,0+radius-5]


    def update(self):
        new_posy = 2 * self.rect.centery - self.prev_pos[1] + (9.81 * 0.5*0.5)
        #new_posx = 2 * self.rect.center - self.prev_pos[0] + (0 * 0.2*0.2)
        self.rect.centery += new_posy - self.prev_pos[1]
        v_y = new_posy - self.prev_pos[0]
        #self.rect.centerx += new_posx - self.prev_pos[0]
        #self.prev_pos[0] = new_posx
        self.prev_pos[1] = new_posy
        if self.rect.centery >= self.screen.get_height():
            new_posy = self.screen.get_height()
            self.prev_pos[1] = new_posy + v_y * 0.9

        elif self.rect.centery <= 0.0:
            new_posy = 0.0
            self.prev_pos[1] = new_posy + v_y * 0.9
        print (v_y)

