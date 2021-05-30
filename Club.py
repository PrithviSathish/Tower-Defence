import pygame
import os
from Enemy import Enemy

imgs = [pygame.transform.scale(pygame.image.load(os.path.join('Enemy', 'Clu.png')), (40, 64))]


class Club(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        self.name = "Club"
        self.money = 10
        self.max_health = 5
        self.health = self.max_health
        self.imgs = imgs[:]
