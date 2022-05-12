import requests
import json
import salvarbd

class listaDeRepositorios():

    #é a função de inicio do programa, o 'self' é semelhante a um dicionário em python, armazena variáveis na própria classe
    def __init__(self,usuario):
        self._usuario = usuario

    #realiza a requisição
    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    
    #imprime a lista de repositórios
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()

        #se a função acima não retornar um erro (Status code), ele entrará nesse IF (ou seja, a variável estará com uma lista)        
        if type(dados_api) is not int:

            #verifico se o usuario quer salvar os repositórios
            print('Para salvar no banco de dados, digite "y", senão digite qualquer outro valor.')
            resposta = input()
           
           #um laço que será executado até percorrer toda a lista que foi retornada
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
                if resposta == 'y':        
                    #salvo cada repositório no banco de dados    
                    salvarbd.salvar(self._usuario,dados_api[i]['name']) 
                
        else:
            print(dados_api)


#self.usuario = usuario
#dados_api = repositorios