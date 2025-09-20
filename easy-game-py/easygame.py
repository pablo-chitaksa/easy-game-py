# Commands

import pygame
import time
import sys

class TestWindow():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("EasyGame TEST WINDOW")

    arial36 = pygame.font.SysFont('arial', 36)
    testtxt = arial36.render('Hello! This is test window of EasyGame based on pygame!', True, (255, 255,255))
    screen.blit(testtxt, (0, 0))
class Loop():
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
                sys.exit()

        pygame.display.flip()
