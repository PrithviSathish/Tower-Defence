import pygame
import os
from tower import Tower, draw, draw_radius
import math

range_imgs = [pygame.transform.scale(
    pygame.image.load(os.path.join("Archer_Tower", "TowersImages", "SupportTowers", "Sup_tower4.png")),
    (90, 90)),
              pygame.transform.scale(
                  pygame.image.load(os.path.join("Archer_Tower", "TowersImages", "SupportTowers", "Sup_tower5.png")),
                  (70, 70))]


class RangeTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y)
        self.range = 70
        self.effect = [0.2, 0.4]
        self.tower_imgs = range_imgs[:]
        self.width = self.height = 70
        self.name = "Range"

    def draw(self, display):
        # click(self, )
        draw_radius(self, display)
        draw(self, display)
        # display.blit(display, (0, 0))

    def Support(self, towers):
        """
        Will add extra range to each surrounding tower
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + int(tower.range * self.effect[self.level - 1])


damage_imgs = [(pygame.image.load(os.path.join("Archer_Tower", "TowersImages", "SupportTowers", "Sup_tower7.png"))),
               pygame.image.load(os.path.join("Archer_Tower", "TowersImages", "SupportTowers", "Sup_tower8.png"))]


class DamageTower(RangeTower):
    """
    Add damage to surrounding towers
    """

    def __init__(self, x, y):
        Tower.__init__(self, x, y)
        self.range = 70
        self.effect = [0.5, 1]
        self.tower_imgs = damage_imgs[:]
        self.width = self.height = 70
        self.name = "Damage"

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def Support(self, towers):
        """
        Will modify towers according to its ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + int(tower.damage * self.effect[self.level - 1])
