class Triangulo:

    def __init__ (self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def semelhantes(self, triangulo):
        lados_triangulo_um = [self.ladoA, self.ladoB, self.ladoC]
        lados_triangulo_dois = [triangulo.ladoA, triangulo.ladoB, triangulo.ladoC]

        semelhancia = 0

        for i in range (len(lados_triangulo_um)):
            if lados_triangulo_dois[i] % lados_triangulo_um[i] == 0:
                semelhancia += 1
        
        if semelhancia == len(lados_triangulo_um):
            return True
        else:
            return False

def TestValores():
    t = Triangulo(2,2,2)
    t2 = Triangulo(4, 4, 4)
    t3 = Triangulo(3,3,3)
    t4 = Triangulo(4,4,4)
    print(t.semelhantes(t2))
    print(t3.semelhantes(t4))

TestValores()