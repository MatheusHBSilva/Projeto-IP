import pygame

class Terrain:

    def __init__(self):
        #chama a imagem do terreno
        self.ground_1 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_2 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_3 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_4 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_5 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_6 = pygame.image.load('assets/ground/ground_placeholder.png')
        self.ground_7 = pygame.image.load('assets/ground/ground_placeholder.png')

        #escalona a imagem do terreno
        self.ground_1 = pygame.transform.scale(self.ground_1, (1000, 20))
        self.ground_2 = pygame.transform.scale(self.ground_2, (1000, 20))
        self.ground_3 = pygame.transform.scale(self.ground_3, (1000, 20))
        self.ground_4 = pygame.transform.scale(self.ground_4, (1000, 20))
        self.ground_5 = pygame.transform.scale(self.ground_5, (1000, 20))
        self.ground_6 = pygame.transform.scale(self.ground_6, (1000, 20))
        self.ground_7 = pygame.transform.scale(self.ground_7, (1000, 30))

        #posições de cada plataforma
        self.x = 0 #posição do x geral para todos
        self.y_1 = 635
        self.y_2 = 535
        self.y_3 = 435
        self.y_4 = 335
        self.y_5 = 235
        self.y_6 = 135
        self.y_7 = 758

    def desenhar_plataformas(self):
        tela = pygame.display.get_surface()
        tela.blit(self.ground_1, (self.x, self.y_1))
        tela.blit(self.ground_2, (self.x, self.y_2)) 
        tela.blit(self.ground_3, (self.x, self.y_3)) 
        tela.blit(self.ground_4, (self.x, self.y_4)) 
        tela.blit(self.ground_5, (self.x, self.y_5)) 
        tela.blit(self.ground_6, (self.x, self.y_6))  
        tela.blit(self.ground_7, (self.x, self.y_7))  