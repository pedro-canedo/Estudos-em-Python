#BIBLIOTECA DE INTERFACE


def leiaInt(msg):
    while True:
        try:
            n = int(input((msg)))
        except (ValueError, TypeError):
            print('\n\033[31mUsuário preferiu não digitar um número inteiro. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar este número. \033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[33m - \033[34m{item}\033[31m')
        c += 1
    print(linha())
    opc = leiaInt('\033[37mSua Opção:\033[37m ')
    return opc


#BIBVLIOTECA DE ARQUIVOS


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso !')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
            a.close()


#PROGRAMA PRINCIPAL


from time import sleep

arq = 'menu.txt'
if arqExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado !')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas','Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\n\033[31mERRO ! (opção invalida tente novamente.\033[m')
        sleep(2)