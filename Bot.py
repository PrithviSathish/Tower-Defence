import pygame
from Enemy import Enemy
import os

imgs = []

for x in range(10, 16):
    add_str = str(x)
    imgs.append(pygame.image.load(os.path.join('Enemy', 'Bot_images', add_str + '.png')))


class Bot(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        self.name = "Bot"
        # self.imgs = [pygame.image.load(os.path.join('GoblinImages', 'R' + str(x) + 'E.png')) for x in range(2, 5)]
        self.max_health = 5
        self.money = 10
        self.health = self.max_health
        self.imgs = imgs[:]
