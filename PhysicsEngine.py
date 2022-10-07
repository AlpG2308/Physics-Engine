import pygame
from Object import Ball
pygame.init()
White = (255,255,255)
Black = (0,0,0)
(width,height) = (700,500)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Physics Engine")
screen.fill(Black)

ball = Ball(White,10,100)
ball.rect.x = 345
ball.rect.y = 195

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(ball)
clock = pygame.time.Clock()
running = True
##Window Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprite_list.update()
    pygame.draw.line(screen, White, [349, 0], [349, 500], 5)
    screen.fill(Black)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()





if __name__ == "__main__":
    main()