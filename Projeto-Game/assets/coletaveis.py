import pygame

class Coletaveis:

    def __init__(self):
        self.heart = pygame.image.load('assets/icone.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (30, 35))
        self.x = 200
        self.y = 600
        self.colisor_heart = pygame.Rect(self.x, self.y, 30, 35)
        self.collected_heart = False
        self.collecting_heart = False

    def coletar_vida(self, vida, colisor):
        if(self.colisor_heart.colliderect(colisor)):
            
            if(vida <3 and not self.collecting_heart):
                vida += 1
                self.collected_heart = True
                self.collecting_heart = True
        
        return vida

    def desenhar_coletaveis(self):
        if(not self.collected_heart):
            tela = pygame.display.get_surface()
            tela.blit(self.heart, (self.x, self.y))
        else:
            tela = pygame.display.get_surface()
            tela.blit(self.heart, (1000, 1000))


    def moeda(self):
        self.coin = pygame.image.load('assets/icone.png').convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (30, 35))
        self.x = 200
        self.y = 600
        self.colisor_coin = pygame.Rect(self.x, self.y, 30, 35)
        self.collected_coin = False
        self.collecting_coin = False
