import pygame
import math
Black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self,color, x_coor,y_coor, radius,screen):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([x_coor+radius,y_coor+radius])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        #Draw the ball
        pygame.draw.circle(self.image, color, [x_coor, y_coor],radius)
        self.rect = self.image.get_rect()
        self.screen = screen

        self.prev_pos = [self.rect.centerx,self.rect.centery +10]
        self.acc = 9.81 #pygame rect class only accepts integers so only integer values are possible
        #self.friction = 0.999

    def update(self,acc):
        self.acc = acc
        v_y = self.rect.centery - self.prev_pos[1]
        v_x = self.rect.centerx - self.prev_pos[0]
        self.prev_pos[0] = self.rect.centerx
        self.prev_pos[1] = self.rect.centery
        p_y = self.rect.centery + v_y
        p_x = self.rect.centerx + v_x
        p_y += self.acc
        print(self.rect.centery, self.prev_pos[1],v_y, v_x)
        self.rect.center=(p_x,p_y)

        if self.rect.centery >= self.screen.get_height():
            self.rect.centery = self.screen.get_height()
            self.prev_pos[1] = self.rect.centery + v_y*0.9
        if self.rect.centery <= 0.0:
            self.rect.centery = 0
            self.prev_pos[1] = self.rect.centery + v_y*0.9

class Mesh(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self,color,x_coor,y_coor, distance_x,distance_y,screen):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([x_coor+distance_x,y_coor+distance_y])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        #Draw the ball

        image1 = pygame.draw.rect(self.image, color, (x_coor,y_coor,distance_x,distance_y))
        images = [image1]
        image2 = pygame.draw.rect(self.image, color, (images[0].midright[0], images[0].midright[1], distance_x, distance_y))
        self.rect = self.image.get_rect()
        self.screen = screen
