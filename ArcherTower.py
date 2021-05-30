import pygame
import os
from tower import Tower, draw_radius, draw
import math
from Menu import menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'MenuBar_short.png')),
                                 (120, 50))
Upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Upgrade2.png')),
                                     (50, 50))

tower_imgs1 = []
archer_imgs1 = []

for x in range(1, 4):
    print("Yes")
    tower_imgs1.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join('Archer_Tower', 'TowersImages', 'ArcherTower' + str(x) + '.png')),
            (90, 90)))

for x in range(1, 4):
    print("Ofc")
    archer_imgs1.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join('Archer_Tower', 'Archer_images', 'Archer' + str(x) + '.png')), (40, 45)))


class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        # super.__init__(x, y)
        Tower.__init__(self, x, y)
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1
        self.archer_count = 0
        self.range = 130
        self.enemy = []
        self.original_range = self.range
        self.inRange = False
        self.left = False
        self.width = self.height = 90
        # self.timer = time.time()
        self.damage = 1
        self.original_damage = self.damage
        self.menu = menu(self, self.x, self.y, menu_bg, [2000, 6000, "MAX"])
        self.menu.add_btn(Upgrade_btn, "Upgrade")
        self.moving = False
        self.selected_enemy = None
        self.name = "Archer"

    def get_upgrade_cost(self):
        """
        Gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def draw(self, display):
        draw_radius(self, display)

        draw(self, display)

        # img = self.tower_imgs[self.level - 1]
        # display.blit(img, ((self.x - img.get_width() // 2), (self.y - img.get_height() // 2)))

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 15:
                self.archer_count = 0

        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 15]
        display.blit(archer, (self.x - 25, self.y - archer.get_height() - 20))

    def Change_range(self, r):
        """
        Changes range of Archer Tower
        :param r: int
        :return: None
        """
        self.range = r

    def Attack(self, enemies):

        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return:
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]

        if len(enemy_closest) > 0:
            print("Yes, it is done")
            first_enemy = enemy_closest[0]

            if self.archer_count == 20:

                # self.timer = time.time()
                if first_enemy.hit(self.damage):
                    # print("yes, it is hit")
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money


tower_imgs2 = []
archer_imgs2 = []

for x in range(4, 7):
    print("Yes")
    tower_imgs2.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join('Archer_Tower', 'TowersImages', 'ArcherTower' + str(x) + '.png')),
            (80, 90)))

for x in range(1, 4):
    print("Ofc")
    archer_imgs2.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join('Archer_Tower', 'Archer_images', 'Archer' + str(x) + '.png')), (40, 45)))


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        # super.__init__(x, y)
        Tower.__init__(self, x, y)
        self.tower_imgs = tower_imgs2
        self.archer_imgs = archer_imgs2
        self.archer_count = 1
        self.range = 100
        self.inRange = False
        self.left = False
        # self.timer = time.time()
        self.width = self.height = 90
        self.damage = 2
        self.original_range = self.range
        self.original_damage = self.damage
        self.menu = menu(self, self.x, self.y, menu_bg, [3200, 8000, "MAX"])
        self.menu.add_btn(Upgrade_btn, "Upgrade")
        self.name = "Archer2"


'''
        pos = pygame.mouse.get_pos()
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        
        if Enemy.click(pos[0], pos[1]):
            print("Yes, it is done")
            first_enemy = enemy_closest[0]

            if self.archer_count == 20:

                # self.timer = time.time()
                if first_enemy.hit(self.damage):
                    # print("yes, it is hit")
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
'''
