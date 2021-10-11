a = int(input('primeiro bimestre: '))
b = int(input('segundo bimestre: '))
c = int(input('terceiro bimestre: '))
d = int(input('quarto bimestre: '))
media = (a+b+c+d)/4
if a<=10 and b<=10 and c<=10 and d<=10 :
    print('media: {}'.format(media))
else:
    print('algum valor inválido')
#a = int(input('Digite um numero: '))
#b = int(input('Digite um numero: '))
#c = int(input('Digite um numero: '))
#if a > b and a > c:
#    print('{} é maior'.format(a))
#elif b>a and b > c:
#    print('{} é maior'.format(b))
#else:
#    print('{} é maior' .format(c))