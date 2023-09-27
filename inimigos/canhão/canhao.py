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

        self.hitting = False
        self.sprite_bala = pygame.image.load('inimigos/canhão/tiro_placeholder.png').convert_alpha()
        self.sprite_bala = pygame.transform.scale(self.sprite_bala, (15, 25))
        self.sprite_canhao = pygame.image.load('inimigos/canhão/canhão.png').convert_alpha()
        self.sprite_canhao = pygame.transform.scale(self.sprite_canhao, (80, 90))
        self.y_bala = 0
        self.x_bala = -25
        self.atirando = True

        self.collider_bala = pygame.Rect(self.x_bala, self.y_bala, 3, 10)

    def gerar_posicao(self):
          for i in range(self.qtd_canhao):
            #vai gerar a posicao x do coracao no mapa
            index = random.randint(0,len(self.y_possiveis) - 1)
            self.x_balas.append(7)
            self.y.append(self.y_possiveis[index])
            self.y_possiveis.remove(self.y_possiveis[index])
            velo = random.randint(5,8)
            self.velocidades.append(velo)

    def atirar(self, val, collider):
        collider_bala = pygame.Rect(self.x_balas[val] + 7.5, self.y[val] + 30, 10, 10)
        if(self.atirando):
            self.x_balas[val] += self.velocidades[val]
            if(self.x_balas[val] >= 395):
                self.x_balas[val] = 7
            elif(collider_bala.colliderect(collider)):
                self.x_balas[val] += 20
    
        
    def desenhar(self, val):
        tela = pygame.display.get_surface()
        tela.blit(self.sprite_bala, (self.x_balas[val], self.y[val] + 33))
        tela.blit(self.sprite_canhao, (self.x, self.y[val]))
        
        
    def canhao_dano(self, vida, colisor, val):
        collider_bala = pygame.Rect(self.x_balas[val] + 7.5, self.y[val] + 30, 10, 10)
        if(collider_bala.colliderect(colisor) and not self.hitting):
            vida -= 1
        return vida

    def resetar(self):
        self.x = -20
        self.y = []
        self.x_balas = []
        self.y_possiveis = [575, 475,375,275,175,75]
            
