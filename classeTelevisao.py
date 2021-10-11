class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = -1
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def canal(self):
        if self.ligada:
            self.canal
    def aumentaCanal(self):
        if self.ligada:
            self.canal+=1
    def diminuiCanal(self):
        if self.ligada:
            self.canal-=1

if __name__ == '__main__':    
    tv = Televisao()
    print('tv está ligada: {}'.format(tv.ligada))
    tv.power()
    print('tv está ligada: {}'.format(tv.ligada))
    print('canal atual: {}'.format(tv.canal))
    print('aumenta canal')
    tv.aumentaCanal()
    print('canal atual: {}'.format(tv.canal))
    print('aumenta canal')
    tv.aumentaCanal()
    print('canal atual: {}'.format(tv.canal))
    print('diminui canal')
    tv.diminuiCanal()
    print('canal atual: {}'.format(tv.canal))
    print('diminui canal')
    tv.diminuiCanal()
    print('canal atual: {}'.format(tv.canal))
