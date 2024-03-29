from pyth_files.config import *
import pygame
from pyth_files.menu import MainMenu
from pyth_files.sound import *
from pyth_files.sprite import *
from pyth_files.cameras import *
from pyth_files.level import Level
from pyth_files.pause import Pause
from pyth_files.fade import Fade
from pyth_files.statistic import Statistics

"""Класс игры, из которого всё запускается"""


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self._caption = WINDOW_NAME
        self.theme = Music()

    def _pre_init(self):
        pygame.display.set_caption(self._caption)
        pygame.display.set_icon(load_image(WINDOW_ICON_PATH, WINDOW_ICON_NAME))
        self.theme.path = MENU_THEME
        self.theme.init_track()
        self.statistic = Statistics()
        self._menu = MainMenu(self.screen, self.clock, self.theme)
        self._level = Level(self.screen, self.clock, self.run, self.statistic, self.theme)
        SoundEffect.change_effects_volume(
            get_volume_from_fson()[
                1] if SoundEffect.return_volume() > MAX_EFFECT_VOLUME else SoundEffect.return_volume())

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
        """Рисуем лвл и проверяем нажатия на кнопки"""
        Fade(self.screen).fade_in(FADE_SPEED_MENU)
        self._level.show()
        Fade(self.screen).fade_out(FADE_SPEED_MENU)
        pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT, dialogue='dialogue_1'), 200)
        while self._running:
            self._level.show()
            self.clock.tick(FPS)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_pause()
                if event.type == pygame.USEREVENT:
                    self._level.dialogs_check(event.dialogue)

    def set_pause(self):
        """Ставим паузу"""
        if Pause(self.screen, self.clock, self.theme).run():
            self.run()

    def _play_theme(self):
        """Включаем музыку"""
        self.theme.path = MUSIC_FILES
        self.theme.init_track()
        self.theme.play_music()

    @staticmethod
    def _finish():
        """Выходим"""
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
