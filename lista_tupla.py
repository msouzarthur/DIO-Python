#lista.index('elemento') - numero dele
#.sum(lista) - só com numero
#.max/min(lista) - maior valor ou string/ menor valor ou string 
#.append() - adiciona no fim
#.pop() - remove o fim
#.pop(índice) - remove o índice
#.remove(nome) - remove o nome
#.sort() - ordena crescente/alfabetico
#.reverse() - inverte a ordem
#len() - conta o tamanho
numeros = [1,3,5,7]
animais = ['cachorro','elefante','gato']
misto = [1,3,5,'gato','cachorro']
print('listas: ')
print('numeros: ' +str(numeros))
print('animais: ' +str(animais))
print('misto: ' +str(misto))
print('\n')
#soma=0
#for x in numeros:
#    print(x)
#    soma+=x
#print(soma)
novaLista = numeros*3
print('novaLista = numeros*3 > '+str(novaLista))
print('soma dos digitos de numeros: ' +str(sum(numeros)))
print('tem gato em animais? ')
if 'gato' in misto:
    print("já tem gato")
else:
    print("não tem gato")
#---------------------------------
#tupla não se pode alterar 
print('\n')
tupla = (1,10,12,14)
print('tupla: ' + str(tupla))
print('índice 0: '+str(tupla[0]))
print('comprimento: '+str( len(tupla)))
tupla_animal = tuple(animais)
print('converter lista em tupla: tuple(elemento)')
print(tupla_animal)
print('converter tupla em lista: list(elemento)')
print(list(tupla_animal))