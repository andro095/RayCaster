from math import cos, sin, pi
import pygame

class MyRender(object):
    def __init__(self, disp, textures):
        self.disp = disp
        _, _, self.width, self.height = disp.get_rect()

        self.chzu = []
        self.bksize = 50
        self.wH = 50

        self.textures = textures

        self.stpsize = 5

        self.x = 75
        self.y = 175
        self.ag = 0
        self.fov = 60

    def glload_map(self, fname):
        f = open(fname).readlines()
        for l in f:
            self.chzu.append(list(l))

    def gldrawRect(self, x, y, txt):
        txt = pygame.transform.scale(txt, (self.bksize, self.bksize))
        rt = txt.get_rect()
        rt = rt.move((x, y))
        self.disp.blit(txt, rt)

    def gldrawPlayerIcon(self, color):
        self.disp.fill(color, (int(self.x - 2), int(self.y - 2), 5, 5))

    def glcRay(self, rd):
        rds = rd * pi / 180
        dt = 0
        while True:
            x = int(self.x + dt * cos(rds))
            y = int(self.y + dt * sin(rds))

            a = int(x / self.bksize)
            b = int(y / self.bksize)

            if self.chzu[b][a] != ' ':
                tsY = y - b * self.bksize
                tsX = x - a * self.bksize

                if self.bksize - 1 > tsX > 1:
                    ust = tsX
                else:
                    ust = tsY

                tx = ust / self.bksize

                return dt, self.chzu[b][a], tx

            self.disp.set_at((x, y), (255, 255, 255))
            dt += 2

    def glrender(self):
        for x in range(0, int(self.width / 2), self.bksize):
            for y in range(0, self.height, self.bksize):
                a = int(x / self.bksize)
                b = int(y / self.bksize)

                if self.chzu[b][a] != ' ':
                    self.gldrawRect(x, y, self.textures[self.chzu[b][a]])
        self.gldrawPlayerIcon((0, 0, 0))

        for x in range(int(self.width / 2)):
            ag = self.ag - (self.fov / 2) + (self.fov * x / int(self.width / 2))
            dt, wTp, tx = self.glcRay(ag)

            cord = int(self.width / 2) + x

            a = self.height / (dt * cos((ag - self.ag) * pi / 180)) * self.wH

            emp = int(int(self.height / 2) - a / 2)
            fin = int(int(self.height / 2) + a / 2)

            img = self.textures[wTp]
            tx = int(tx * img.get_width())

            for y in range(emp, fin):
                ty = (y - emp) / (fin - emp)
                ty = int(ty * img.get_height())
                tColor = img.get_at((tx, ty))
                self.disp.set_at((cord, y), tColor)

        for x in range(self.height):
            self.disp.set_at((int(self.width / 2), x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) + 1, x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) - 1, x), (0, 0, 0))
