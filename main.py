from config import *
import pygame
from player import Player
from menu import MainMenu
from sound import Music
from sprite import *
from cameras import *
from debug import debug
from level import Level
from pause import Pause


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self._caption = WINDOW_NAME

    def _pre_init(self):
        pygame.display.set_caption(self._caption)
        self._menu = MainMenu(self.screen, self.clock)
        self._level = Level()

    def run(self):
        self._pre_init()
        self._menu.run()
        self._init()
        self._play_theme()
        self._config()
        self._update()
        self._finish()

    def _init(self):
        self._running = True
        pygame.init()

    def _config(self):
        pygame.display.set_caption(self._caption)
        pygame.mouse.set_visible(True)

    def _update(self):
        while self._running:
            self.screen.fill(BLACK)
            self._level.show()
            self.clock.tick(FPS)
            pygame.display.set_caption('FPS: ' + str(int(self.clock.get_fps())))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_pause()

    def set_pause(self):
        if Pause(self.screen, self.clock).run():
            self.run()

    @staticmethod
    def _finish():
        pygame.quit()

    @staticmethod
    def _play_theme():
        theme = Music()
        theme.play_music()


if __name__ == '__main__':
    game = Game()
    game.run()
