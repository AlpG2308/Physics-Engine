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
        #self.dy = 2*self.rect.centery-self.rect.centery+9.81*1/60
        self.prev_pos = [(self.screen.get_width()/2)-5,0+radius-10]
        self.vel_y = 0
        self.vel_x = 0

    def update(self):
        new_posy = 2 * self.rect.centery - self.prev_pos[1] + (1 * 0.2*0.2)
        new_posx = 2 * self.rect.centerx - self.prev_pos[0] + (0 * 0.2*0.2)
        self.vel_y = (new_posy + self.prev_pos[1])*0.5 * 0.2
        self.vel_x = 0
        self.prev_pos[0] = new_posx
        self.prev_pos[1] = new_posy
        self.rect.centery += self.vel_y
        self.rect.centerx += self.vel_x
        if self.rect.centery > self.screen.get_height():
            new_posy = self.screen.get_height()
            self.prev_pos[1] = new_posy + self.vel_y * 0.9
        print(self.vel_y)
