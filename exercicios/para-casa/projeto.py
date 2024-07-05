# módulos
import print_reprograma as pr # está na pasta do meu projeto
from datetime import datetime # servirá para registro de horário das transações

# catálogo de produtos
produtos = [
    {'codigo': 1, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 1', 'valor': 150.00},
    {'codigo': 2, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 2', 'valor': 10.00},
    {'codigo': 3, 'nome': 'Linguagens de Programação Web para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 4, 'nome': 'Tecnologias de Scripting para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 5, 'nome': 'Desenvolvimento Web com SQL para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 6, 'nome': 'Desenvolvimento Web com C++ para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 7, 'nome': 'Desenvolvimento Web com Java para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 8, 'nome': 'Desenvolvimento Web com .Net para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 9, 'nome': 'Hardware e Redes de Computadores para Alunos Inteligentes - Volume 1', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Hardware e Redes de Computadores para Alunos Inteligentes - Volume 2', 'valor': 15.00},
    {'codigo': 11, 'nome': 'Hardware e Redes de Computadores para Alunos Inteligentes - Volume 3', 'valor': 15.00},
    {'codigo': 12, 'nome': 'Hardware e Redes de Computadores para Alunos Inteligentes - Volume 4', 'valor': 15.00},
    {'codigo': 13, 'nome': 'Dominando o Inglês para Alunos Inteligentes', 'valor': 5.00},
    {'codigo': 14, 'nome': 'Comunicação Empresarial para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 15, 'nome': 'Desenvolvimento Pessoal para Alunos Inteligentes - Livro 1', 'valor': 15.00},
    {'codigo': 16, 'nome': 'Desenvolvimento Pessoal para Alunos Inteligentes - Livro 2', 'valor': 15.00},
    {'codigo': 17, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 1', 'valor': 10.00},
    {'codigo': 18, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 2', 'valor': 10.00},
    {'codigo': 19, 'nome': 'Fundamentos da Programação para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 20, 'nome': 'Algoritmos e Estruturas de Dados para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 21, 'nome': 'Introdução à Engenharia de Software para Alunos Inteligentes', 'valor': 18.00},
    {'codigo': 22, 'nome': 'Banco de Dados para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 23, 'nome': 'Programação Web com Python para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Programação Web com JavaScript para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 25, 'nome': 'Introdução à Ciência da Computação para Alunos Inteligentes', 'valor': 18.00},
    {'codigo': 26, 'nome': 'Inteligência Artificial para Alunos Inteligentes', 'valor': 20.00},
    {'codigo': 27, 'nome': 'Redes de Computadores para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 28, 'nome': 'Segurança da Informação para Alunos Inteligentes', 'valor': 18.00},
    {'codigo': 29, 'nome': 'Administração de Sistemas para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 30, 'nome': 'Gestão de Projetos de TI para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 31, 'nome': 'Introdução à Estatística para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 32, 'nome': 'Probabilidade para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 33, 'nome': 'Matemática Discreta para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 34, 'nome': 'Cálculo para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 35, 'nome': 'Álgebra Linear para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 36, 'nome': 'Geometria Analítica para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 37, 'nome': 'Física para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 38, 'nome': 'Química para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 39, 'nome': 'Biologia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 40, 'nome': 'História para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 41, 'nome': 'Geografia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 42, 'nome': 'Sociologia para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 43, 'nome': 'Filosofia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 44, 'nome': 'Literatura Brasileira para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 45, 'nome': 'Literatura Portuguesa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 46, 'nome': 'Literatura Inglesa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 47, 'nome': 'Literatura Espanhola para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 48, 'nome': 'Literatura Francesa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 49, 'nome': 'Literatura Alemã para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Literatura Italiana para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 51, 'nome': 'Literatura Russa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 52, 'nome': 'Literatura Japonesa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 53, 'nome': 'Literatura Chinesa para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 54, 'nome': 'Arte para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 55, 'nome': 'Música para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 56, 'nome': 'Cinema para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 57, 'nome': 'Teatro para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 58, 'nome': 'Dança para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 59, 'nome': 'Fotografia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 60, 'nome': 'Direito para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 61, 'nome': 'Economia para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 62, 'nome': 'Administração para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 63, 'nome': 'Contabilidade para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 64, 'nome': 'Marketing para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 65, 'nome': 'Publicidade e Propaganda para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 66, 'nome': 'Recursos Humanos para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 67, 'nome': 'Relações Públicas para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 68, 'nome': 'Comunicação para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 69, 'nome': 'Jornalismo para Alunos Inteligentes', 'valor': 12.00},
    {'codigo': 70, 'nome': 'Psicologia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 71, 'nome': 'Sociologia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 72, 'nome': 'Antropologia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Ciência Política para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 74, 'nome': 'História da Arte para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 75, 'nome': 'História da Música para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 76, 'nome': 'História do Cinema para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 77, 'nome': 'História do Teatro para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 78, 'nome': 'História da Dança para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 79, 'nome': 'História da Fotografia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 80, 'nome': 'Filosofia da Arte para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 81, 'nome': 'Filosofia da Música para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 82, 'nome': 'Filosofia do Cinema para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 83, 'nome': 'Filosofia do Teatro para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 84, 'nome': 'Filosofia da Dança para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 85, 'nome': 'Filosofia da Fotografia para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 86, 'nome': 'Ética para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 87, 'nome': 'Ética Profissional para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 88, 'nome': 'Ética e Responsabilidade Social para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 89, 'nome': 'Lógica para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 90, 'nome': 'Pensamento Crítico para Alunos Inteligentes', 'valor': 10.00},
    {'codigo': 91, 'nome': 'Introdução ao Direito para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 92, 'nome': 'Direito Constitucional para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 93, 'nome': 'Direito Civil para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 94, 'nome': 'Direito Penal para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 95, 'nome': 'Direito Processual para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 96, 'nome': 'Direito do Trabalho para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 97, 'nome': 'Direito Tributário para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 98, 'nome': 'Direito Empresarial para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 99, 'nome': 'Direito Internacional para Alunos Inteligentes', 'valor': 15.00},
    {'codigo': 100, 'nome': 'Direito Ambiental para Alunos Inteligentes', 'valor': 15.00},
]

# função que buscará o código digitado no catálogo de produtos
def cod_produto(codigo): # recebe o código
    for produto in produtos: # produto está contido na lista de produtos
        if produto['codigo'] == codigo: # se o código digitado for igual ao código no catálogo
            return produto #retorne o produto correspondente
        
# função que imprimirá as informações do produto
def imprime_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|') # quantidade
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|') #valor unitário
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim') #valor total = valor unitário + quantidade   

# função que insere o produto na lista de compra do cliente
def item_compra(produto, quantidade):
    return { # retorna um novo dicionário
        'codigo':produto['codigo'], #'produto' chama um item do catálogo (ligada a função anterior)
        'nome':produto['nome'],
        'valor':produto['valor'],
        'quantidade':quantidade # será a quantidade digitada (1)
    }

# função que imprimirá os produtos da sua compra
def imprime_compra(compra):
    if(len(compra) > 0): # condicional que verifica se há itens na lista
        total = 0 # somatória iniciada em zero
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')   
        for produto in compra: # produto está contido dentro de compra (um cliente)
            imprime_produto(produto)
            total += produto['valor'] * produto['quantidade']
        pr.pular_linha()
        pr.separador(107,caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim')
    else: # se a lista de compras estiver vazia
        pr.imprimir('Sem itens na lista ainda', tamanho=80, alinhar='centro')
    pr.pular_linha()
    pr.pular_linha()

# função que encerra a compra do cliente (indica que todos os produtos já foram inseridos)
def imprime_compra_finalizada(compra, total): #irá mostrar os itens comprados e o valor total
    total_compra = 0 #início da variável (caixa inicia com 0 e os itens se somam)
    # estilo do cabeçalho da tabela
    pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
    pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')   
    for produto in compra: # produto está contido na lista de compras do cliente
        imprime_produto(produto)
        total_compra += produto['valor'] * produto['quantidade']
        if total_compra > 100: #desconto1
            desconto = total_compra * 0.1
            total_com_desconto = total_compra - desconto
    pr.pular_linha()
    pr.separador(107,caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    if total_compra > 100: #desconto1 - impressão
        pr.imprimir('Desconto de 10%', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(desconto, 2)), tamanho=12, alinhar='fim',cor_texto='amarelo')
        pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total_com_desconto, 2)), tamanho=12, alinhar='fim',cor_texto='verde negrito')
    else: #desconto2 - impressão ou sem desconto
        pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total_compra, 2)), tamanho=12, alinhar='fim',cor_texto='verde negrito')
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

def calcula_total_desconto(compra):
    total = 0 #início da função
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])
        if total > 100 and compra.count(produto) > 1: #aplica desconto de 10% e 50% nos itens repetidos
            total = total - (total * 0.1)
            produto['valor'] *= 0.5
            total == total
        elif total > 100:
            total = total - (total * 0.1)
        elif compra.count(produto) > 1:
            produto['valor'] *= 0.5
            total == total
    return total

# função para imprimir o fechamento de todas as compras do caixa do dia
def imprime_fechamento_caixa(compras):
    # estilo do cabeçalho
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')  
    total = 0 #início em zero para somatória
    for compra in compras: # cada compra realizada está contida em compras do fechamento
        total += compra['total'] # soma todas as compras
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.pular_linha()
    pr.separador(80,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')

# função para imprimir o cabeçalho da tela inicial
def imprime_cabeçalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
    pr.separador(120,cor_texto='ciano')
    if(erro != ''):
        pr.imprimir(erro,tamanho=80,alinhar='centro',cor_texto='vermelho negrito')
        pr.separador(120,cor_texto='ciano')
        pr.pular_linha()
    erro = ''

# função para iimprimir o rodapé da tela inicial
def imprime_rodape():
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=115,alinhar='fim',end='>> ')
    return input().lower() #lê a inserção do usuário e converte para letras minusculas

# função que imprime o menu de ajuda/auxiliar do programa
def imprime_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=80)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=80)
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=80)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=80)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=80)
    pr.imprimir('[nnn] >> Adicionar o código do produto a compra',alinhar='centro',tamanho=80)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=80)
    pr.imprimir('[E]   >> Encerrar caixa',alinhar='centro',tamanho=80)
    pr.pular_linha(quantidade=2)

