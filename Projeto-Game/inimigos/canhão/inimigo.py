import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images_right = [pygame.image.load(f'D:\Vscode\projeto do jogo\inimigo\direita{i}.png').convert_alpha() for i in range(1, 5)]
        self.images_left = [pygame.image.load(f'D:\Vscode\projeto do jogo\inimigo\esquerda{i}.png').convert_alpha() for i in range(1, 5)]
        self.image_index = 0
        self.image = self.images_right[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 3
        self.direction_x = 1
        self.walkCount = 0

    def update(self):
        self.rect.x += self.speed_x * self.direction_x

        # Mudar a direção ao atingir as bordas da tela
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction_x *= -1

        # Atualizar a animação
        if self.walkCount >= 33:
            self.walkCount = 0
        self.walkCount += 1
        self.update_image()

    def update_image(self):
        if self.direction_x == 1:
            self.image_index = (self.walkCount // 8) % len(self.images_right)
            self.image = self.images_right[self.image_index]
        else:
            self.image_index = (self.walkCount // 8) % len(self.images_left)
            self.image = self.images_left[self.image_index]

#para colocar o inimigo
## Grupos de sprites
#all_sprites = pygame.sprite.Group()
#enemies = pygame.sprite.Group()

#enemy = Enemy(40, 400)#coordenadas
#all_sprites.add(enemy)#lista dos sprites
#enemies.add(enemy)#chamar a classe
# Grupos de sprites
