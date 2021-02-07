import math

class Triangulo:

    def __init__ (self, cateto_adjacente, cateto_oposto, hipotenusa):
        self.cateto_adjacente = cateto_adjacente
        self.cateto_oposto = cateto_oposto
        self.hipotenusa = hipotenusa

    def retangulo(self):
        if math.pow(self.hipotenusa,2) == math.pow(self.cateto_adjacente,2) + math.pow(self.cateto_oposto,2):
            return True
        else:
            return False

def TestValores():
    t = Triangulo(1,3,5)
    t2 = Triangulo(3, 4, 5)
    print(t.retangulo())
    print(t2.retangulo())

TestValores()