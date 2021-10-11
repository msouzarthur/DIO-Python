#usar em sites
import requests
def retornaInfoCep(cep):
    #r = requests.get('https://viacep.com.br/ws/95630000/json/')
    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    #se printar 200, deu certo
    #diferente de 200, link tá errado
    print(r.status_code)
    print(r.text)
    #print(type(r.text))
    #print(type(r.json()))
    #informações em específico
    info = r.json()
    print(info['localidade'])
def retornaDadosPokemon(poke):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(poke))
    dados = r.json()
    return dados
def retornaResponse(url):
    r = requests.get(url)
    return r.text
if __name__ == '__main__':
    pass
    #cep = input('Digite o cep: ')
    #retornaInfoCep(cep)
    #nome = input('Digite o nome do pokemon: ')
    #dados = retornaDadosPokemon(nome)
    #link pra foto
    #print(dados['sprites']['front_shiny'])
    #retorna o html
    #url = retornaResponse('https://www.facebook.com/')
    #print(url)