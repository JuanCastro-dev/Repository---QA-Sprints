class Calculadora:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def soma(self,n1,n2):
        return n1+n2

    def sub(self,n1,n2):
        return n1-n2

    def mul(self,n1,n2):
        return n1*n2

    def div(self,n1,n2):
        if n2 == 0:
            raise ZeroDivisionError("Impossível dividir um número por zero.")
        return n1/n2

    def resto(self,n1,n2):
        if n2 == 0:
            raise ZeroDivisionError("Impossível dividir um número por zero"
                                    ", portanto não há resto")
        return n1%n2

    def pot(self,n1,n2):
        return n1**n2

    def raiz(self,n1,n2):
        if n2 == 0:
            raise ValueError("Não é possível tirar a raiz zero de um número")
        if n1 < 0:
            raise ValueError("Não é possível tirar uma raiz negativa")
        return n1**(1/n2)

