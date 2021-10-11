import shutil

def escreverArquivo(texto):
    arq = open('teste.txt','w')
    arq.write(texto)
    arq.close()
def atualizarArquivo(texto):
    arq = open('teste.txt','a')
    arq.write(texto)
    arq.close()

def lerArquivo(nome):
    arq = open(nome,'r')
    conteudo = arq.read()
    print(conteudo)
    arq.close()

def media_notas(nomeArquivo):
    arq = open(nomeArquivo,'r')
    ficha = []
    alunoNota = arq.read()
    alunoNota = alunoNota.split('\n')
    for x in alunoNota:
        dados = x.split(',')
        nome = dados[0]
        dados.pop(0)
        media = lambda dados:sum([int(i) for i in dados])/4
        print('média de {}: {}'.format(nome,media(dados)))
        ficha.append({nome:media(dados)})
    return ficha
    arq.close()

def copiarArquivo(nome):
    shutil.copy(nome,'C:/Users/arthu/Desktop/')

def moverArquivo(nome):
    shutil.move(nome,'C:/Users/arthu/Desktop')
if __name__ == '__main__':
    #moverArquivo('notas.txt')
    #ficha = media_notas('notas.txt')
    #print(ficha)
    #escreverArquivo('primeira linha\n')
    #atualizarArquivo('Segunda linha\n')
    #lerArquivo('teste.txt')