# função para interação do usuárío com o menu do programa
def menu():
    #variáveis
    opcao = '' #string
    erro = '' #string
    tela = '' #string
    compra = [] # lista
    compras = [] # lista
    # loop do menu
    while(opcao != 'q'): # rodar enquanto o usuário não optar por sair (q)
        imprime_cabeçalho(erro) # mostrar cabeçalho inicial
        if(tela == ''): # se não for inserido nada, pula 4 linhas
            pr.pular_linha(quantidade=4)
        elif(tela == 'ajuda'): # se for optado por ajuda, trará a função imprime_ajuda
            imprime_ajuda()
            tela=''
        elif(tela == 'compra'): # se for inserido uma lista de compra, trará a função imprime_compra
            imprime_compra(compra)    
        elif(tela == 'fechar'): # se a compra for finalizada, trará a função imprime_compra_finalizada
            imprime_compra_finalizada(compra,total)
        elif(tela == 'encerrar'): # se o caixa for encerrado do dia, trará a função imprime_fechamento_caixa 
            imprime_fechamento_caixa(compras)
            compras = []
            tela=''
            pr.pular_linha(quantidade=2)
    # lê a inserção do usuário
        opcao = imprime_rodape()
        if(opcao == 'h'): #se a opção selecionada for 'h', retorna no loop acima e busca a função definida para atender o menu
            tela='ajuda'
        elif(opcao == 'n'): #se a opção selecionada for 'n', retorna no loop acima e busca a função definida para atender o menu
            tela='compra'
        elif(opcao == 'f'): #se a opção selecionada for 'f', retorna no loop acima e busca a função definida para atender o menu
            total = calcula_total_desconto(compra) # calcula o desconto final
            tela = 'fechar'
        elif(opcao == 'e'): #se a opção selecionada for 'e', retorna no loop acima e busca a função definida para atender o menu
            tela = 'encerrar'
        elif('p' in opcao): #se a opção selecionada for 'p', encerra a compra
            compras.append({'itens':compra, 'total':total, 'data': datetime.now()})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = cod_produto(codigo)
                compra.append(item_compra(produto,1))
            except (ValueError, TypeError):
                erro = 'A opção selecionada não existe no sistema'
                continue

menu()