import pygame
from icons import Icon


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.workspace = Icon("computer_explorer_cool-0",25, 25)
        self.network = Icon("network_normal_two_pcs-5", 25, 125)
        self.mailing = Icon('mailbox_world-2', 25, 225)
        self.bin = Icon('recycle_bin_empty_cool-0', 25, 325)
        self.msn = Icon('msn_cool-4', 25, 425)
        self.explorer = Icon('briefcase-2', 25, 525)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def display(self):
        self.screen.fill('#018382')
        self.workspace.draw(self.screen)
        self.network.draw(self.screen)
        self.mailing.draw(self.screen)
        self.bin.draw(self.screen)
        self.msn.draw(self.screen)
        self.explorer.draw(self.screen)
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
