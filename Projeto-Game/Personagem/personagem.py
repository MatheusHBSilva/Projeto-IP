import pygame

class player:

    def __init__(self):
        self.player_sprite = pygame.image.load('personagem/personagem_placeholder.png').convert() #imagem da personagem//quando colocarmos animação, terá que ser modificado
        self.player_sprite = pygame.transform.scale(self.player_sprite, (40, 60)) #resize do tamanho da imagem da personagem
        self.x = 100 #x iniciai da personagem
        self.y = 700 #y inicial da personaem
        self.y_plataforma = self.y #esse y será utilizado para modidicar o y que ela vai descer em relação a plataforma
        self.velocidade = 5
        self.forca_pulo = 15
        self.double_jump_available = False #verifica se é possível dar o double jump nesse momento
        self.double_jump_reset = True #reseta a possibilidade de dar o double jump (essa variável é confusa, ela é mais uma bugfixer)
        self.is_jumping = False #verifica se a personagem esta no ar 
        self.gravidade = 1 #força de gravidade do projeto
        self.jump_height = 0
        self.fall = False

    def movimento(self):
        #siatema de pulo
        keys = pygame.key.get_pressed() #verifica se a tecla 'espaço' foi pressionada

        if(keys[pygame.K_SPACE] and not self.is_jumping): #pulo normal inicial, liberando o código de aumentar a altura
            self.is_jumping = True 
            self.jump_height = 0

        if(keys[pygame.K_SPACE] and self.double_jump_available and self.fall and self.double_jump_reset): #verifica o double jump // o double jump só é liberado caso a altura máxima aconteça, mas é possível mudar essa variável tranquilamente
            self.double_jump_available = False
            self.double_jump_reset = False
            self.fall = False
            self.jump_height = 0
       
        if(self.is_jumping and not self.fall): #aumenta a altura do personagem no eixo Y
            self.y -= self.forca_pulo - self.jump_height
            self.jump_height += 1
            if(self.jump_height >= self.forca_pulo): #quando o personagem chega na altura máxima do pulo, ele começa a descer e autoriza o double jump
                self.fall = True
                self.double_jump_available = True
                self.jump_height = 0

        if(self.fall): #o código de gravidade, bastante semelhante ao código de subida
            self.y += self.gravidade + self.jump_height
            self.jump_height += 1
            if(self.y >= self.y_plataforma):
                self.fall = False
                self.is_jumping = False
                self.double_jump_available = True
                self.y = self.y_plataforma
                self.double_jump_reset = True

        #código de controle automático da movimentação no x e y
        if(self.velocidade > 0):
            if(self.x != 432):
                self.x += self.velocidade

            if(self.x >= 396):
                self.velocidade *= -1
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)

        if(self.velocidade < 0):
            if(self.x != 0):
                self.x += self.velocidade

            if(self.x <= 0):
                self.velocidade *= -1
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)

    def desenhar_player(self):
        tela = pygame.display.get_surface()
        tela.fill((255, 0, 0))
        tela.blit(self.player_sprite, (self.x, self.y))
