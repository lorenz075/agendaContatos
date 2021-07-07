# Dictionary dos contatos
AGENDA = {}

# Método para mostrar todos os contatos da agenda


def mostrar_contatos():
    if(AGENDA):
        for contato in AGENDA:
            print()
            buscar_contatos(contato)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    else:
        print('>>>>Agenda vazia')

# Método que busca um contato em específico passado como paramêtro


def buscar_contatos(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
    except KeyError:
        print()
        print('>>>>CONTATO INEXISTENTE')
        print()
    except Exception as error:
        print('>>>>Um erro inesperado ocorreu')


# Método que inclui ou edita novos contatos na lista
def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print("===>>> {} adicionado/editado com sucesso!".format(contato))


# Método para excluir um contato passado como parâmetro
def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print("===>>> O usuário {} foi removido.".format(contato))
        print()
    except KeyError:
        print()
        print('>>>>CONTATO INEXISTENTE')
        print()
    except Exception as error:
        print('>>>>Um erro inesperado ocorreu')


def ler_detalhes_contato():
    telefone = input('Digite o telefone desejado: ')
    email = input('Digite o email desejado: ')
    endereco = input('Digite o endereço desejado: ')
    return telefone, email, endereco;


def exportar_contatos(file_name):
    try:
        with open(file_name, 'w') as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write("{}, {}, {}, {}\n".format(
                    contato, telefone, email, endereco))
        print('>>>>Agenda salva')
    except:
        print('>>>>Ocorreu algum erro ao exportar')


def importar_contatos(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                detalhes = line.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contatos(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('>>>>Arquivo não encontrado')
    except Exception as error:
        print('>>>>Erro inesperado')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def load():
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                detalhes = line.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    "telefone": telefone,
                    'email': email,
                    'endereco': endereco,
                }  
        print('>>>>Database carregado')
        print('>>>>{} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>>Arquivo não encontrado')
    except Exception as error:
        print('>>>>Erro inesperado')
        print(error)
        

# Imprime o menu de opcoes pro usuário
def imprimir_menu():
    print('++++++++++++++++++++++ MENU ++++++++++++++++++++++')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir/Editar contato')
    print('4 - Excluir contato')
    print('5 - Exportar contatos para CSV')
    print('6 - Importar contatos de CSV')
    print('0 - Sair do programa')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    

# Início do programa
load()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if(opcao == '1'):
        mostrar_contatos()

    elif(opcao == '2'):
        contato = input('Digite o nome do usuário a ser buscado:')
        print('')
        buscar_contatos(contato)
        print('')

    elif(opcao == '3'):
        contato = input('Digite o nome desejado: ')
        
        try:
            AGENDA[contato]
            print('>>>> Editando', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
        except KeyError:
            print('>>>>Incluindo contato', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
        

    elif(opcao == '4'):
        contato = input('Digite o usuário a ser excluído: ')
        excluir_contato(contato)
    
    elif(opcao == '5'):
        file_name = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(file_name)
        
    elif(opcao == '6'):
        file_name = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(file_name)
        
    elif(opcao == '0'):
        break
    else:
        print('Opção inválida')

