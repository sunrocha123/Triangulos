import pytest

class Triangulo:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c and self.b == self.a and self.b == self.c and self.c == self.a and self.c == self.b:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.a and self.b != self.c and self.c != self.a and self.c != self.b:
            return 'escaleno'
        else:
            return 'isósceles'

class Testvalores:

    @pytest.mark.parametrize("a, b, c, tipo_triangulo",[

        (1,1,1,'equilátero'),
        (3,4,9,'escaleno'),
        (2,2,1, 'isósceles')
    ])

    def testa_valores(self, a, b, c, tipo_triangulo):
        t = Triangulo(a,b,c)
        assert t.tipo_lado() == tipo_triangulo