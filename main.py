from render import *
import pygame
from math import cos, sin, pi
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txts = {
        '1': pygame.image.load('./textures/brick.jpg'),
        '2': pygame.image.load('./textures/clear.jpg'),
        '3': pygame.image.load('./textures/dark.jpg'),
        '4': pygame.image.load('./textures/stone.jpg'),
        '5': pygame.image.load('./textures/white.jpg')
    }


    pygame.init()
    disp = pygame.display.set_mode((1000, 500), pygame.DOUBLEBUF | pygame.HWACCEL)
    disp.set_alpha(None)
    tkei = pygame.time.Clock()
    ltr = pygame.font.SysFont("Arial", 30)

    def incF():
        fs = str(int(tkei.get_fps()))
        fs = ltr.render(fs, 1, pygame.Color("white"))
        return fs

    cast = MyRender(disp, txts)
    cast.glload_map('chzu.txt')

    flag = True

    while flag:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                flag = False

            nX = cast.x
            nY = cast.y

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    isRunning = False
                elif ev.key == pygame.K_w:
                    nX += cos(cast.ag * pi / 180) * cast.stpsize
                    nY += sin(cast.ag * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_s:
                    nX -= cos(cast.ag * pi / 180) * cast.stpsize
                    nY -= sin(cast.ag * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_a:
                    nX -= cos((cast.ag + 90) * pi / 180) * cast.stpsize
                    nY -= sin((cast.ag + 90) * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_d:
                    nX += cos((cast.ag + 90) * pi / 180) * cast.stpsize
                    nY += sin((cast.ag + 90) * pi / 180) * cast.stpsize
                elif ev.key == pygame.K_LEFT:
                    cast.ag -= 5
                elif ev.key == pygame.K_RIGHT:
                    cast.ag += 5

                a = int(nX / cast.bksize)
                b = int(nY / cast.bksize)

                if cast.chzu[b][a] == ' ':
                    cast.x = nX
                    cast.y = nY

        disp.fill(pygame.Color("gray"))

        disp.fill(pygame.Color("saddlebrown"), (int(cast.width / 2), 0, int(cast.width / 2), int(cast.height / 2)))

        disp.fill(pygame.Color("dimgray"), (int(cast.width / 2), int(cast.height / 2), int(cast.width / 2), int(cast.height / 2)))

        cast.glrender()

        disp.fill(pygame.Color("black"), (0, 0, 30, 30))

        disp.blit(incF(), (0,0))
        tkei.tick(30)

        pygame.display.update()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
