import pygame
import random

class Moedas:

    def __init__(self):
        #informações do coração
        self.moeda = pygame.image.load('assets/coinbar/moeda.png').convert_alpha()
        self.moeda = pygame.transform.scale(self.moeda, (15, 15))
        self.capital_acumulado = 0

        #listas para spawnar o coração individualmente
        self.num_of_coins = 5
        self.moedas = []
        self.xs = []
        self.ys = []
        self.colliders = []
        self.ys_disponíveis = [590, 490, 390, 290, 190, 100]
    
    def posicoes(self):
        for i in range(self.num_of_coins):
            #vai gerar a posicao x do coracao no mapa
            index = random.randint(0,len(self.ys_disponíveis) - 1)
            pos_x = random.randint(75, 200)
            self.moedas.append(self.moeda)
            self.xs.append(pos_x)
            self.ys.append(self.ys_disponíveis[index])
            self.ys_disponíveis.remove(self.ys_disponíveis[index])

    def hitbox(self, player_collider, moeda, val):  
        collisor = pygame.Rect(self.xs[val], self.ys[val], 15, 15)
        if(collisor.colliderect(player_collider)):
            moeda += 1
            self.capital_acumulado += 1
            self.xs[val] = 10000
            self.ys[val] = 10000
            return moeda
        else:
            return moeda
    
    def desenhar(self, val):
        tela = pygame.display.get_surface()
        tela.blit(self.moedas[val], (self.xs[val], self.ys[val]))
        
    def resetar(self):
        self.moedas = []
        self.xs = []
        self.ys = []
        self.colliders = []
        self.ys_disponíveis = [590, 490, 390, 290, 190, 100]
    
    def show_text(self):
        dialogue_font = pygame.font.SysFont('arial', 20)
        text_normal = dialogue_font.render(f'Moedas: {self.capital_acumulado}', False, (0, 255, 0), (0, 0, 128))
        tela = pygame.display.get_surface()
        tela.blit(text_normal,(5,75))
    
            
