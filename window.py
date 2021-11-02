import pygame


class Workspace:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/workspace.png")
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
