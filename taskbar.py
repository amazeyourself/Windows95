import pygame
from datetime import datetime


class Taskbar:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/taskbar.png")
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Hour:
    def __init__(self, x, y):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        interval = "PM"

        self.hour = "{} {}".format(current_time, interval)
        self.font = pygame.font.Font('assets/W95FA.otf', 18)
        self.text = self.font.render(self.hour, True, "black")
        self.text_rect = self.text.get_rect(x=x, y=y)

    def draw(self, screen):
        self.text = self.font.render(self.hour, True, "black")
        screen.blit(self.text, self.text_rect)


class Start:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/start.png")
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
