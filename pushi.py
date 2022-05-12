
from git import Repo



class processo_push():

    #é a função de inicio do programa, o 'self' é semelhante a um dicionário em python, armazena variáveis na própria classe
    def __init__(self, commit, caminho):
        print('\nInsira o commit: ')
        self._commit = commit
        print('\nInsira o caminho do repositorio: ')
        self._caminho_repositorio = caminho
        

    #Realiza o push
    def git_push(self):
        try:
            repo = Repo(self._caminho_repositorio)
            repo.git.add(update=True)
            repo.index.commit(self._commit)
            origin = repo.remote(name='origin')
            origin.push()
            print('\npush realizado com sucesso')  
        except:
            print('\nHouve algum erro durante a execução do push')  






   