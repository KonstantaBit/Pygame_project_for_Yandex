import pygame
import sys


class App:
    def __init__(self):
        # Проверка на целостность конфига
        try:
            # Распаковка настроек и конфигов
            with open('config.txt', 'r') as f:
                config = {i.split('=')[0]: i.split('=')[1] for i in f.read().split('\n')}
            # Инициализация pygame
            pygame.init()
            # Установка настроек приложения
            self.running = True
            self.SIZE = self.WIDTH, self.HEIGHT = (int(config['WIDTH']), int(config['HEIGHT']))
            self.screen = pygame.display.set_mode(self.SIZE)
            self.clock = pygame.time.Clock()
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

    def update(self):
        pass

    def draw(self):
        pygame.display.flip()
        pass

    def run(self):
        while self.running:
            self.update()
            self.draw()

            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            self.clock.tick(self.FPS)

            name = '???'
            if self.DISPLAY_FPS:
                name += f' - FPS: {self.clock.get_fps()}'
            pygame.display.set_caption(name)

    def end(self):
        self.running = False

    def terminate(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()
