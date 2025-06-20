#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # desenha as imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 40))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, (WIN_WIDTH / 2, 80))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 150 + 35 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 150 + 35 * i))

            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:  # evento de pressionar a tecla
                    if event.key == pygame.K_DOWN:  # quando a seta para baixo for pressionada
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # quando a seta para cima for pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1

                    if event.key == pygame.K_RETURN:  # tecla enter for pressionada
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
