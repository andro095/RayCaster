from render import *
import pygame
from math import cos, sin, pi
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    disp = pygame.display.set_mode((1000, 500))
    cast = MyRender(disp)

    cast.glsColor((128, 0, 0))
    cast.glload_map('chzu.txt')

    flag = True

    while flag:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                flag = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    isRunning = False
                elif ev.key == pygame.K_w:
                    cast.x += cos(cast.ag * pi / 180) * cast.stpsize
                    cast.y += sin(cast.ag * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_s:
                    cast.x -= cos(cast.ag * pi / 180) * cast.stpsize
                    cast.y -= sin(cast.ag * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_a:
                    cast.x -= cos((cast.ag + 90) * pi / 180) * cast.stpsize
                    cast.y -= sin((cast.ag + 90) * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_d:
                    cast.x += cos((cast.ag + 90) * pi / 180) * cast.stpsize
                    cast.y += sin((cast.ag + 90) * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_LEFT:
                    cast.ag -= 5
                elif ev.key == pygame.K_RIGHT:
                    cast.ag += 5

        disp.fill((64, 64, 64))
        cast.glrender()

        pygame.display.flip()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
