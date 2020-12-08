from collections import namedtuple

G = 6.67384e-11

Pos = namedtuple('Pos', ['x', 'y'])
Hastighet = namedtuple('Hastighet', ['x', 'y'])


class Himlakropp():
    def __init__(self, massa, radie, pos, hastighet, color=0):
        self.massa = massa
        self.radie = radie
        self.pos = pos
        self.hastighet = hastighet
        self.color = color


def F(kropp1, kropp2):
    r2 = (kropp2.pos.x - kropp1.pos.x)**2 +\
         (kropp2.pos.y - kropp1.pos.y)**2
    return G*kropp1.massa*kropp2.massa/r2
