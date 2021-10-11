#para importar em outro programa
#from funcoes import contador
'''
def contador(lista):
    quantidade = []
    for x in lista:
        count = len(x)
        quantidade.append(count)
    return quantidade
'''
#lamba é função anonima
#armazena na lista o comprimento de cada x na lista
contador = lambda lista: [len(x) for x in lista]
#soma = lambda a,b: a+b
#subtracao = lambda a,b: a-b

calculadora = {
    'soma':lambda a,b: a+b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda a,b: a/b
}

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador(lista))
    soma = calculadora['soma']
    mult = calculadora['multiplicacao']
    sub = calculadora['subtracao']
    print(soma(10,124))
    print(mult(5,2))