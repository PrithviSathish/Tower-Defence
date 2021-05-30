import pygame
import os
import math
from Menu import menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'MenuBar_short.png')), (120, 50))
Upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Upgrade2.png')), (50, 50))


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.tower_imgs = []
        self.damage = 1
        # Define menu and buttons
        self.menu = menu(self, self.x, self.y, menu_bg, [1500, "MAX"])
        self.menu.add_btn(Upgrade_btn, "Upgrade")
        self.place_color = (30, 230, 30, 130)

    '''
    def draw(self, display):
        """
        Draws the tower
        :param display: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        display.blit(self.tower_imgs, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def draw_radius(self, display):
        if self.selected:
            # Draw range circle
            circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (0, 0, 0, 70), (self.range, self.range), self.range, 0)

            display.blit(circle_surface, (self.x - self.range, self.y - self.range))
    
    '''

    def draw_placement(self, display):
        # Draw range circle
        circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle_surface, self.place_color, (50, 50), 50, 0)  # type: int

        display.blit(circle_surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        """
        returns if tower has been clicked on and selects the clicked tower
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.tower_imgs[self.level - 1]
        # print(img)
        if self.x - img.get_width() // 2 + self.width >= X >= self.x - img.get_width() // 2:
            if self.y + self.height - img.get_height() // 2 >= Y >= self.y - img.get_height() // 2:
                return True
        return False

    def sell(self):
        """
        Calls to sell the tower, returns price of tower
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        Upgrades the tower for a given cost
        :return: None
        """
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def get_upgrade_cost(self):
        """
        returns the upgrade cost; if 0, then cannot upgrade anymore
        :return:int
        """

        return self.price[self.level - 1]

    def move(self, x, y):
        """
        Moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, OtherTower):
        x2 = OtherTower.x
        y2 = OtherTower.y

        dis = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dis >= 100:
            return False
        else:
            return True


def draw(self, display):
    """
     Draws the tower
     :param self:
     :param display: surface
     :return: None
     """
    img = self.tower_imgs[self.level - 1]
    display.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    # Draw menu
    if self.selected:
        self.menu.draw(display)


def draw_radius(self, display):
    if self.selected:
        # Draw range circle
        circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle_surface, (0, 0, 0, 70), (self.range, self.range), self.range, 0)  # type: int

        display.blit(circle_surface, (self.x - self.range, self.y - self.range))


def click(self, X, Y):
    """
    returns if tower has been clicked on
    and selects tower if it was clicked
    :param X: int
    :param Y: int
    :return: bool
    """
    img = self.tower_imgs[self.level - 1]
    if self.x - img.get_width() // 2 + self.width >= X >= self.x - img.get_width() // 2:
        if self.y + self.height - img.get_height() // 2 >= Y >= self.y - img.get_height() // 2:
            return True
    return False
