import pygame

BLACK = (0,0,0)
RED = (255, 0, 0)
class Score():
    def __init__(self):
        self.score = {"player": 0, "enemy": 0}
        self.text = pygame.font.SysFont(None, 48).render(self.get_score(),True, RED, BLACK )
        self.textrect = self.text.get_rect()
        
    def update_score(self, player_scored=False, enemy_scored=False):
        if player_scored:
            self.score["player"] += 1
        if enemy_scored:
            self.score["enemy"] += 1
        self.text = pygame.font.SysFont(None, 48).render(self.get_score(),True, RED, BLACK)
            
    def get_score(self):
        return str(self.score["enemy"]) + "          " + str(self.score["player"])