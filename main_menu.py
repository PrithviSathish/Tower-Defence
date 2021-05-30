import pygame
import os
# from Menu import menu, Button
from Game import Game

start_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Play.png')), (150, 150))
logo = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'logo.png')), (700, 200))


class MainMenu:
    def __init__(self):
        self.width = 1000
        self.height = 540
        self.Display = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Menu_bg.png'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.btn = (
            self.width / 2 - start_btn.get_width() / 2, self.height / 2 - start_btn.get_height() / 2,
            start_btn.get_width(),
            start_btn.get_height())

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] + 200 <= y <= self.btn[1] + 200 + self.btn[3]:
                            game = Game(self.Display)
                            game.run()
                            del game

            self.draw()
        pygame.quit()

    def draw(self):
        self.Display.blit(self.bg, (0, 0))
        # self.Display.blit(logo, (self.width / 2 - logo.get_width() / 2, 0))
        self.Display.blit(start_btn, (self.btn[0], self.btn[1] + 200))
        pygame.display.update()
