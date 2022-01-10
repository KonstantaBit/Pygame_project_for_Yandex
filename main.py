import pygame as pg
import sys
from screen_impact_objects import *
from structure_classes import *


class App:
    def __init__(self):
        # Проверка на целостность конфига
        try:
            # Распаковка настроек и конфигов
            with open('config.txt', 'r') as f:
                config = {i.split('=')[0]: i.split('=')[1] for i in f.read().split('\n')}
            # Инициализация pygame
            pg.init()
            # Установка настроек приложения
            self.running = True
            self.SIZE = self.WIDTH, self.HEIGHT = (int(config['WIDTH']), int(config['HEIGHT']))
            self.screen = pg.display.set_mode(self.SIZE)
            self.clock = pg.time.Clock()
            self.FPS = int(config['FPS'])
            self.DISPLAY_FPS = bool(int(config['DISPLAY_FPS']))
        except KeyError as error:
            print(f'Фатальная ошибка: нарушена целостность конфига\n'
                  f'Подробнее об ошибке:\n'
                  f'Ключ {str(error)} отсутвует ')
            self.terminate()
        except FileNotFoundError as error:
            print(f'Фатальная ошибка: отсутствует config.txt\n'
                  f'Подробнее об ошибке:\n'
                  f'{str(error)}')
            self.terminate()
        # Данные об оъектах
        self.physical_objects = []
        n = Camera(Cords(20, 20, 150), Angles(0, 82, 45), self, self.WIDTH, self.HEIGHT)
        self.screen_objects = [n, DebugMap(self, n)]
        self.currect_map = []

    def update(self):
        """
        GUI, RENDER, SKYBOX, COLLISIONS, CONTROLS, Physics
        """
        for obj in self.screen_objects:
            obj.impact()
            try:
                obj.update()
            except AttributeError:
                pass

    def draw(self):
        pg.display.flip()

    def run(self):
        while self.running:
            self.update()
            self.draw()

            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(self.FPS)

            name = '???'
            if self.DISPLAY_FPS:
                name += f' - FPS: {self.clock.get_fps()}'
            pg.display.set_caption(name)

    def end(self):
        self.running = False

    def terminate(self):
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()

