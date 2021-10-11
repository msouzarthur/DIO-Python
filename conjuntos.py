#desconsidera elementos repetidos
#.add(elemento) - adiciona elemento 
#.discard(elemento) - remove elemento

#fazer isso remove os repetidos
#converter lista em conjunto - conjunto=set(lista)
#converter conjunto em lista - lista=list(conjunto)
conjunto = {1,2,3,4,5,5,5}
print('conjunto = {}'.format(conjunto))
print('adicionar no conjuto: .add(elemento')
conjunto.add(99)
print('conjunto: {}'.format(conjunto))
print('remover do conjunto: .discard(elemento)')
conjunto.discard(1)
print(conjunto)
conjuntoA = {0,1,3,5,7,9}
conjuntoB = {0,8,6,4,2,0}
conjuntoAB = conjuntoA.union(conjuntoB)
print('conjuntoA: {}'.format(conjuntoA))
print('conjuntoB: {}'.format(conjuntoB))
print('união de conjuntos: conjunto.union(outro conjunto)')
print('conjuntoAB: {}'.format(conjuntoA.union(conjuntoB)))
print('interseção de conjuntos: conjunto.intersection(outro conjunto)')
print('interseção: {}'.format(conjuntoA.intersection(conjuntoB)))
print('diferença de conjuntos: conjunto.difference(outro conjunto)')
print('diferença de A e B: {}'.format(conjuntoA.difference(conjuntoB)))
print('diferença de B e A: {}'.format(conjuntoB.difference(conjuntoA)))
print('diferença simétrica: conjunto.symetric_differente(outro conjunto)')
print('diferença simétrica: {}'.format(conjuntoA.symmetric_difference(conjuntoB)))
print('está contido em: conjunto.issubset(outro conjunto)')
print('A está contido em B: {}'.format(conjuntoA.issubset(conjuntoB)))
print('contem e mais: conjunto.issuperset(outro conjunto)')
print('A é um superset de B: {}'.format(conjuntoA.issuperset(conjuntoB)))
print('AB é um superset de B: {}'.format(conjuntoAB.issuperset(conjuntoB)))
print('AB é um superset de A: {}'.format(conjuntoAB.issuperset(conjuntoA)))
