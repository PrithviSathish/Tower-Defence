import pygame
import time
import random
import os
from Scorpion import Scorpion
from Club import Club
from Bot import Bot
from Goblin import Goblin
from BigMan import Bigman
from Junior_BigMan import junior_Bigman
from ArcherTower import ArcherTowerLong, ArcherTowerShort
from SupportTower import RangeTower, DamageTower
from Menu import vertical_menu, Play_PauseButton

pygame.font.init()
pygame.mixer.init()
pygame.init()

path = [(5, 128), (130, 155), (169, 171), (317, 210), (506, 160), (521, 113), (559, 49), (628, 43),
        (677, 82), (699, 172), (870, 254), (877, 330), (812, 374), (659, 376), (557, 418), (295, 422),
        (105, 390), (75, 340), (35, 279), (0, 260)]

lives_img = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', "Lives_images", "Heart.png")),
                                   (40, 40))
star = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'star.png')), (35, 25))
side_menu = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'MenuBar_long.png')),
                                   (90, 380))

buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Buy_Archer1.png')),
                                     (60, 60))
buy_archer2 = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Buy_Archer2.png')),
                                     (60, 60))
buy_damage = pygame.transform.scale(
    pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Increase_damage.png')), (60, 60))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Increase_range.png')),
                                   (60, 60))

play_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Battle.png')), (90, 90))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Pause.png')), (95, 95))

sound_btn = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Music.png')), (78, 78))
sound_btn_off = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Music_off.png')),
                                       (75, 75))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join('MenuAndLife', 'Menu_images', 'Wave.png')), (290, 155))

attack_tower_name = ["Archer", "Archer2"]
support_tower_name = ["Range", "Damage"]

pygame.mixer.music.load(os.path.join('Music', 'NewMusic.mp3'))

# (scorpions, goblins, clubs, bots, Junior_Big Man, Big Man)
waves = [
    [20, 0, 0, 0, 0, 0],
    [50, 10, 0, 0, 0, 0],
    [50, 20, 10, 0, 0, 0],
    [100, 50, 0, 10, 0, 0],
    [0, 100, 50, 10, 0, 0],
    [100, 50, 0, 0, 1, 0],
    [0, 100, 100, 100, 0, 0],
    [200, 100, 100, 100, 0, 0],
    [0, 100, 200, 200, 0, 0],
    [100, 100, 0, 20, 0, 0],
    [0, 0, 20, 20, 2, 1],
    [0, 100, 100, 100, 5, 0],
    [0, 50, 100, 100, 10, 2],
    [0, 10, 10, 10, 20, 2],
    [0, 0, 100, 100, 20, 3],
    [0, 50, 100, 100, 20, 4],
    [200, 100, 100, 100, 30, 5],

]


