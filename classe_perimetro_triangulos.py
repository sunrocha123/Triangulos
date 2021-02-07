import pytest

class Triangulo:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            return self.a + self.b + self.c
        else:
            return 'Não existe lado negativo para um triângulo'

class Testvalores:

    @pytest.mark.parametrize("a, b, c, perimetro_esperado",[

        (1,1,1,3),
        (2,2,2,6),
        (16,14,20,50),
        (-2,10,1,'Não existe lado negativo para um triângulo')
    ])

    def testa_valores(self, a, b, c, perimetro_esperado):
        t = Triangulo(a,b,c)
        assert t.perimetro() == perimetro_esperado