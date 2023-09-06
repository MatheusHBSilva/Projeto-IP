import pygame

class player:

    #teremos nessa função as variáveis básicas do nosso jogador e nossa manipulação delas
    def __init__(self):
        self.player_sprite = pygame.image.load('personagem/personagem_placeholder.png').convert() #podemos adicionar animação depois, por enquanto place holder
        self.player_sprite = pygame.transform.scale(self.player_sprite, (40, 60)) #escala
        self.x = 100 #x inicial do nosso objeto jogador (meio da tela)
        self.y = 700 #y inicial do nosso jogador (final da tela)
        self.velocidade = 1
        self.forca_pulo = 1
        self.massa = 3
        self.gravidade = 10
        self.is_jumping = False

    def movimento(self):

        event = pygame.event.get()

        '''
        for event in event:
            #responsável por verificar o input do player
            if(event.type == pygame.KEYDOWN):

                if(event.key == pygame.K_SPACE and not self.is_jumping):
                    self.y += self.forca_pulo
                    self.is_jumping = True

                    print('jumped')  
        '''
        
        '''
        #faz o cálculo da gravidade caso o player esteja pulando
        if(self.is_jumping ==  True):
            F =(1 / 2)*self.massa*(self.gravidade**2) 
            self.y-= F 
            
            self.gravidade = self.gravidade-1
            if (gravidade < 0): 
                self.massa =-1
            
            if(gravidade == -6):
                gravidade = 10
                self.massa= 3
                self.is_jumping = False
        '''

        #faz a movimentação automática no eixo X
        if(self.velocidade > 0):
            if(self.x != 432):
                self.x += self.velocidade
            
            if(self.x == 396):
                self.velocidade *= -1
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)
                
        
        if(self.velocidade < 0):
            if(self.x != 0):
                self.x += self.velocidade
            
            if(self.x == 0):
                self.velocidade *= -1
                self.player_sprite = pygame.transform.flip(self.player_sprite, True, False)
    
    
    def desenhar_player(self):
        tela = pygame.display.get_surface()
        tela.blit(self.player_sprite, (self.x,self.y))

        #print(self.x, self.y)
        