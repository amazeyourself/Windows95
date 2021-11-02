import pygame
from icons import Icon
from taskbar import Taskbar, Hour, Start, Menu
from window import Workspace

FPS = 60
WIDTH = 960
HEIGHT = 720
TITLE = 'Windows95 - CallMeKitsu.'
ICON = pygame.image.load('assets/app_icon.png')


class Game:
    def __init__(self, screen):
        print('© CopyRight 2021 CallMeKitsu')
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        # ==={ icônes du bureau }==================================================================================
        self.workspace = Icon("computer_explorer_cool-0", "Poste de travail", 35, 25)
        self.network = Icon("network_normal_two_pcs-5", "Voisinage réseau", 35, 90)
        self.mailing = Icon('mailbox_world-2', "Boîte de réception", 35, 155)
        self.bin = Icon('recycle_bin_empty_cool-0', "Corbeille", 35, 220)
        self.msn = Icon('internet_connection_wiz-4', "The Internet", 35, 285)
        self.explorer = Icon('briefcase-4', "Porte-documents", 35, 345)

        # ==={ barre des tâches }==================================================================================
        self.taskbar = Taskbar(0, 720 - 42)
        self.hour = Hour(882, 693)
        self.start = Start(0, 720 - 41)
        self.menu = Menu(2, 720 - 441.84)
        self.show_menu = 1

        # ==={ poste de travail }==================================================================================
        self.workspace_x = 960 / 3
        self.workspace_y = 720 / 3
        self.workspace_moved = 1
        self.window_workspace = Workspace(self.workspace_x, self.workspace_y)
        self.show_workspace = 1

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if self.start.rect.collidepoint(x, y):
                    self.show_menu += 1
                if self.workspace.rect.collidepoint(x, y):
                    self.show_workspace += 1
                # if Rect(left, top, width, height).collidepoint(x, y):
                # self.show_workspace += 1

    def update(self):
        pass

    def display(self):
        self.screen.fill('#018382')

        # ==={ icônes du bureau }==================================================================================
        self.workspace.draw(self.screen)
        self.network.draw(self.screen)
        self.mailing.draw(self.screen)
        self.bin.draw(self.screen)
        self.msn.draw(self.screen)
        self.explorer.draw(self.screen)

        # ==={ barre des tâches }==================================================================================
        self.taskbar.draw(self.screen)
        self.hour.draw(self.screen)
        self.start.draw(self.screen)
        if self.show_menu % 2 == 0:
            self.menu.draw(self.screen)

        # ==={ poste de travail }==================================================================================
        if self.show_workspace % 2 == 0:
            self.window_workspace.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(FPS)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)
Game(screen).run()

pygame.quit()
