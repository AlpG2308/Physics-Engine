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
        self.prev_pos = [self.screen.get_width()/2,0+radius-5]


    def update(self):
        new_posy = int(2 * self.rect.centery - self.prev_pos[1] + 9.81 * 0.5*0.5)
        new_posx = int(2 * self.rect.centerx - self.prev_pos[0] + 0 * 0.5*0.5)
        v_y = new_posy - self.prev_pos[1]
        v_x = new_posx - self.prev_pos[0]
        print(self.rect.centery, new_posy, self.prev_pos[1], v_y)
        self.prev_pos[0] = new_posx
        self.prev_pos[1] = new_posy
        self.rect.center = (new_posx,new_posy)
        if self.rect.bottom > self.screen.get_height():
            new_posy = self.screen.get_height()
            self.rect.bottom= new_posy
            self.prev_pos[1] = new_posy + v_y
        if self.rect.top < 0:
            new_posy = 0
            self.prev_pos[1] = new_posy + v_y


