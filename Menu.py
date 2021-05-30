import pygame
import os

pygame.font.init()
star = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'star.png')), (35, 25))
star2 = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'star.png')), (25, 15))


class Button:
    """
    Button class for menu objects
    """

    def __init__(self, menu, img, name):
        self.img = img
        self.name = name
        self.x = menu.x - 50
        self.y = menu.y - 105
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        Returns if position has collided with menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def Update(self):
        self.x = self.menu.x - 50
        self.y = self.menu.y - 105


class Play_PauseButton(Button):
    def __init__(self, play_img, pause_img, x, y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self, display):
        if self.paused:
            display.blit(self.play, (self.x, self.y))
        else:
            display.blit(self.pause, (self.x, self.y))


class VButton(Button):
    """
    Button class for menu objects
    """

    def __init__(self, x, y, img, name, cost):
        self.img = img
        self.name = name
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


class menu:
    """
    Menu for holding items
    """

    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        # self.item_names = []
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont('comicsans', 20)
        self.tower = tower

    def add_btn(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        # inc_x = self.width / self.items
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        """
        gets the cost of upgrade to next level
        :return: int
        """
        return self.item_cost[self.tower.level - 1]

    def draw(self, display):
        """
        draws buttons and menu bg
        :param display: Surface
        :return: None
        """
        display.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 110))
        for item in self.buttons:
            item.draw(display)
            display.blit(star, (item.x + item.width + 14, item.y))
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255, 255, 255))
            display.blit(text, (item.x + item.width + 15, item.y + star.get_height() + 3))

    def get_clicked(self, X, Y):
        """
        Returns the clicked item from menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    def update(self):
        """
        Update menu and location
        :return: None
        """
        for btn in self.buttons:
            btn.Update()


class vertical_menu(menu):
    """
    Vertical menu for side-bar of the game
    """

    def __init__(self, x, y, img):

        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont('freesansbold.ttf', 20)

    def add_btn(self, img, name, cost):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        # inc_x = self.width / self.items
        btn_x = self.x - 30
        btn_y = self.y - 80 + (self.items - 1) * 84
        self.buttons.append(VButton(btn_x, btn_y, img, name, cost))

    def get_item_cost(self, name):
        """
        Gets the cost of item
        :param name: str
        :return: int
        """
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost

        return -1

    def draw(self, display):
        """
        draws buttons and menu bg
        :param display: Surface
        :return: None
        """
        display.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 110))
        for item in self.buttons:
            item.draw(display)
            display.blit(star2, (item.x, item.y + item.height + 5))
            text = self.font.render(str(item.cost), 1, (255, 255, 255))
            display.blit(text, (item.x + item.width / 2, item.y + item.height + 5))
