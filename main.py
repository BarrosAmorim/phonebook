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
   
def cadastrarContato():
    nome = input('Nome: ')
    phone = input('Telefone: ')
    email = input('E-mail: ')
    twitter = input('Twitter: ')
    facebook = input('Facebook: ')
    instagram = input('Instagram: ')
    try:
        agenda = open('agenda.csv', 'a')
        dados = f'Nome:{nome}, Telefone:{phone}, Email:{email}, Twitter:{twitter}, Facebook:{facebook}, Instagram:{instagram} \n' 
        agenda.write(dados)
        agenda.close()
        print('Contato cadastrado com sucesso!')
    except:
        print('Error')

def listarContatos():
    agenda = open('agenda.csv', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletado = input('Nome: ').lower()
    agenda = open("agenda.csv", 'r')
    aux = []
    aux2= []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.csv', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso')
 
def buscarContato():
    nome=input(f'Insira nome: ').upper()
    agenda = open('agenda.csv','r')
    for contato in agenda:
        if nome in contato.split(';')[0].upper():
            print(contato)
    agenda.close()

def sair():
    exit()

def main():
    menu()
main()
