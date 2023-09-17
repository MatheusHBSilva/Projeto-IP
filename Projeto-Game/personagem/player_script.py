import pygame

class Player:
    def __init__(self):
        self.vida = 3
        self.x = 100 #x inicial da personagem
        self.y = 735 #y inicial da personaem 735
        self.y_plataforma = self.y #esse y será utilizado para modidicar o y que ela vai descer em relação a plataforma
        self.velocidade = 4
        self.forca_pulo = 12
        self.double_jump_available = False #verifica se é possível dar o double jump nesse momento
        self.double_jump_reset = True #reseta a possibilidade de dar o double jump (essa variável é confusa, ela é mais uma bugfixer)
        self.is_jumping = False #verifica se a personagem esta no ar 
        self.gravidade = 1 #força de gravidade do projeto
        self.sliding = False
        self.jump_height = 0
        self.fall = False
        self.inverter_esquerda = True
        self.inverter_direita = True
        self.invertido = False

        #chamar sprites da animação
        self.run = ['assets/animações/player_run/run-1.png','assets/animações/player_run/run-2.png','assets/animações/player_run/run-3.png','assets/animações/player_run/run-4.png','assets/animações/player_run/run-5.png','assets/animações/player_run/run-6.png','assets/animações/player_run/run-7.png','assets/animações/player_run/run-8.png']
        self.jump = ['assets/animações/player_jump/jump-1.png', 'assets/animações/player_jump/jump-2.png', 'assets/animações/player_jump/jump-3.png', 'assets/animações/player_jump/jump-4.png']
        self.falling = ['assets/animações/player_fall/fall-1.png', 'assets/animações/player_fall/fall-2.png', 'assets/animações/player_fall/fall-3.png', 'assets/animações/player_fall/fall-4.png']
        self.run_invertida = []
        self.jump_invertida = []
        self.falling_invertida = []

        #criando as animações invertidas
        for val in range(len(self.run)):
            imagem_invetida = pygame.image.load(self.run[val]).convert_alpha()
            imagem_invetida = pygame.transform.flip(imagem_invetida, True, False)
            self.run_invertida.append(imagem_invetida)
        for val in range(len(self.jump)):
            imagem_invetida = pygame.image.load(self.jump[val]).convert_alpha()
            imagem_invetida = pygame.transform.flip(imagem_invetida, True, False)
            self.jump_invertida.append(imagem_invetida)
        for val in range(len(self.falling)):
            imagem_invetida = pygame.image.load(self.falling[val]).convert_alpha()
            imagem_invetida = pygame.transform.flip(imagem_invetida, True, False)
            self.falling_invertida.append(imagem_invetida)
        
        self.animation_cooldown = 100
        self.frame = 0
        #box collider do jogador
        self.player_collider = pygame.Rect(self.x, self.y, 25, 30)

    def movimento(self):
        #siatema de pulo
        keys = pygame.key.get_pressed() #verifica se a tecla 'space' foi pressionada
        pronto = False
        if(keys[pygame.K_SPACE] or keys[pygame.K_UP] ):
            pronto = True

        if(pronto and not self.is_jumping): #pulo normal inicial, liberando o código de aumentar a altura
            self.is_jumping = True 
            self.jump_height = 0

        if(pronto and self.double_jump_available and self.fall and self.double_jump_reset): #verifica o double jump // o double jump só é liberado caso a altura máxima aconteça ou caso o personagem está dando sliding, mas é possível mudar essa variável tranquilamente
            self.double_jump_available = False
            self.double_jump_reset = False
            self.fall = False
            self.jump_height = 0
            self.is_jumping = True

            if(self.sliding == True):
                self.velocidade *= -1
                self.sliding = False
       
        if(self.is_jumping and not self.fall): #aumenta a altura do personagem no eixo Y
            self.y -= self.forca_pulo - self.jump_height
            self.jump_height += 1
            if(self.jump_height >= self.forca_pulo): #quando o personagem chega na altura máxima do pulo, ele começa a descer e autoriza o double jump
                self.fall = True
                self.double_jump_available = True
                self.jump_height = 0

        if(self.fall): #o código de gravidade, bastante semelhante ao código de subida   
            if(self.x <= 0 or self.x >= 405): #caso o personagem esteja nas paredes (beirada do mapa), ele entrará em slide pelo código abaixo e sua velocidade de descida será menor
                self.sliding = True
                self.jump_height = 0
                self.jump_height += 1.9
                self.y += 0.5 + self.jump_height
                self.double_jump_available = True
                self.double_jump_reset = True
            else:
                self.y += self.gravidade + self.jump_height
                self.jump_height += 1
                
            if(self.y >= self.y_plataforma): #quando o personagem retorna ao chão que partiu
                self.fall = False
                self.is_jumping = False
                self.double_jump_available = True
                self.y = self.y_plataforma
                self.double_jump_reset = True

        #código de controle automático da movimentação no x + slide wall
        #OBS: o slide está funcionando da seguinte forma, eu limitei a distância máxima que a personagem pode andar para 0-395, quando ela chega nessas coordenadas, inverte sua velocidade
        #porém, a velocidade só será invertida se o personagem não estiver caindo, caso ele esteja, apenas muda o eixo da imagem
        if(self.velocidade > 0): #caso a velocidade seja positiva, ou seja, indo para direita
            if(self.x != 432):
                if(self.x < 405):
                    self.x += self.velocidade
            if(self.x >= 405 and self.y == self.y_plataforma):
                self.velocidade *= -1
                self.sliding = False
            

        if(self.velocidade < 0): #velocidade negativa (indo para a esquerda)
            if(self.x > 0):
                self.x += self.velocidade
            if(self.x <= 0 and self.y == self.y_plataforma): 
                self.velocidade *= -1
                self.sliding = False
            
    def shared_data_player(self):
        vida = self.vida
        collider = pygame.Rect(self.x, self.y, 30, 45)
        self.vida = vida
        return vida, collider

    def animacoes(self, timer):
        #animacao de corrida 
        current_time = pygame.time.get_ticks() #recebe a informação do tempo do frame, usado pra calcular quando vai ser chamado o próximo sprite
        #os códigos de animações são iguais para todas as animações por enquanto, só muda a forma de chamar a animação
        #chama a animação de cair 
        if(self.fall):
            if(self.frame < 4 and current_time - timer > self.animation_cooldown): #caso o frame esteja seja menor que a quantidade de sprites, e o tempo para chamar foi atingido, um novo sprite é desenhado
                if(not self.invertido and self.x <= 405): #verifica se está invertido e se não está na beirada do mapa
                    self.player_sprite = pygame.image.load(self.falling[self.frame])
                elif(self.invertido and self.x >= 0): #caso esteja invertido, entra nessa parte e utiliza a lista de sprites invertidas
                    self.player_sprite = self.falling_invertida[self.frame]
                self.frame += 1
            elif(self.frame >= 4):
                self.frame = 0
            
            print('animação: caindo')
        #chama a animação de pular
        if(self.is_jumping and not self.fall):
            if(self.frame < 4 and current_time - timer > self.animation_cooldown):
                if(not self.invertido and self.x <= 405):
                    self.player_sprite = pygame.image.load(self.jump[self.frame])
                elif(self.invertido and self.x >= 0):
                    self.player_sprite = self.jump_invertida[self.frame]
                self.frame += 1
            elif(self.frame >= 4):
                self.frame = 0
            
            print('animação: pulando')
        #chama a animação de correr
        if(not self.is_jumping and not self.fall):
            if(self.frame < 7 and current_time - timer > self.animation_cooldown):
                if(not self.invertido and self.x <= 405):
                    self.player_sprite = pygame.image.load(self.run[self.frame]).convert_alpha()
                elif(self.invertido and self.x >= 0):
                    self.player_sprite = self.run_invertida[self.frame]
                self.frame += 1
            elif(self.frame == 7):
                self.frame = 0
            
            print('animação: correndo')

        #chama a animação de cair
        if(not self.is_jumping and self.fall):
            if(self.frame < 4 and current_time - timer > self.animation_cooldown):
                if(not self.invertido and self.x <= 405):
                    self.player_sprite = pygame.image.load(self.falling[self.frame]).convert_alpha()
                elif(self.invertido and self.x >= 0):
                    self.player_sprite = self.falling_invertida[self.frame]
                self.frame += 1
            elif(self.frame == 4):
                self.frame = 0
            
            print('animação: caindo')
        
        #inverte o eixo do personagem ao bater nas paredes do mapa
        if(self.x >= 400 and self.inverter_direita):
            self.inverter_direita = False
            self.inverter_esquerda = True
            self.invertido = True
            self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)
            
        if(self.x <= 0 and self.inverter_esquerda):
            self.inverter_direita = True
            self.inverter_esquerda = False
            self.invertido = False
            self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)

        #desenha a personagem na tela
        tela = pygame.display.get_surface()
        tela.blit(self.player_sprite, (self.x, self.y))

    
    def set_timer(self,timer):
        #substitui o tempo atual no script main.py (vairável usada para calcular se irá chamar ou não o próximo sprite)
        current_time = pygame.time.get_ticks()
        if(current_time - timer > self.animation_cooldown):
            timer = current_time
            return timer
        else:
            return timer
        
    def recuar_colisao_inimigo(self):
        # 1 segundo de recuo
        tempo_de_recuo = 1000

        # Salva a posição original do jogador
        x_original = self.x

        # Move o jogador para trás
        self.x -= 50

        # Desenha o jogador na nova posição (recuando)
        screen.blit(self.player_sprite, (self.x, self.y))
        pygame.display.flip()

        # Espera pelo tempo de recuo
        pygame.time.delay(tempo_de_recuo)

        # Restaura a posição original do jogador
        self.x = x_original
