import pygame
import math
Black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self,color, x_coor,y_coor, radius,screen):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface([x_coor,y_coor])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        #Draw the ball
        pygame.draw.circle(self.image, color, [x_coor//2, y_coor//2],radius)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.center = (self.screen.get_width()//2,0+radius+10)#Pos at time = 0
        self.prev_pos = [self.screen.get_width()/2,0+radius]
        self.acc = 10 * (0.5*0.5) #pygame rect class only accepts integers so only integer values are possible -> a*delta_t**2
                                    # use 1/60 to adjust for framerate

    def update(self):
        v_y = int(self.rect.centery - self.prev_pos[1])
        v_x = int(self.rect.centerx - self.prev_pos[0])
        self.prev_pos[0] = self.rect.centerx
        self.prev_pos[1] = self.rect.centery
        p_y = self.rect.centery + v_y
        p_x = self.rect.centerx + v_x
        p_y += self.acc
        print(self.rect.centery, self.prev_pos[1],v_y, v_x,self.acc)
        self.rect.center=(p_x,p_y)

        if self.rect.centery + self.radius>= self.screen.get_height()-self.radius:
            self.rect.centery = self.screen.get_height()-self.radius
            self.prev_pos[1] = self.rect.centery + v_y*0.9
        if self.rect.centery - self.radius <= 0 + self.radius:
            self.rect.centery = 0+self.radius
            self.prev_pos[1] = self.rect.centery + v_y*0.9

