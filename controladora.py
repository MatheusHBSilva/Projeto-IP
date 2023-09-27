import pygame
pygame.init()
import random

class Controladora:

    def __init__(self):
        self.coca = pygame.image.load('assets/icone.png').convert_alpha()
        self.coca = pygame.transform.scale(self.coca, (30,30))
        self.hitbox_coca = pygame.Rect(200, 30, 30, 30)
        self.touching_coca = False
        self.lvl = 1
        self.pontuação = 0
        self.x = 370
        self.y = 0
        self.dialogue_font = pygame.font.SysFont('arial', 20)
        self.text_normal = self.dialogue_font.render(f'Nível {self.lvl}', False, (0, 255, 0), (0, 0, 128))
        self.texto_final = self.dialogue_font.render(f'Obrigado por jogar Alice in Cocafeland', True, (0, 255, 0), (0, 0, 128))
        self.texto_final_2 = self.dialogue_font.render(f'esperamos que você tenha gostado', True, (0, 255, 0), (0, 0, 128))
        self.texto_final_3 = self.dialogue_font.render(f'perssione "ESC" para sair', True, (0, 255, 0), (0, 0, 128))
        self.texto_final_4 = self.dialogue_font.render(f'ou pressione R para tentar de novo', True, (0, 255, 0), (0, 0, 128))


    def show_text(self):
        self.text_normal = self.dialogue_font.render(f'Nível {self.lvl}', False, (0, 255, 0), (0, 0, 128))
        texto_pontuacao = self.dialogue_font.render(f'Sua pontuação: {self.pontuação}', True, (0, 255, 0), (0, 0, 128))
        if(self.lvl == 1):
            self.y = 0
            self.pontuação = 0
            tela = pygame.display.get_surface()
            if(self.lvl < 6):
                tela.blit(self.text_normal, (self.x, self.y))
            else:
                tela.blit(self.text_normal, (self.x-30, self.y))
            if(self.pontuação == 0):
                tela.blit(texto_pontuacao, (self.x - 95 , self.y + 20))
            elif(self.pontuação < 100):
                tela.blit(texto_pontuacao, (self.x - 100 , self.y + 20))
            elif(self.pontuação < 1000):
                tela.blit(texto_pontuacao, (self.x - 118 , self.y + 20))
            else:
                tela.blit(texto_pontuacao, (self.x - 128 , self.y + 20))

        elif(self.lvl < 6):
            self.y = 0
            self.text_normal = self.dialogue_font.render(f'Nível {self.lvl}', False, (0, 255, 0), (0, 0, 128))
            tela = pygame.display.get_surface()
            if(self.lvl < 10):
                tela.blit(self.text_normal, (self.x, self.y))
            else:
                tela.blit(self.text_normal, (self.x-20, self.y))
            if(self.pontuação == 0):
                tela.blit(texto_pontuacao, (self.x - 95 , self.y + 20))
            elif(self.pontuação < 100):
                tela.blit(texto_pontuacao, (self.x - 100 , self.y + 20))
            elif(self.pontuação < 1000):
                tela.blit(texto_pontuacao, (self.x - 118 , self.y + 20))
            else:
                tela.blit(texto_pontuacao, (self.x - 128 , self.y + 20))

        else:
            self.y = 200
            tela = pygame.display.get_surface()
            tela.blit(self.texto_final, (self.x - 325, self.y + 90))
            tela.blit(self.texto_final_2, (self.x - 315, self.y + 120))
            tela.blit(self.texto_final_3, (self.x - 270, self.y + 150))
            tela.blit(self.texto_final_4, (self.x - 310, self.y + 180))
            if(self.pontuação < 100):
                tela.blit(texto_pontuacao, (self.x - 230, self.y + 210))
            elif(self.pontuação < 1000):
                tela.blit(texto_pontuacao, (self.x - 250 , self.y + 210))
            else:
                tela.blit(texto_pontuacao, (self.x - 245 , self.y + 210))
            
    def desenhar_coca(self, colisor, moedas):
        tela = pygame.display.get_surface()
        tela.blit(self.coca, (200, 30))
        if(self.hitbox_coca.colliderect(colisor) and not self.touching_coca):
            self.touching_coca = True
            self.lvl += 1
            val = random.randint(23,300)
            self.pontuação += moedas * val
        elif(not self.hitbox_coca.colliderect(colisor)):
            self.touching_coca = False
    
    def next_lvl_load(self, variavel):
        if(self.touching_coca == True):
            variavel = True
            return variavel
    
    def teste(variavel):
        variavel = True
        return variavel
    




