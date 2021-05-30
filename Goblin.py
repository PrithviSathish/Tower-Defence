import pygame
from Enemy import Enemy
import os

imgs = []

for x in range(1, 12):
    add_str = str(x)
    imgs.append(pygame.image.load(os.path.join('Enemy', 'GoblinImages', 'R' + add_str + 'E.png')))


class Goblin(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        # self.imgs = [pygame.image.load(os.path.join('GoblinImages', 'R' + str(x) + 'E.png')) for x in range(2, 5)]
        self.name = "Goblin"
        self.max_health = 3
        self.money = 6
        self.health = self.max_health
        self.imgs = imgs[:]
