import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def display(self):
        self.screen.fill('#018382')
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption('Windows95 - CallMeKitsu.')
Game(screen).run()

pygame.quit()
