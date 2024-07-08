import print_reprograma as pr
from datetime import datetime

produtos = [
    {'codigo': 1, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 1', 'valor': 10.00},
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

def get_cor():
    print(cor_texto)

def branco():
    cor_texto = 'branco'
    print('\033[30m', end='')
 
def vermelho():
    cor_texto = 'vermelho'
    print('\033[31m', end='')
 
def verde():
    cor_texto = 'verde'
    print('\033[32m', end='')
 
def amarelo():
    cor_texto = 'amarelo'
    print('\033[33m', end='')
 
def azul():
    cor_texto = 'azul'
    print('\033[34m', end='')

def magenta():
    cor_texto = 'magenta'
    print('\033[35m', end='')

def ciano():
    cor_texto = 'ciano'
    print('\033[36m', end='')

def cinza():
    cor_texto = 'cinza'
    print('\033[37m', end='')

def negrito():
    print('\033[1m', end='')

def branco_negrito():
    print('\033[1;30m', end='')
 
def vermelho_negrito():
    print('\033[1;31m', end='')
 
def verde_negrito():
    print('\033[1;32m', end='')
 
def amarelo_negrito():
    print('\033[1;33m', end='')
 
def azul_negrito():
    print('\033[1;34m', end='')

def magenta_negrito():
    print('\033[1;35m', end='')

def ciano_negrito():
    print('\033[1;36m', end='')

def cinza_negrito():
    print('\033[1;37m', end='')

def cor(cor):
    if(cor == 'branco'):
        branco()
    elif(cor == 'vermelho'):
        vermelho()
    elif(cor == 'verde'):
        verde()
    elif(cor == 'amarelo'):
        amarelo()
    elif(cor == 'azul'):
        azul()
    elif(cor == 'magenta'):
        magenta()
    elif(cor == 'ciano'):
        ciano()
    elif(cor == 'cinza'):
        cinza()
    elif(cor == 'w'):
        branco()
    elif(cor == 'r'):
        vermelho()
    elif(cor == 'g'):
        verde()
    elif(cor == 'y'):
        amarelo()
    elif(cor == 'b'):
        azul()
    elif(cor == 'm'):
        magenta()
    elif(cor == 'c'):
        ciano()
    elif(cor == 'gr'):
        cinza()
    elif(cor == 'branco negrito'):
        branco_negrito()
    elif(cor == 'vermelho negrito'):
        vermelho_negrito()
    elif(cor == 'verde negrito'):
        verde_negrito()
    elif(cor == 'amarelo negrito'):
        amarelo_negrito()
    elif(cor == 'azul negrito'):
        azul_negrito()
    elif(cor == 'magenta negrito'):
        magenta_negrito()
    elif(cor == 'ciano negrito'):
        ciano_negrito()
    elif(cor == 'cinza negrito'):
        cinza_negrito()
    elif(cor == 'wb'):
        branco_negrito()
    elif(cor == 'rb'):
        vermelho_negrito()
    elif(cor == 'gb'):
        verde_negrito()
    elif(cor == 'yb'):
        amarelo_negrito()
    elif(cor == 'bb'):
        azul_negrito()
    elif(cor == 'mb'):
        magenta_negrito()
    elif(cor == 'cb'):
        ciano_negrito()
    elif(cor == 'grb'):
        cinza_negrito()
    elif(cor == 'negrito'):
        negrito()

def imprimir(*textos, sep=' ',end='\n', caracter = ' ', tamanho=0, alinhar='comeco', cor_texto=''):
    cor(cor_texto)
    tamanho_total = 0
    for texto in textos:
        tamanho_total += len(texto)
    tamanho_total += (len(textos)-1) * len(sep)
    
    espaco_ini = 0
    espaco_fim = 0

    if(alinhar == 'fim'):
        espaco_ini = tamanho - tamanho_total
        espaco_fim = 0
    elif(alinhar == 'centro'):
        espaco_ini = (tamanho - tamanho_total)//2
        espaco_fim = (tamanho - tamanho_total)//2
        if((tamanho - tamanho_total) % 2 > 0):
            espaco_fim += 1
    else:
        espaco_ini = 0
        espaco_fim = tamanho - tamanho_total

    if(espaco_ini < 0):
        espaco_ini = 0

    if(espaco_fim < 0):
        espaco_fim = 0

    for i in range(espaco_ini):
        print(caracter, end='')

    for i in range(len(textos)):
        temp_sep = sep
        if(i == len(textos) - 1):
            temp_sep = ''
        else:
            tamanho_total += 1
        print(textos[i], end = temp_sep)
    
    for i in range(espaco_fim):
        print(caracter, end='')

    print(end, end='')

    limpar_formatacao()

def separador(tamanho,caracter = '═', cor_texto=''):
    cor(cor_texto)
    for i in range(tamanho):
        print(caracter,end='')
    print('\n')
    limpar_formatacao()

def retangulo(texto,sv=0,sh=0,tamanho=0,cor_barra = '', cor_texto = '',margem=0):
    linhas = texto.split('\n')
    max_len = 0
    for linha in linhas:
        if(max_len < len(linha)):
            max_len = len(linha)
    ajuste = False
    if(tamanho>0):
        sh = (tamanho - max_len - 2) // 2
        if(sh < 0):
            sh = 0
        else:
            ajuste = (tamanho - max_len - 2) % 2 > 0
    cor(cor_barra)
    sh_texto_ini = ''
    sh_barra_ini = ''
    sh_texto_fim = ''
    sh_barra_fim = ''
    for i in range(sh):
        sh_texto_ini += ' '
        sh_barra_ini += '═'
        sh_texto_fim += ' '
        sh_barra_fim += '═'
    if(ajuste):
        sh_texto_fim += ' '
        sh_barra_fim += '═'
    texto_branco = ''
    texto_barra = ''
    margem_texto = ''
    for i in range(margem):
        margem_texto += ' '
    for i in range(max_len):
        texto_barra+= '═' 
        texto_branco += ' '
    print(margem_texto,'╔',sh_barra_ini,texto_barra,sh_barra_fim,'╗',sep='')
    for i in range(sv):
        print(margem_texto,'║',sh_texto_ini,texto_branco,sh_texto_fim,'║',sep='')
    
    for linha in linhas:
        cor(cor_barra)
        print(margem_texto,'║',end='',sep='')
        cor(cor_texto)
        for i in range((max_len - len(linha))//2):
            print(' ',end='')
        print(sh_texto_ini,linha,sh_texto_fim,sep='',end='')
        for i in range((max_len - len(linha))//2):
            print(' ',end='')
        if((max_len - len(linha))%2 > 0):
            print(' ',end='')
        cor(cor_barra)
        print('║')

    for i in range(sv):
        print(margem_texto,'║',sh_texto_ini,texto_branco,sh_texto_fim,'║',sep='')

    print(margem_texto,'╚',sh_barra_ini,texto_barra,sh_barra_fim,'╝',sep='')
    limpar_formatacao()

def pular_linha(quantidade = 1):
    for i in range(quantidade):
        print('')

def limpar():
    print(chr(27) + "[2J")

def limpar_formatacao():
    print('\033[m', end='')
    
def produto_codigo(codigo): 
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto

def novo_produto(produto, quantidade):
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
    }

def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')
    total = 0
    total_desconto = 0
    for compra in compras:
        total += compra['total']
        total_desconto += compra['desconto']
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim')
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')
    pr.separador(120, caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')


    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')

def imprime_compra_fechada(compra, total, desconto):
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')
    pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')
    for produto in compra:
        imprimir_produto(produto)
        total_compra += produto['valor'] * produto['quantidade']
    pr.separador(120, caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim')


    if desconto > 0:
        pr.imprimir('Desconto aplicado', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('- R$', str(round(desconto, 2)), tamanho=12, alinhar='fim', cor_texto='vermelho negrito')

    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito') 

    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

def imprime_compra(compra):
    if len(compra) > 0:
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')
        for produto in compra:
            imprimir_produto(produto)
            total += produto['valor'] * produto['quantidade']
        pr.separador(120, caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim')
    else:
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')
    pr.pular_linha()
    pr.pular_linha()

def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=100, margem=10, cor_texto='azul negrito', cor_barra='magenta')
    pr.separador(120, cor_texto='ciano')
    if erro != '':
        pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(120, cor_texto='ciano')
    erro = ''

def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema', alinhar='centro', tamanho=120)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema', alinhar='centro', tamanho=120)
    pr.imprimir('[N]   >> Cria uma Nova Compra', alinhar='centro', tamanho=120)
    pr.imprimir('[F]   >> Fechar a Compra', alinhar='centro', tamanho=120)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga', alinhar='centro', tamanho=120)
    pr.imprimir('[AC] >> Adicionar o codigo do produto a compra', alinhar='centro', tamanho=120)
    pr.imprimir('[MQ] >> Muda a quantidade de itens adicionado', alinhar='centro', tamanho=120)
    pr.imprimir('[EX]   >> Encerar caixa', alinhar='centro', tamanho=120)
    pr.pular_linha(quantidade=2)

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=80, alinhar='fim', end='╣')
    return input().lower()

def menu():
    opcao = ''
    erro = ''
    tela = ''
    compra = []
    compras = []
    while opcao != 'q':
        imprimir_cabecalho(erro)
        if tela == '':
            pr.pular_linha(quantidade=4)
        elif tela == 'ajuda':
            imprimir_ajuda()
            tela = ''
        elif tela == 'compra':
            imprime_compra(compra)
        elif tela == 'fechar':
            total, desconto = calcula_total_desconto(compra)
            imprime_compra_fechada(compra, total, desconto)
        elif tela == 'encerar':
            imprime_fechamento_caixa(compras)
            compras = []
            tela = ''
            pr.pular_linha(quantidade=2)
        opcao = imprimir_rodape()
        if opcao == 'h':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'
        elif opcao == 'f':
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif opcao == 'e':
            tela = 'encerar'
        elif 'p' in opcao:
            compras.append({'itens': compra, 'total': total, 'data': datetime.now(), 'desconto': desconto})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                compra.append(novo_produto(produto, 1))
            except ValueError:
                erro = 'A opção selecionada não existe no sistema'
            except TypeError:
                erro = 'O código do produto não existe'

def calcula_total_desconto(compra):
    total = 0
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])

    desconto = 0

    if total >= 100:
        desconto = total * 0.5
        total *= 0.8
    else:
        for codigo in set([item['codigo']for item in compra]):
           quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo]) 
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5

    return total, desconto

