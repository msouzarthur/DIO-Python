#__init__ é o passo inicial, optativo 
#class Calculadora:
#    def __init__(self):
#        pass
#        def soma(self, valor_a, valor_b):
#            return valor_a + valor_b
#        def subtracao(self, valor_a, valor_b):
#            return valor_a - valor_b
#calc = Calculadora()
#print(calc.soma(10,2))
#print(calc.subtracao(10,2))
#etc
#----------------------------------------------------------
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
calc = Calculadora(10,2)
print(calc.soma())
print(calc.subtracao())
print(calc.multiplicacao())
print(calc.divisao())