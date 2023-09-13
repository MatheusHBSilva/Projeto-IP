import pygame
from personagem.player_script import Player

class Canhao:
    def __init__(self):
        self.sprite_canhao = pygame.image.load('inimigos/canhão/canhão_placeholder.png').convert_alpha()
        self.sprite_canhao = pygame.transform.scale(self.sprite_canhao, (80, 90))

        self.x = -20
        self.y = 700

        # Collider do canhao
        self.collider_canon = pygame.Rect(self.x, self.y, 40, 55)

    def desenhar_canhao(self):
        tela = pygame.display.get_surface()
        tela.blit(self.sprite_canhao, (self.x, self.y))

class Bala:

    def __init__(self, canon):
        self.canon = canon
        self.hitting = False

        self.sprite_bala = pygame.image.load('inimigos/canhão/tiro_placeholder.png').convert_alpha()
        self.sprite_bala = pygame.transform.scale(self.sprite_bala, (20, 30))

        self.y_bala = self.canon.y + 30
        self.x_bala = self.canon.x + 40
        self.x_bala_original = self.x_bala
        self.velocidade_bala = 2
        self.atirando = False

        self.collider_bala = pygame.Rect(self.x_bala, self.y_bala, 15, 20)

    def atirar(self):
        if(not self.atirando):
            self.atirando = True

        if(self.atirando):
            self.x_bala += self.velocidade_bala
            if(self.x_bala >= 395): #colocar a box collider do player
                self.atirando = False
                self.x_bala = self.x_bala_original

    def desenhar_bala(self):
        if(self.atirando):
            tela = pygame.display.get_surface()
            tela.blit(self.sprite_bala, (self.x_bala, self.y_bala))

    def canhao_dano(self, vida, colisor):

        self.collider_bala = pygame.Rect(self.x_bala, self.y_bala, 20, 30)
        if(self.collider_bala.colliderect(colisor) and not self.hitting and vida > 0):
            vida -= 1
            self.hitting = True
            #self.x_bala = self.canon.x + 40
        
        elif(not self.collider_bala.colliderect(colisor)):
            self.hitting = False

        return vida

    
    

            
