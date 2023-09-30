import pygame
import random

class Canhao:
    def __init__(self):
        self.x = -20
        self.y = []
        self.x_balas = []
        self.y_possiveis = [575, 475,375,275,175,75]
        self.qtd_canhao = 4
        self.velocidades = []
        self.lane = -1

        self.sprite_bala = pygame.image.load('inimigos/canhão/tiro_placeholder.png').convert_alpha()
        self.sprite_bala = pygame.transform.scale(self.sprite_bala, (15, 25))
        self.sprite_canhao = pygame.image.load('inimigos/canhão/canhão.png').convert_alpha()
        self.sprite_canhao = pygame.transform.scale(self.sprite_canhao, (80, 90))
        self.y_bala = 0
        self.x_bala = -25
        self.atirando = True

        self.collider_bala = pygame.Rect(self.x_bala, self.y_bala, 3, 10)

        self.lst_colliders = []
        self.hitting_lst = []

    def gerar_posicao(self):
          for i in range(self.qtd_canhao):
            index = random.randint(0,len(self.y_possiveis) - 1)
            self.x_balas.append(7)
            self.hitting_lst.append(False)
            self.lst_colliders.append(self.collider_bala)
            self.y.append(self.y_possiveis[index])
            self.y_possiveis.remove(self.y_possiveis[index])
            velo = random.randint(2,8)
            self.velocidades.append(velo)

    def atirar(self, val):
        if(self.atirando):
            self.x_balas[val] += self.velocidades[val]
            if(self.x_balas[val] >= 415):
                self.x_balas[val] = 7
    
        
    def desenhar(self, val):
        tela = pygame.display.get_surface()
        tela.blit(self.sprite_bala, (self.x_balas[val], self.y[val] + 33))
        tela.blit(self.sprite_canhao, (self.x, self.y[val]))
        
        
    def canhao_dano(self, vida, colisor, val):
        self.lst_colliders[val] = pygame.Rect(self.x_balas[val] + 7.5, self.y[val] + 30, 10, 10)
        if(self.lst_colliders[val].colliderect(colisor) and self.hitting_lst[val] == False):
            vida -= 1
            self.hitting_lst[val] = True
        elif(not self.lst_colliders[val].colliderect(colisor)):
            self.hitting_lst[val] = False

        return vida

    def resetar(self):
        self.x = -20
        self.lst_colliders = []
        self.hitting_lst = []
        self.y = []
        self.x_balas = []
        self.y_possiveis = [575, 475,375,275,175,75]
            