class Game:
    def __init__(self, Display):
        self.width = 1000
        self.height = 540
        self.Display = Display
        self.enemy = []
        self.attack_tower = []
        self.support_tower = []
        self.lives_having = int(self.Backup_life())
        self.life = self.lives_having
        self.coins_having = int(self.Backup_coins())
        self.money = self.coins_having
        self.bg = pygame.image.load(os.path.join('Background_images', 'Background.PNG'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.font = pygame.font.SysFont('comicsans', 40)
        self.selected_towers = None
        self.selected_enemies = None
        self.menu = vertical_menu(self.width - side_menu.get_width() + 48, 210, side_menu)
        self.moving_object = None
        self.music_on = True
        self.Play_PauseButton = Play_PauseButton(play_btn, pause_btn, 2, self.height - 90)
        self.SoundButton = Play_PauseButton(sound_btn, sound_btn_off, 92, self.height - 81)

        self.menu.add_btn(buy_archer1, "Buy_Archer", 500)
        self.menu.add_btn(buy_archer2, "Buy_Archer2", 800)
        self.menu.add_btn(buy_damage, "Buy_Damage", 1000)
        self.menu.add_btn(buy_range, "Buy_Range", 1000)

        self.waves_finished = int(self.Backup_wave())
        self.wave = self.waves_finished
        self.current_wave = waves[self.wave][:]
        self.pause = True
        # self.clicks = []

    def Backup_coins(self):
        """
        Returns the coins to start the game with that amount
        :return: int
        """
        coins_file = open(os.path.join('Backup', 'coins_file.txt'), 'r+')
        self.coins_having = coins_file.readlines()
        return self.coins_having[0]

    def Backup_wave(self):
        """
        Returns the wave to start the game with that wave
        :return: int
        """
        waves_file = open(os.path.join('Backup', 'wave_file.txt'), 'r+')
        self.waves_finished = waves_file.readlines()
        return self.waves_finished[0]

    def Backup_life(self):
        """
        Returns the life to start the game with that life
        :return: int
        """
        life_file = open(os.path.join('Backup', 'life_file.txt'), 'r+')
        self.lives_having = life_file.readlines()
        return self.lives_having[0]

    def gen_enemy(self):
        """
        generate the next enemy of enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemy) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.Play_PauseButton.paused = self.pause

        else:
            wave_enemies = [Scorpion(), Goblin(), Club(), Bot(), junior_Bigman(), Bigman()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemy.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def Backup2_coins(self):
        """
        returns the money you have left after the end of the game
        :return: int
        """
        coins_file = open(os.path.join('Backup', 'coins_file.txt'), "w+")
        coins_file.write(str(self.money))
        return self.coins_having

    def Backup2_wave(self):
        """
        returns the wave you are in after the end of the game
        :return: int
        """
        wave_file = open(os.path.join('Backup', 'wave_file.txt'), "w+")
        wave_file.write(str(self.wave))
        return self.waves_finished

    def Backup2_life(self):
        """
        returns the life you are in after the end of the game
        :return: int
        """
        life_file = open(os.path.join('Backup', 'life_file.txt'), "w+")
        life_file.write(str(self.wave))
        return self.lives_having

    def run(self):
        pygame.mixer.music.play(loops=-1)
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(100)

            if not self.pause:
                # Enemy's Incoming
                if time.time() - self.timer >= random.randrange(2, 4):
                    self.timer = time.time()
                    self.gen_enemy()
                    # self.enemy.append(random.choice([Bot(), Scorpion(), Goblin(), Club()]))

            pos = pygame.mouse.get_pos()

            # check for moving objects
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_tower[:] + self.support_tower[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (230, 30, 30, 130)
                        self.moving_object.place_color = (230, 30, 30, 130)
                    else:
                        tower.place_color = (30, 230, 30, 130)
                        if not collide:
                            self.moving_object.place_color = (30, 230, 30, 130)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Backup2_coins()
                    self.Backup2_wave()
                    self.Backup2_life()
                    # self.Tower_Backup()
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If moving object and clicking objects
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_tower[:] + self.support_tower[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_name:
                                self.attack_tower.append(self.moving_object)

                            elif self.moving_object.name in support_tower_name:
                                self.support_tower.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        # Check for Play or Pause
                        if self.Play_PauseButton.click(pos[0], pos[1]):
                            self.pause = not self.pause
                            self.Play_PauseButton.paused = self.pause

                        # Regulating Music
                        if self.SoundButton.click(pos[0], pos[1]):
                            self.music_on = not self.music_on
                            self.SoundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # Check if Menu buttons are clicked
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            Cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= Cost:
                                self.money -= Cost
                                self.add_tower(side_menu_button)

                        # Check if Towers are clicked
                        btn_clicked = None
                        if self.selected_towers:
                            btn_clicked = self.selected_towers.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_towers.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_towers.upgrade()

                        if not btn_clicked:
                            # Attack tower click
                            for atw in self.attack_tower:
                                if atw.click(pos[0], pos[1]):
                                    # print("Attack tower selected: " + str(atw))
                                    atw.selected = True
                                    self.selected_towers = atw
                                else:
                                    atw.selected = False

                            # Support tower click
                            for stw in self.support_tower:
                                if stw.click(pos[0], pos[1]):
                                    # print("Attack tower selected: " + str(stw))
                                    stw.selected = True
                                    self.selected_towers = stw
                                else:
                                    stw.selected = False

                        # check if enemy clicked
                        for en in self.enemy:
                            if en.click(pos[0], pos[1]):
                                if not en.selected:
                                    en.selected = True
                                    self.selected_enemies = en

                                if en.selected:
                                    en.selected = False
                                    self.selected_enemies = en
            if not self.pause:
                to_del = []
                for en in self.enemy:
                    en.move()
                    if en.x < -15:
                        to_del.append(en)

                for d in to_del:
                    self.life -= 1
                    self.enemy.remove(d)

                for atw in self.attack_tower:
                    self.money += atw.Attack(self.enemy)

                for stw in self.support_tower:
                    stw.Support(self.attack_tower)

                # If we lose
                if self.life <= 0:
                    print("You lose")
                    running = False

            self.draw()

    def point_to_line(self, tower):
        """
        Returns if you can place tower based on distance from the path
        :param tower: Tower
        :return: Bool
        """
        '''
        closest = []
        for point in path:
            distance = math.sqrt((tower.x - point[0]) ** 2 + (tower.y - point[1]) ** 2)
            closest.append([distance, point])

        closest.sort(key=lambda x: x[0])
        x = closest[0][1]
        y = closest[1][1]

        coefficients = np.polyfit(x, y, 1)
        a = coefficients[0]
        b = coefficients[1]
        c = a * x[0] + b * x[1]
        # line_vector = (closest2[0] - closest1[0], closest2[1] - closest1[1])
        # slope = line_vector[1] / line_vector[0]
        # B = 1 / slope
        # c = closest1[1] - closest1[0] * slope

        dis = abs((a * x[0] + b * x[1]) / math.sqrt(a * a + b * b))
        # line_vector[0] ** 2 + line_vector[1] ** 2))
        # print(dis)
        '''
        return True

    def draw(self):
        self.Display.blit(self.bg, (0, 0))

        # Redraw selected tower
        if self.selected_towers:
            self.selected_towers.draw(self.Display)

        if self.selected_enemies:
            self.selected_enemies.draw_selected_circle(self.Display)

        # Drawing attack Towers
        for atw in self.attack_tower:
            atw.draw(self.Display)

        # Drawing support Towers
        for stw in self.support_tower:
            stw.draw(self.Display)

        # Drawing enemies
        for en in self.enemy:
            en.draw(self.Display)

        # Draw Play Pause Button
        self.Play_PauseButton.draw(self.Display)

        # Draw music toggle button
        self.SoundButton.draw(self.Display)

        # Draw menu
        self.menu.draw(self.Display)

        # Draw placement rings
        if self.moving_object:
            for tower in self.attack_tower:
                tower.draw_placement(self.Display)

            for tower in self.support_tower:
                tower.draw_placement(self.Display)

            self.moving_object.draw_placement(self.Display)

        # Drawing lives
        text = self.font.render(str(self.life) + "x", 1, (255, 255, 255))

        life = lives_img
        start_life = self.width
        self.Display.blit(text, (start_life - text.get_width() - 60, 15))
        self.Display.blit(life, (start_life - life.get_width() - 5, 10))

        # Draw money
        text = self.font.render(str(self.money) + "x", 1, (255, 255, 255))

        money = pygame.transform.scale(star, (60, 50))
        start_life = self.width
        self.Display.blit(text, (start_life - text.get_width() - 60, 75))
        self.Display.blit(money, (start_life - life.get_width() - 15, 60))

        # Draw moving object
        if self.moving_object:
            self.moving_object.draw(self.Display)

        # Draw wave
        self.Display.blit(wave_bg, (-70, -40))
        text = self.font.render("Wave # " + str(self.wave), 1, (255, 255, 255))
        self.Display.blit(text, (wave_bg.get_width() / 2 - text.get_width() / 2 - 75, 23))

        pygame.display.update()

    def add_tower(self, name):
        global object_list, obj
        x, y = pygame.mouse.get_pos()
        name_list = ["Buy_Archer", "Buy_Archer2", "Buy_Damage", "Buy_Range"]
        object_list = [ArcherTowerLong(x, y), ArcherTowerShort(x, y), DamageTower(x, y), RangeTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
            print(obj)
        except Exception as e:
            print(str(e), ": Not a VALID NAME")

    def Tower_Backup(self):
        print("obj: " + str(obj))


'''
Display = pygame.display.set_mode((1000, 540))
g = Game(Display)
g.run()
'''
