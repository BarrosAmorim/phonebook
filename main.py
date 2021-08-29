def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        menuInput =  input('''
    ############################################
    |----------- AGENDA TELEFÔNICA ----------- |
    ############################################
    ____________________________________________
    |     ESCOLHA UMA OPÇÃO PARA INICIAR       |
    | => [1] CADASTRAR CONTATO                 |
    | => [2] LISTAR CONTATOS                   |  
    | => [3] BUSCAR CONTATO                    |
    | => [4] DELETAR CONTATO                   |
    | => [5] SAIR                              |
    |__________________________________________|
    ''')
        if menuInput == '1':
            cadastrarContato()
        elif menuInput == '2':
            listarContatos()
        elif menuInput == '3':
            buscarContato()
        elif menuInput == '4':
            deletarContato()
        elif menuInput == '5':
            sair() 
        else:
            print('Opção Inválida!')
        
        voltarMenu = input("Deseja voltar ao menu principal ? (s/n) ").lower()
   
def cadastrarContato(): # Função cadastrar um novo contato
    nome = input('Nome: ') # variaveis que vão armazenar dados informados pelo usuario
    phone = input('Telefone: ')
    email = input('E-mail: ')
    twitter = input('Twitter: ')
    facebook = input('Facebook: ')
    instagram = input('Instagram: ')
    try:
        agenda = open('agenda.csv', 'a') # criar arquivo csv em mode de escrita
        dados = f'Nome:{nome}, Telefone:{phone}, Email:{email}, Twitter:{twitter}, Facebook:{facebook}, Instagram:{instagram} \n' 
        agenda.write(dados) # Escreve os dados da agenda ao qual foram armazenados da variavel "dados"
        agenda.close()
        print('Contato cadastrado com sucesso!')
    except:
        print('Error')

def listarContatos(): # Função listar contatos
    agenda = open('agenda.csv', 'r') # abre o arquivo csv em modo leitura
    for contato in agenda: # percorre todos os elementos da da agenda
        print(contato)
    agenda.close()

def deletarContato():# Função deletar contatos
    nomeDeletado = input('Nome: ').lower() # . lower converte cada caractere maiústo em minúscula
    agenda = open("agenda.csv", 'r')
    aux = []
    aux2= []
    for i in agenda: # percorre todos os indices no array de contatos
        aux.append(i) # grava todos os indices e armazena na variavel i
    for i in range(0, len(aux)): # percorre cada nome e conta a quantidade de contatos na agenda
        if nomeDeletado not in aux[i].lower(): # verifica se os dados informados pelo usuario contem na variavel aux
            aux2.append(aux[i]) # caso o nome informado exista na agenda, armazena na variavel
    agenda = open('agenda.csv', 'w') # abre o o arquivo em modo de escrita
    for i in aux2: 
        agenda.write(i)
    print(f'Contato deletado com sucesso')
 
def buscarContato(): # Função buscar contatos
    nome=input(f'Insira nome: ').upper() # .upper converte todos os caracteres minúsculos em uma string em caracteres maiúsculos
    agenda = open('agenda.csv','r')
    for contato in agenda:
        if nome in contato.split(';')[0].upper(): # verifica se o nome informado esta na lista de contatos separando os com uma ,
            print(contato)
    agenda.close()

def sair(): # Funcão para sair do programa
    exit()

def main(): # Função que carrefa o menu dentro da funcao principal
    menu()
main()
