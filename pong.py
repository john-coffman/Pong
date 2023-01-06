import sys, pygame 

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    player = pygame.Rect(0, 0, 100, 100)
    
    screen.fill("purple")
    pygame.draw.rect(screen, (60, 179, 113), player, 50)
    pygame.display.flip()
    clock.tick(60)

