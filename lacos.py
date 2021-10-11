#calculo de primos
#for
#a = int(input('Entre com um valor: '))
a=0
for num in range(a):
    div = 0
    for x in range(1, num+1):
        resto = num%x
        #print(x,resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
#--------------------------------------
#while
a = int(input('Digite valores menos que 10: '))
while a<10:
    print(a)
    a = int(input('Digite valores menos que 10: '))
