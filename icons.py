import pygame


class Icon:

    def __init__(self, name, string, x, y):
        self.image = pygame.image.load("assets/icons/{}.png".format(name))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(x=x, y=y)
        self.font = pygame.font.Font('assets/W95FA.otf', 12)
        self.text = self.font.render(string, True, "white")
        self.text_rect = self.text.get_rect(centerx=self.rect.centerx, y=y+self.rect.height * 1.09375)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
