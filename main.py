import pygame, sys
from personagem.player_script import Player
from inimigos.canhão.canhao import Canhao
from assets.hud import Hud
from assets.hearts import Hearts
from assets.moedas import Moedas
from assets.terrain import Terrain
from controladora import Controladora
from menu import Mainmenu

#definição dos dados básicos do jogo
musica = pygame.mixer_music.load('assets/musica/game_ost.mp3')
pygame.mixer_music.set_volume(0.1)

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
    next_level = True
    randomize = False
    renderizar = True 
    pygame.init() #inicializa as funções do pygame
    game_running = True #variável que faz o código principal permanecer rodando
    pygame.display.set_caption(game_name) #define o nome da janela do jogo 
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #define o tamanho da janela do jogo
    WINDOW.blit(bg,(0,0))
    pygame.display.set_icon(icone_game)

    pygame.mixer_music.play()

    #espaço para alocar os códigos
    jogador = Player()
    tiro = Canhao()
    hud_ = Hud()
    terrain_ = Terrain()
    controladora_ = Controladora()
    coracoes = Hearts()
    moedas_ = Moedas()
    mm = Mainmenu()
    #loop para funcionar o game
    while (game_running):
        #recebe os inputs para fechar o aplicativo
        events = pygame.event.get()
        for events in events:
            if events.type == pygame.QUIT:
                game_running = False
            if(events.type == pygame.KEYDOWN):
                if(events.key == pygame.K_ESCAPE):
                    sys.exit()
                if(events.key == pygame.K_r):
                    randomize = True

        #chama o próximo nível
        if(next_level):
            coracoes.resetar()
            coracoes.posicoes_coracoes()
            moedas_.resetar()
            moedas_.posicoes()
            tiro.resetar()
            tiro.gerar_posicao()
            tiro.atirando = True 
            tiro.x_bala = -25
            jogador.y = 735
            jogador.x = 200
            jogador.posicao_trigger_lista = 0
            jogador.posicao_plataforma_lista = 0
            jogador.y_plataforma = jogador.posicoes_plataformas[jogador.posicao_plataforma_lista]
            jogador.dinheiro = 0
            next_level = False
            randomize = False
        
        #caso o jogador morra, ele pode apertar a tecla R e reiniciar o game
        if(randomize):
            mm.render_menu = True
            moedas_.capital_acumulado = 0
            coracoes.resetar()
            coracoes.posicoes_coracoes()
            moedas_.resetar()
            moedas_.posicoes()
            tiro.resetar()
            tiro.gerar_posicao()
            jogador.inverter_direita = True
            jogador.inverter_esquerda = True
            jogador.vida = 3
            jogador.invertido = 0
            controladora_.lvl = 1
            controladora_.pontuação = 0
            tiro.x_bala = -25
            jogador.y = 735
            jogador.x = 200
            jogador.posicao_trigger_lista = 0
            jogador.posicao_plataforma_lista = 0
            jogador.y_plataforma = jogador.posicoes_plataformas[jogador.posicao_plataforma_lista]
            jogador.dinheiro = 0
            next_level = False
            randomize = False
            jogador.stop_animation = False
            jogador.velocidade = 4
            jogador.forca_pulo = 10
            tiro.atirando = True
        
        #controla caso a vida do jogador chegue a zero ou chegue no lvl 6 (vulgo acabar o game)
        if(jogador.vida < 0 or controladora_.lvl == 6):
            controladora_.lvl = 6
            jogador.velocidade = 0
            jogador.forca_pulo = 0
            jogador.stop_animation = True
            tiro.atirando = False
        
        #caso não esteja no menu principal, começa a renderizar o resto do jogo
        if(not mm.render_menu):
            #jogador
            jogador.movimento()
            jogador.atualizar_terreno()
            holder_info = jogador.shared_data_player() #variável que aloca as informações públicas do arquivo do jogador

            #hud
            hud_.hearts(jogador.vida)
            hud_.dinheiro(jogador.dinheiro)

            next_level = controladora_.next_lvl_load(next_level)

            #renderiza as imagens do jogo no loop
            if(renderizar):
                controladora_.desenhar_coca(holder_info[1], jogador.dinheiro)
                terrain_.desenhar_plataformas()
                hud_.desenhar_hud()
                jogador.animacoes(tempo_inicial)
                tempo_inicial = jogador.set_timer(tempo_inicial)
                
                #spawns dos coletáveis e dos inimigos
                for i in range(coracoes.num_of_hearts):#vida
                    coracoes.desenhar(i)
                    jogador.vida = coracoes.hitbox(holder_info[1], jogador.vida, i)
                for i in range(moedas_.num_of_coins):#moedas
                    moedas_.desenhar(i)
                    jogador.dinheiro = moedas_.hitbox(holder_info[1], jogador.dinheiro, i)
                for i in range(tiro.qtd_canhao):#canhao
                    jogador.vida = tiro.canhao_dano(jogador.vida, holder_info[1], i)
                    tiro.atirar(i, holder_info[1])
                    tiro.desenhar(i)

                controladora_.show_text()
                moedas_.show_text()

        else:
            mm.desenhar()
            mm.logicamenu()

        #dados para atualizar o jogo a cada loop
        pygame.display.update()
        WINDOW.blit(bg,(0,0))
        fpsClock.tick(fps)

main()