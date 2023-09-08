import pygame, sys
from Personagem.personagem import player   

#definição dos dados básicos do jogo
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 432
WINDOW_HEIGHT = 768
bg_color = (255,0,0)
game_name = 'Alice in Cocafeland'
icone_game = '' #necessário criar o ícone ainda

def main():

    #renderiza os eventos iniciais do jogo
    pygame.init() #inicializa as funções do pygame
    game_running = True #variável que faz o código principal permanecer rodando
    pygame.display.set_caption(game_name) #define o nome da janela do jogo 
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #define o tamanho da janela do jogo
    WINDOW.fill(bg_color)
    jogador = player()

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
        jogador.desenhar_player()
        

        #dados para atualizar o jogo a cada loop
        pygame.display.update()
        fpsClock.tick(fps)

main()