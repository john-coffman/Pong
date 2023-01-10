import pygame 

from Ball import Ball
from Paddles import Paddles
from Score import Score

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

WIDTH = 1280
HEIGT = 720
screen = pygame.display.set_mode((WIDTH,HEIGT))

enemy = Paddles(WHITE, 20, 100)
enemy.rect.x = WIDTH-1200
enemy.rect.y = HEIGT/2-50

player = Paddles(WHITE, 20, 100)
player.rect.x = WIDTH-80
player.rect.y = HEIGT/2-50

ball = Ball(WHITE, 15, 15)
ball.rect.x = WIDTH/2
ball.rect.y = HEIGT/2

score = Score()
score.textrect.centerx = screen.get_rect().centerx 
score.textrect.centery = screen.get_rect().top + 100

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(player)
all_sprites_list.add(enemy)

pads = [player.rect, enemy.rect]
clock = pygame.time.Clock()

def run():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.rect.y > 0:
            player.moveUp(5)
        if keys[pygame.K_DOWN] and player.rect.y < HEIGT-100:
            player.moveDown(5)
            
        if enemy.rect.y >= ball.rect.y and enemy.rect.y > 0:
            enemy.moveUp(5)
        if enemy.rect.y <= ball.rect.y and enemy.rect.y < HEIGT-100:
            enemy.moveDown(5)
            
        if ball.rect.x >= WIDTH-15:
            ball.reset()
            score.update_score(enemy_scored = True)
        if ball.rect.x <= 0:
            ball.reset()
            score.update_score(player_scored = True)
            
        if ball.rect.y > HEIGT-15:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]
        
        if ball.rect.collidelist(pads) >= 0:
            ball.bounce()
        
        all_sprites_list.update()
        screen.fill(BLACK)
        all_sprites_list.draw(screen)
        clock.tick(60)
        screen.blit(score.text, score.textrect)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    run() 