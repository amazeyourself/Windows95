import pygame


class Icon:

    def __init__(self, name, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/icons/{}.png".format(name))
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
