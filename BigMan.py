import pygame
from Enemy import Enemy
import os

imgs = []

for x in range(1, 10):
    add_str = str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join('Enemy', 'Big Man_images', 'R' + add_str + '.png')), (120, 120)))


class Bigman(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        # self.imgs = [pygame.image.load(os.path.join('GoblinImages', 'R' + str(x) + 'E.png')) for x in range(2, 5)]
        self.name = "Giant"
        self.max_health = 50
        self.money = 500
        self.health = self.max_health
        self.imgs = imgs[:]