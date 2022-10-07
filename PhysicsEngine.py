import pygame
from Object import Ball

pygame.init()

def main():
    White = (255,255,255)
    Black = (0,0,0)
    (width,height) = (700,500)
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Physics Engine")
    background = pygame.Surface(screen.get_size())
    background.fill(Black)
    screen.blit(background,(0,0))


    ball = Ball(White,20,20,10,screen)
    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(ball)
    clock = pygame.time.Clock()
    running = True
    ##Window Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprite_list.clear(screen,background)
        all_sprite_list.update()
        all_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
pygame.quit()