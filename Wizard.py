import pygame
import os
from .Enemy import Enemy


class Wizard(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        self.imgs = [pygame.transform.scale(pygame.image.load(os.path.join('Mine', 'Enemy', 'Wiz.png')), (40, 50))]

    '''for x in range(20):
        add_str = str(x)
        if x < 10:
            add_str = "0" + add_str

    '''