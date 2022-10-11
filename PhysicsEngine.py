import pygame
from Object import Ball,Mesh

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

    all_sprite_list = pygame.sprite.Group()
    ## For Mesh creation
    ## create ball group -> nodes of Mesh
    ## create line group -> Edges of mesh
    ## loop through mesh matrix and add edges and nodes
    
    for i in range (10,300,100):
        ball  = Ball(White, i,20, 10,screen)
        all_sprite_list.add(ball)

#    mesh = Mesh(White,20,20,10,10,screen)

    clock = pygame.time.Clock()
    running = True
    acc = 9.81
    ##Window Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif pygame.mouse.get_pressed()[0]:
                mouse_pos= pygame.mouse.get_pos()
                new_ball = Ball(White,mouse_pos[0],mouse_pos[1],10,screen)
                all_sprite_list.add(new_ball)

        all_sprite_list.clear(screen,background)
        all_sprite_list.update(acc)
        all_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
pygame.quit()