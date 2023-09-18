import pygame
from personagem.player_script import Player

#definições dos sprites e das posições do hud (vida e moedas)
class Hud:

    def __init__(self):
        self.sprites_vida = ['assets/lifebar/lifebar_placeholder_low.png', 'assets/lifebar/lifebar_placeholder_medium.png', 'assets/lifebar/lifebar_placeholder_high.png']
        self.x_heart = 0
        self.y_heart = 0
        self.sprite_vida_atual = self.sprites_vida[2]
    
    #código que muda os sprites da barra de vida
    def hearts(self, vida):
        if(vida == 3):
            self.sprite_vida_atual = self.sprites_vida[2]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
        elif(vida == 2):
            self.sprite_vida_atual = self.sprites_vida[1]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
        elif(vida == 1):
            self.sprite_vida_atual = self.sprites_vida[0]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
    
    #desenha o hud como um todo, corações e moedas
    def desenhar_hud(self):
        tela = pygame.display.get_surface()
        tela.blit(self.sprite_vida_atual, (self.x_heart, self.y_heart))

    
    def coin_bar(self):
        self.sprite_coin = ['assets/CoinBar/coinBar#1.png','assets/CoinBar/coinBar#2.png','assets/CoinBar/coinBar#3.png','assets/CoinBar/coinBar#4.png']
        self.x_coin = 30
        self.y_heart = 0
        self.sprite_coin_atual = self.sprite_coin[0]
    
    def coin_change(self,moeda):
        if(moeda == 0):
            self.sprite_coin_atual = self.sprite_coin[0]
            self.sprite_coin_atual = pygame.image.load(self.sprite_coin_atual).convert_alpha()
            self.sprite_coin_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
        elif(moeda == 1):
            self.sprite_coin_atual = self.sprite_coin[1]
            self.sprite_coin_atual = pygame.image.load(self.sprite_coin_atual).convert_alpha()
            self.sprite_coin_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
        elif(moeda == 2):
            self.sprite_coin_atual = self.sprite_coin_atual[2]
            self.sprite_coin_atual = pygame.image.load(self.sprite_coin_atual).convert_alpha()
            self.sprite_coin_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
        elif(moeda == 3):
            self.sprite_coin_atual = self.sprite_coin_atual[3]
            self.sprite_coin_atual = pygame.image.load(self.sprite_coin_atual).convert_alpha()
            self.sprite_coin_atual = pygame.transform.scale(self.sprite_vida_atual, (100, 50))
