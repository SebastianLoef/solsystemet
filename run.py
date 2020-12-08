from collections import namedtuple

G = 6.67384e-11
dt = 1

Pos = namedtuple('Pos', ['x', 'y'])
Hastighet = namedtuple('Hastighet', ['x', 'y'])
Kraft = namedtuple('Kraft' ['x', 'y'])


class Himlakropp():
    def __init__(self, massa, radie, pos, hastighet, color=0):
        self.massa = massa
        self.radie = radie
        self.pos = pos
        self.hastighet = hastighet
        self.color = color


def F(kropp1, kropp2):
    dx = kropp1.pos.x - kropp2.pos.x
    dy = kropp1.pos.y - kropp2.pos.y
    F_x = G*kropp1.massa*kropp2.massa/dx
    F_y = G*kropp1.massa*kropp2.massa/dy
    return Kraft(F_x, F_y)


himlakroppar = []


def updatera_hastigheter():
    for kropp in himlakroppar:
        alla_krafter = []
        for annan_kropp in himlakroppar:
            alla_krafter(F(kropp, annan_kropp))
        F_sum = sum(kraft.x for kraft in alla_krafter) 
        kropp.hastighet.x += F_sum/kropp.massa*dt


def updatera_positioner():
    for kropp in himlakroppar:
        kropp.pos.x += kropp.hastighet.x*dt
        kropp.pos.y += kropp.hastighet.y*dt
