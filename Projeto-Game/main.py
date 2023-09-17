import pygame, sys
from personagem.player_script import Player
from inimigos.canhão.canhao import Bala, Canhao
from assets.hud import Hud
from assets.coletaveis import Coletaveis
 
#definição dos dados básicos do jogo
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 432
WINDOW_HEIGHT = 768
bg = pygame.image.load("assets/bckd_placeholder.png")
game_name = 'Alice in Cocafeland'
icone_game = pygame.image.load('assets/icone.png') #necessário criar o ícone ainda
inicio = True

class Objeto:
    def __init__(self,x,y,largura,altura,caminho): 
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
       # self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.superficie = pygame.image.load(caminho)
        self.superficie = pygame.transform.scale(self.superficie, (largura,altura))
        self.superficie_rect = self.superficie.get_rect(topleft = (self.x,self.y))
class Floor(pygame.sprite.Sprite):
    def __init__(self,x,y,largura,altura,caminho_imagem):
        super().__init__()
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.caminho = caminho_imagem
        self.image = pygame.image.load(self.caminho)
        self.image = pygame.transform.scale(self.image,(largura,altura))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
class Portal(Objeto):
    def __init__(self, x, y, largura, altura, caminho):
        super().__init__(x, y, largura, altura, caminho)
        
    def desehar_portal(self):
        tela = pygame.display.get_surface()
        tela.blit(self.superficie,(self.x,self.y))
   

#Floor
floor_group = pygame.sprite.Group()
posicao_x = -50
for floor in range(9):
    posicao_x += 50
    new_floor = Floor(posicao_x,743,50,30,'niveis/Terrain1.png')
    floor_group.add(new_floor)

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,largura,altura,caminho_imagem) :
        super().__init__()
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.caminho = caminho_imagem
        self.image = pygame.image.load(self.caminho)
        self.image = pygame.transform.scale(self.image,(largura,altura))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
class Plataform(pygame.sprite.Sprite):  
    def __init__(self,x,y,largura,altura,caminho_imagem ):
        super().__init__()
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.caminho_imagem = caminho_imagem
        self.image = pygame.image.load(self.caminho_imagem)
        self.image = pygame.transform.scale(self.image,(largura,altura))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))

#plataforma1       
plataform_group1 = pygame.sprite.Group()
plataform_position = 17
for plataform in range(97):
    plataform_position += 4
    new_plataform = Plataform(plataform_position,660,5,5,'niveis/plataforma.png')
    new_plataform.add(plataform_group1)

#Plataforma 2
plataform_group2 = pygame.sprite.Group()
plataform_position2 = -10
for plataform in range(13):
    plataform_position2 += 30
    new_plataform = Plataform(plataform_position2,535,35,17,'niveis/Terrain2.png')
    new_plataform.add(plataform_group2)    

#Plataforma3
plataform_group3 = pygame.sprite.Group()
plataform_position3 = -10
for plataform in range(13):
    plataform_position3 += 30
    new_plataform = Plataform(plataform_position3,410,30,17,'niveis/Terrain5.png')
    new_plataform.add(plataform_group3)    

#Plataforma 4
plataform_group4 = pygame.sprite.Group()
plataform_position4 = -10
for plataform in range(13):
    plataform_position4 += 30
    new_plataform = Plataform(plataform_position4,290,35,17,'niveis/Terrain2.png')
    new_plataform.add(plataform_group4)
    
plataform_group5 = pygame.sprite.Group()
plataform_position5 = 17
for plataform in range(97):
    plataform_position5 += 4
    new_plataform = Plataform(plataform_position5,190,5,5,'niveis/plataforma.png')
    new_plataform.add(plataform_group5)

#Plataforma6
plataform_group6 = pygame.sprite.Group()
plataform_position6 = -10
for plataform in range(13):
    plataform_position6 += 30
    new_plataform = Plataform(plataform_position6,80,35,17,'niveis/Terrain2.png')
    new_plataform.add(plataform_group6)    
    
#Parede direita:
right_wall_group = pygame.sprite.Group()
posicao_parede_y = 724
for wall in range(12):
    posicao_parede_y -= 62
    new_right_wall = Wall(411,posicao_parede_y,20,80,'niveis/parede.png')
    right_wall_group.add(new_right_wall)
#Parede esquerda:
left_wall_group = pygame.sprite.Group()
esquerda_posicao_y = 724
for wall in range(12):
    esquerda_posicao_y -= 62
    new_left_wall = Wall(0,esquerda_posicao_y,20,80,'niveis/parede.png')
    left_wall_group.add(new_left_wall)


def main():

    #renderiza os eventos iniciais do jogo
    renderizar = True
    pygame.init() #inicializa as funções do pygame
    game_running = True #variável que faz o código principal permanecer rodando
    pygame.display.set_caption(game_name) #define o nome da janela do jogo 
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #define o tamanho da janela do jogo
    WINDOW.blit(bg,(0,0))
    pygame.display.set_icon(icone_game)

    #espaço para alocar os códigos
    jogador = Player()
    canon = Canhao()
    tiro = Bala(canon)
    hud_ = Hud()
    coletaveis_ = Coletaveis()
    portal = Portal(340,-5,100,90,'niveis/portal.png')
     #loop para funcionar o game
    while (game_running):

        #recebe os inputs para fechar o aplicativo
        events = pygame.event.get()
        for events in events:
            if(events.type == pygame.KEYDOWN):
                if(events.key == pygame.K_ESCAPE):
                    sys.exit()
        if(jogador.vida == 0):
            sys.exit()


        #movimento do jogador
        jogador.movimento()
        holder_info = jogador.shared_data_player() #variável que aloca as informações públicas do arquivo do jogador
        
        #área colocada para os inimigos
        jogador.vida = tiro.canhao_dano(holder_info[0], holder_info[1]) #determina a vida atual depois de tirarmos a o dano pelo canhão
        tiro.atirar()
        
        #hud
        hud_.hearts(jogador.vida)

        #coletaveis
        jogador.vida = coletaveis_.coletar_vida(jogador.vida, holder_info[1])
        
        #renderiza as imagens do jogo no loop
        if(renderizar):
            coletaveis_.desenhar_coletaveis()
            hud_.desenhar_hud()
            jogador.desenhar_player()
            tiro.desenhar_bala()
            canon.desenhar_canhao()
            portal.desehar_portal()
            floor_group.draw(WINDOW)
            right_wall_group.draw(WINDOW)
            left_wall_group.draw(WINDOW)
            plataform_group1.draw(WINDOW)
            plataform_group2.draw(WINDOW)
            plataform_group3.draw(WINDOW)
            plataform_group4.draw(WINDOW)
            plataform_group5.draw(WINDOW)
            plataform_group6.draw(WINDOW)
            pygame.display.update()
            WINDOW.blit(bg,(0,0))

        #dados para atualizar o jogo a cada loop
        fpsClock.tick(fps)

main()