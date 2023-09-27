import pygame, sys

class Mainmenu:

    def __init__(self):
        self.img = pygame.image.load("menu_img.jpeg").convert_alpha()
        self.img = pygame.transform.scale(self.img, (435,768))
        self.x = -2
        self.y = 0
       
        font = pygame.font.SysFont("Arial", 30)

        self.texto_start = font.render("START", True, (191, 64, 191))
        self.texto_quit = font.render("QUIT", True, (191, 64, 191))

        self.start_collider =  pygame.Rect(186, 600, 80, 20)
        self.quit_collider =  pygame.Rect(186, 650, 80, 20)

        self.render_menu = True
    
    def desenhar(self):
        if(self.render_menu):
            tela = pygame.display.get_surface()
            tela.blit(self.img, (self.x, self.y))
            tela.blit(self.texto_start, (176, 600))
            tela.blit(self.texto_quit, (186, 650))

    def logicamenu(self):
        x, y = pygame.mouse.get_pos()
        box_collider_mouse = pygame.Rect(x, y, 10, 10)
        left, middle, right= pygame.mouse.get_pressed(num_buttons=3)

        if(self.start_collider.colliderect(box_collider_mouse) and left == True):
            self.render_menu = False

        if(self.quit_collider.colliderect(box_collider_mouse) and left == True):
            sys.exit()



    