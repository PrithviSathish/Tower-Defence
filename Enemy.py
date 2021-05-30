import math
import pygame
# from Mine.ArcherTower import ArcherTowerLong, ArcherTowerShort


class Enemy:

    def __init__(self):
        self.level = None
        self.width = 64
        self.height = 64
        self.vel = 3
        self.animation_count = 0
        self.health = 1
        self.path = [(5, 128), (130, 155), (169, 171), (317, 210), (506, 160), (521, 113), (559, 49), (628, 43),
                     (677, 82), (699, 172), (870, 254), (877, 330), (812, 374), (659, 376), (557, 418), (295, 422),
                     (105, 390), (75, 340), (35, 279), (0, 260)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.imgs = []
        self.img = None
        self.move_count = 0
        self.move_dis = 0
        self.flipped = False
        self.max_health = 0
        self.speed_increase = 1.2
        self.selected = False
        self.place_color = (255, 255, 255, 100)

    def draw(self, display):
        """
        Draws the enemy with the given images
        :param display: surface
        :return: None
        """

        self.img = self.imgs[self.animation_count]
        # pygame.time.delay(20)

        # for dot in self.path:
        # pygame.draw.circle(display, (255, 0, 0), dot, 5, 0)

        display.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))
        self.draw_health_bar(display)

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param X: int
        :param Y: int
        :return: Bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def move(self):
        # clock = pygame.time.Clock()
        # clock.tick(10)
        """
        Move enemy
        :return: None
        """
        self.animation_count += 1

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            # print("Yes")
            x2, y2 = (-20, 240)
        else:
            # print("No")
            x2, y2 = self.path[self.path_pos + 1]

        # move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # self.move_count += 1
        Dir = ((x2 - x1) * 5, (y2 - y1) * 5)
        Length = int(math.sqrt((Dir[0]) ** 2 + (Dir[1]) ** 2))
        Dir = (Dir[0] / Length * self.speed_increase, Dir[1] / Length * self.speed_increase)

        if Dir[0] < 0 and not self.flipped:
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + Dir[0]), (self.y + Dir[1]))
        # self.move_dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)
        # self.move_dis += Length

        self.x = move_x
        self.y = move_y

        if Dir[0] >= 0:
            if Dir[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    # self.move_dis = 0
                    # self.move_count = 0
                    self.path_pos += 1

            if Dir[1] < 0:
                if self.x >= x2 and self.y <= y2:
                    # self.move_dis = 0
                    # self.move_count = 0
                    self.path_pos += 1

        else:
            if Dir[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    # self.move_dis = 0
                    # self.move_count = 0
                    self.path_pos += 1

            if Dir[1] < 0:
                if self.x <= x2 and self.y >= y2:
                    # self.move_dis = 0
                    # self.move_count = 0
                    self.path_pos += 1

    def click(self, X, Y):
        """
        returns if enemy has been clicked on
        and selects enemy if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.imgs[self.animation_count]
        if self.x - img.get_width() // 2 + self.width >= X >= self.x - img.get_width() // 2:
            if self.y + self.height - img.get_height() // 2 >= Y >= self.y - img.get_height() // 2:
                return True
        return False

    def draw_selected_circle(self, display):
        # Draw range circle
        circle_surface = pygame.Surface((self.x, self.y), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle_surface, self.place_color, (30, 30), 30, 0)  # type: int

        display.blit(circle_surface, (self.x - 30, self.y - 30))

    def draw_health_bar(self, display):
        """
        Draws the health bar
        :param display: Surface
        :return: None
        """
        length = 50
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(display, (255, 0, 0), (self.x - 30, self.y - 42, length, 6), 0)
        pygame.draw.rect(display, (0, 255, 0), (self.x - 30, self.y - 42, health_bar, 6), 0)

    def hit(self, damage):
        """
        Returns if enemy has died and removes ones health each call
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            return True

        return False
