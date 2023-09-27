import pygame
import random

class Hearts:

    def __init__(self):
        #informações do coração
        self.heart = pygame.image.load('assets/lifebar/coracao.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (15, 15))
        self.collected_heart = False
        self.collecting_heart = False

        #listas para spawnar o coração individualmente
        self.num_of_hearts = 5
        self.corações = []
        self.xs = []
        self.ys = []
        self.colliders = []
        self.ys_disponíveis = [590, 490, 390, 290, 190, 100]
    
    def posicoes_coracoes(self):
        for i in range(self.num_of_hearts):
            #vai gerar a posicao x do coracao no mapa
            index = random.randint(0,len(self.ys_disponíveis) - 1)
            pos_x = random.randint(225, 400)
            self.corações.append(self.heart)
            self.xs.append(pos_x)
            self.ys.append(self.ys_disponíveis[index])
            self.ys_disponíveis.remove(self.ys_disponíveis[index])
    

    def hitbox(self, player_collider, vida, val):  
        collisor = pygame.Rect(self.xs[val], self.ys[val], 15, 15)
        if(collisor.colliderect(player_collider) and vida < 3):
            vida += 1
            self.xs[val] = 10000
            self.ys[val] = 10000
            return vida
        else:
            return vida
    
    def desenhar(self, val):
        tela = pygame.display.get_surface()
        tela.blit(self.corações[val], (self.xs[val], self.ys[val]))
        
    def resetar(self):
        self.corações = []
        self.xs = []
        self.ys = []
        self.colliders = []
        self.ys_disponíveis = [590, 490, 390, 290, 190, 100]
    
            
