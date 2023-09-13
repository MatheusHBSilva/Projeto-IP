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

def main():

    tempo_inicial = pygame.time.get_ticks()

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


        #jogador
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
            jogador.animacoes(tempo_inicial)
            tempo_inicial = jogador.set_timer(tempo_inicial)
            tiro.desenhar_bala()
            canon.desenhar_canhao()
            pygame.display.update()
            WINDOW.blit(bg,(0,0))

        #dados para atualizar o jogo a cada loop
        fpsClock.tick(fps)

main()