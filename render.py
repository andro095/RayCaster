from math import cos, sin, pi

iros = {
    '1': (71, 120, 179),
    '2': (108, 71, 71),
    '3': (155, 160, 37)
}


class MyRender(object):
    def __init__(self, disp):
        self.disp = disp
        _, _, self.width, self.height = disp.get_rect()

        self.chzu = []
        self.bksize = 50
        self.wH = 50

        self.stpsize = 5

        self.glsColor((255, 255, 255))

        self.x = 75
        self.y = 175
        self.ag = 0
        self.fov = 60

    def glsColor(self, color):
        self.bColor = color

    def glload_map(self, fname):
        f = open(fname).readlines()
        for l in f:
            self.chzu.append(list(l))

    def gldrawRect(self, x, y, iro=(255, 255, 255)):
        self.disp.fill(iro, (x, y, self.bksize, self.bksize))

    def gldrawPlayerIcon(self, color):
        self.disp.fill(color, (self.x - 2, self.y - 2, 5, 5))

    def glcRay(self, rd):
        rds = rd * pi / 180
        dt = 0
        while True:
            x = int(self.x + dt * cos(rds))
            y = int(self.y + dt * sin(rds))

            a = int(x / self.bksize)
            b = int(y / self.bksize)

            if self.chzu[b][a] != ' ':
                return dt, self.chzu[b][a]

            self.disp.set_at((x, y), (255, 255, 255))
            dt += 5

    def glrender(self):
        for x in range(0, int(self.width / 2), self.bksize):
            for y in range(0, self.height, self.bksize):
                a = int(x / self.bksize)
                b = int(y / self.bksize)

                if self.chzu[b][a] != ' ':
                    self.gldrawRect(x, y, iros[self.chzu[b][a]])
        self.gldrawPlayerIcon((0, 0, 0))

        for x in range(int(self.width / 2)):
            ag = self.ag - (self.fov / 2) + (self.fov * x / int(self.width / 2))
            dt, i = self.glcRay(ag)

            cord = int(self.width / 2) + x

            a = self.height / (dt * cos((ag - self.ag) * pi / 180)) * self.wH

            emp = int(int(self.height / 2) - a/2)
            fin = int(int(self.height / 2) + a/2)

            for y in range(emp, fin):
                self.disp.set_at((cord, y), iros[i])

        for x in range(self.height):
            self.disp.set_at((int(self.width / 2), x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) + 1, x), (0, 0, 0))
            self.disp.set_at((int(self.width / 2) -1, x), (0, 0, 0))
