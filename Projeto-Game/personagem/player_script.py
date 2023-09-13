import pygame

class Player:

    def __init__(self):
        self.vida = 3
        self.player_sprite = pygame.image.load('personagem/player_run/run-1.png').convert_alpha() #imagem da personagem//quando colocarmos animação, terá que ser modificado
        #self.player_sprite = pygame.transform.scale(self.player_sprite, (30, 45)) #resize do tamanho da imagem da personagem
        self.x = 100 #x inicial da personagem
        self.y = 735 #y inicial da personaem
        self.y_plataforma = self.y #esse y será utilizado para modidicar o y que ela vai descer em relação a plataforma
        self.velocidade = 4
        self.forca_pulo = 20
        self.double_jump_available = False #verifica se é possível dar o double jump nesse momento
        self.double_jump_reset = True #reseta a possibilidade de dar o double jump (essa variável é confusa, ela é mais uma bugfixer)
        self.is_jumping = False #verifica se a personagem esta no ar 
        self.gravidade = 1 #força de gravidade do projeto
        self.sliding = False
        self.jump_height = 0
        self.fall = False
        self.inverter_direita = True
        self.inverter_esquerda = True

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
            if(self.x <= 0 or self.x >= 395): #caso o personagem esteja nas paredes (beirada do mapa), ele entrará em slide pelo código abaixo e sua velocidade de descida será menor
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
                if(self.x < 395):
                    self.x += self.velocidade
            if(self.x >= 395 and self.y == self.y_plataforma):
                self.velocidade *= -1
                self.sliding = False
            if(self.x >= 395 and self.inverter_direita):
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)
                self.inverter_direita = False
                self.inverter_esquerda = True

        if(self.velocidade < 0): #velocidade negativa (indo para a esquerda)
            if(self.x != 0):
                self.x += self.velocidade
            if(self.x <= 0 and self.y == self.y_plataforma): 
                self.velocidade *= -1
                self.sliding = False
            if(self.x <= 0 and self.inverter_esquerda):
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)
                self.inverter_esquerda = False
                self.inverter_direita = True

    def desenhar_player(self):
        tela = pygame.display.get_surface()
        tela.blit(self.player_sprite, (self.x, self.y))

    def shared_data_player(self):
        vida = self.vida
        collider = pygame.Rect(self.x, self.y, 30, 45)

        self.vida = vida
        
        return vida, collider
        
