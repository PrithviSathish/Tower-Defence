import pygame
import os
from Enemy import Enemy

imgs = [pygame.transform.scale(pygame.image.load(os.path.join('Enemy', 'Sco.png')), (64, 64))]


class Scorpion(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        self.name = "Scorpion"
        self.money = 2
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]
