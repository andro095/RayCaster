from math import cos, sin, pi, atan2
import pygame


def degtorad (angle):
    return angle * pi / 180

class MyRender(object):
    def __init__(self, disp, textures, enemies):
        self.disp = disp
        _, _, self.width, self.height = disp.get_rect()

        self.chzu = []
        self.zbuffer = [-float('inf') for z in range(int(self.width / 2))]
        self.bksize = 50
        self.wH = 50

        self.textures = textures
        self.enemies = enemies

        self.stpsize = 5

        self.x = 75
        self.y = 175
        self.ag = 30
        self.fov = 60

    def glload_map(self, fname):
        self.x = 75
        self.y = 175
        self.ag = 30
        if self.chzu != []:
            self.chzu = []
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

    def glSprite(self, spt, tamah):

        bunW = self.width / 2
        bunH = self.height / 2

        sAng = atan2(spt['y'] - self.y, spt['x'] - self.x) * 180 / pi
        sAng %= 360
        sAng = degtorad(sAng)

        sOku = ((self.x - spt['x']) ** 2 + (self.y - spt['y']) ** 2) ** 0.5

        sH = (self.height / sOku) * tamah
        art = spt["texture"].get_width() / spt["texture"].get_height()
        sW = sH * art

        fovR = degtorad(self.fov)
        angR = degtorad(self.ag % 360)

        sX = int((self.width * 3 / 4) + ((sAng - angR) * bunW / fovR) - (sW/2))
        sY = int(bunH - (sH / 2))

        for x in range(sX, int(sX + sW)):
            for y in range(sY, int(sY + sH)):
                if self.width > x > bunW:
                    if sOku <= self.zbuffer[x - int(bunW)]:
                        tx = int((x - sX) * spt["texture"].get_width() / sW)
                        ty = int((y - sY) * spt["texture"].get_height() / sH)

                        tColor = spt["texture"].get_at((tx, ty))

                        if 128 < tColor[3] and (152, 0, 136, 255) != tColor:
                            self.zbuffer[x - int(bunW)] = sOku
                            self.disp.set_at((x, y), tColor)

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

            self.zbuffer[x] = dt

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

        for enemy in self.enemies:
            self.disp.fill(pygame.Color("black"), (enemy['x'], enemy['y'], 3, 3))
            self.glSprite(enemy, 30)

        for x in range(self.height):
            self.disp.set_at((int(self.width / 2), x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) + 1, x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) - 1, x), (0, 0, 0))
