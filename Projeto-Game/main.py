import pygame, sys
from Personagem.player_script import player
from inimigos.canhão.canhao import bala, canhao

#definição dos dados básicos do jogo
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 432
WINDOW_HEIGHT = 768
bg = pygame.image.load("assets/bckd_placeholder.png")
game_name = 'Alice in Cocafeland'
icone_game = pygame.image.load('assets/icone.png') #necessário criar o ícone ainda

def main():

    #renderiza os eventos iniciais do jogo
    renderizar = True
    pygame.init() #inicializa as funções do pygame
    game_running = True #variável que faz o código principal permanecer rodando
    pygame.display.set_caption(game_name) #define o nome da janela do jogo 
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #define o tamanho da janela do jogo
    WINDOW.blit(bg,(0,0))
    pygame.display.set_icon(icone_game)
    jogador = player()
    canon = canhao()
    tiro = bala(canon)

    #loop para funcionar o game
    while (game_running):

        #recebe os inputs do teclado para fechar o aplicativo
        events = pygame.event.get()
        for events in events:
            if(events.type == pygame.KEYDOWN):

                if(events.key == pygame.K_ESCAPE):

                    sys.exit()

        #movimento do jogador
        jogador.movimento()
        
        #área colocada para os inimigos
        tiro.atirar()
        tiro.canhao_dano()
        
        #renderiza as imagens do jogo no loop
        if(renderizar):
            jogador.desenhar_player()
            tiro.desenhar_bala()
            canon.desenhar_canhao()
            pygame.display.update()
            WINDOW.blit(bg,(0,0))

        #dados para atualizar o jogo a cada loop
        fpsClock.tick(fps)

main()