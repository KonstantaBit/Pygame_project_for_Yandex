# Важные либы
import pygame as pg
import sys


class Menu:
    def __init__(self):
        self.running = True
        self.SIZE = self.WIDTH, self.HEIGHT = (700, 500)
        self.screen = pg.display.set_mode(self.SIZE)
        self.clock = pg.time.Clock()
        pg.display.set_icon(pg.image.load('data/Icon.jpg'))
        pg.display.set_caption('Lonely Shooter')

    def update(self):
        pg.surfarray.blit_array(self.screen, pg.surfarray.array3d(pg.image.load('data/Wallpaper.png')))

    def draw(self):
        pg.display.flip()
        self.screen.fill(0)

    def run(self):
        while self.running:
            self.update()
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.terminate()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 170 < pg.mouse.get_pos()[0] < 500 and 250 < pg.mouse.get_pos()[1] < 300:
                        return 7
                    if 170 < pg.mouse.get_pos()[0] < 480 and 320 < pg.mouse.get_pos()[1] < 390:
                        return 1
            self.clock.tick(60)

    def end(self):
        self.running = False

    def terminate(self):
        self.end()
        pg.quit()
        sys.exit()