def remover_item(compra, codigo):
    compra[:] = [item for item in compra if item[codigo] != codigo]
    return compra

def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=120)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=120)
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=120)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=120)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=120)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=120)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=120)
    pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=120)
    pr.pular_linha(quantidade=2)

    #imprimir rodapé
def imprimir_rodape():
    pr.imprimir("[H] Ajuda", "[Q] Sair ", caracter="=", tamanho=120, alinhar="fim", end="╣")

    return input().lower() # lower converte a string para letras minúsculas


def calcular_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    preco_com_desconto = preco - valor_desconto
    return preco_com_desconto

livros = {
    "Direito Ambiental para Alunos Inteligentes": 15.00,
    "Direito Tributário para Alunos Inteligentes": 15.00,
    "Direito do Trabalho para Alunos Inteligentes": 15.00,
    "Ética para Alunos Inteligentes": 10.00,
    "História da Arte para Alunos Inteligentes": 10.00,



}

print("Bem-vindo à nossa loja de livros!")
print("Livros disponíveis:")

for livro, preco in livros.items():
    print(f"{livro}: R${preco:.2f}")

livro_escolhido = input("Digite o nome do livro que deseja comprar: ")
desconto = float(input("Digite o desconto em porcentagem: "))

if livro_escolhido in livros:
    preco_livro = livros[livro_escolhido]
    preco_final = calcular_desconto(preco_livro, desconto)
    print(f"Preço final com desconto: R${preco_final:.2f}")
else:
    print("Livro não encontrado na lista.")

menu ()



