
import pyodbc 

#Função para salvar na base de dados
def salvar(usuario, repositorio):
    
    #Realizo a conexão
    cnxn = pyodbc.connect('Conexao com o Banco')
    #crio um cursor com a variavel da conexão, é uma ferramenta para voce utilizar
    #tipo, voce tem o caminho ali em cima, ele ta "salvo n ferramenta". Agora é só voce usar a ferramenta como quiser
    cursor = cnxn.cursor()
       
    #Apenas um teste de conexão
    #{
    #Sample select query
    #cursor.execute("SELECT @@VERSION") 
    #}
    
   #uma outra forma de fazer é armazenar os valores em variáveis e usá-las como no exemplo abaixo
    #sql = 'INSERT INTO ex1 (usuario, repositorio) VALUES ($s, %s)'
    #val = (usuario, repositorio)

    #Passo o comendo SQL e em sequência as variáveis contendo os valores que serão armazenados
    cursor.execute('''INSERT INTO ex1 (usuario, repositorio) VALUES (?, ?)''',usuario,repositorio)

    #no comentário abaixo tem outra forma de fazer, porém ela é menos segura, pois é vulnerável a SQL Inject
   # cursor.execute(f'''INSERT INTO ex1 VALUES ({usuario}, {repositorio})''')

   #Ao final de todo comamndo execute, é necessário ter um commit
    cnxn.commit()
    
    print('A lista foi salva!')



