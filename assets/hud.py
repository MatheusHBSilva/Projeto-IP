import pygame
from personagem.player_script import Player

#definições dos sprites e das posições do hud (vida e moedas)
class Hud:

    def __init__(self):
        #informações corações
        self.sprites_vida = ['assets/lifebar/lifebar_empty.png','assets/lifebar/lifebar_low.png', 'assets/lifebar/lifebar_medium.png', 'assets/lifebar/lifebar_full.png']
        self.x_heart = 0
        self.y_heart = 10
        self.sprite_vida_atual = self.sprites_vida[2]

        #informações moedas
        self.sprites_moeda = ['assets/coinbar/coin_bar_empty.png', 'assets/coinbar/coin_bar-1.png', 'assets/coinbar/coin_bar-2.png', 'assets/coinbar/coin_bar-3.png']
        self.x_moeda = 5
        self.y_moeda = 45

    #código que muda os sprites da barra de vida
    def hearts(self, vida):
        if(vida == 3):
            self.sprite_vida_atual = self.sprites_vida[3]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (90, 30))
        elif(vida == 2):
            self.sprite_vida_atual = self.sprites_vida[2]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (90, 30))
        elif(vida == 1):
            self.sprite_vida_atual = self.sprites_vida[1]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (90, 30))
        elif(vida <= 0):
            self.sprite_vida_atual = self.sprites_vida[0]
            self.sprite_vida_atual = pygame.image.load(self.sprite_vida_atual).convert_alpha()
            self.sprite_vida_atual = pygame.transform.scale(self.sprite_vida_atual, (90, 30))
    
    def dinheiro(self, moeda):
        if(moeda >= 3):
            self.sprite_moeda_atual = self.sprites_moeda[3]
            self.sprite_moeda_atual = pygame.image.load(self.sprite_moeda_atual).convert_alpha()
            self.sprite_moeda_atual = pygame.transform.scale(self.sprite_moeda_atual, (70, 25))
        elif(moeda == 2):
            self.sprite_moeda_atual = self.sprites_moeda[2]
            self.sprite_moeda_atual = pygame.image.load(self.sprite_moeda_atual).convert_alpha()
            self.sprite_moeda_atual = pygame.transform.scale(self.sprite_moeda_atual, (70, 25))
        elif(moeda == 1):
            self.sprite_moeda_atual = self.sprites_moeda[1]
            self.sprite_moeda_atual = pygame.image.load(self.sprite_moeda_atual).convert_alpha()
            self.sprite_moeda_atual = pygame.transform.scale(self.sprite_moeda_atual, (70, 25))
        elif(moeda == 0):
            self.sprite_moeda_atual = self.sprites_moeda[0]
            self.sprite_moeda_atual = pygame.image.load(self.sprite_moeda_atual).convert_alpha()
            self.sprite_moeda_atual = pygame.transform.scale(self.sprite_moeda_atual, (70, 25))

    
    #desenha o hud como um todo, corações e moedas
    def desenhar_hud(self):
        tela = pygame.display.get_surface()
        tela.blit(self.sprite_vida_atual, (self.x_heart, self.y_heart))
        tela.blit(self.sprite_moeda_atual, (self.x_moeda, self.y_moeda))
