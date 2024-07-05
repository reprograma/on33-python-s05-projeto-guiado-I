import print_reprograma as pr
from datetime import datetime

produtos = [
    {'codigo': 1, 'nome': 'Introdução à Computação - Volume 1', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 2, 'nome': 'Introdução à Computação - Volume 2', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 3, 'nome': 'Linguagens de Programação Web', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 4, 'nome': 'Tecnologias de Scripting', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 5, 'nome': 'Desenvolvimento Web com SQL', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 6, 'nome': 'Desenvolvimento Web com C++', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 7, 'nome': 'Desenvolvimento Web com Java', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 8, 'nome': 'Desenvolvimento Web com .Net', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 9, 'nome': 'Hardware e Redes de Computadores - Volume 1', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Hardware e Redes de Computadores - Volume 2', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 11, 'nome': 'Hardware e Redes de Computadores - Volume 3', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 12, 'nome': 'Hardware e Redes de Computadores - Volume 4', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 13, 'nome': 'Dominando o Inglês', 'tipo': 'comunicação', 'valor': 5.00},
    {'codigo': 14, 'nome': 'Comunicação Empresarial', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 15, 'nome': 'Desenvolvimento Pessoal - Livro 1', 'tipo': 'auto-ajuda', 'valor': 15.00},
    {'codigo': 16, 'nome': 'Desenvolvimento Pessoal - Livro 2', 'tipo': 'auto-ajuda', 'valor': 15.00},
    {'codigo': 17, 'nome': 'Introdução à Computação - Volume 1', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 18, 'nome': 'Introdução à Computação - Volume 2', 'tipo': 'ti', 'valor': 10.00},
    {'codigo': 19, 'nome': 'Fundamentos da Programação', 'tipo': 'ti', 'valor': 12.00},
    {'codigo': 20, 'nome': 'Algoritmos e Estruturas de Dados',  'tipo': 'ti','valor': 15.00},
    {'codigo': 21, 'nome': 'Introdução à Engenharia de Software','tipo': 'ti', 'valor': 18.00},
    {'codigo': 22, 'nome': 'Banco de Dados', 'tipo': 'ti', 'valor': 12.00},
    {'codigo': 23, 'nome': 'Programação Web com Python', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Programação Web com JavaScript', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 25, 'nome': 'Introdução à Ciência da Computação', 'tipo': 'ti', 'valor': 18.00},
    {'codigo': 26, 'nome': 'Inteligência Artificial', 'tipo': 'ti', 'valor': 20.00},
    {'codigo': 27, 'nome': 'Redes de Computadores', 'tipo': 'ti', 'valor': 15.00},
    {'codigo': 28, 'nome': 'Segurança da Informação', 'tipo': 'ti', 'valor': 18.00},
    {'codigo': 29, 'nome': 'Administração de Sistemas', 'tipo': 'gestão', 'valor': 15.00},
    {'codigo': 30, 'nome': 'Gestão de Projetos de TI', 'tipo': 'gestão', 'valor': 12.00},
    {'codigo': 31, 'nome': 'Introdução à Estatística', 'tipo': 'ciências exatas', 'valor': 10.00},
    {'codigo': 32, 'nome': 'Probabilidade', 'tipo': 'ciências exatas', 'valor': 10.00},
    {'codigo': 33, 'nome': 'Matemática Discreta', 'tipo': 'ciências exatas', 'valor': 12.00},
    {'codigo': 34, 'nome': 'Cálculo', 'tipo': 'ciências exatas', 'valor': 15.00},
    {'codigo': 35, 'nome': 'Álgebra Linear', 'tipo': 'ciências exatas', 'valor': 12.00},
    {'codigo': 36, 'nome': 'Geometria Analítica', 'tipo': 'ciências exatas', 'valor': 10.00},
    {'codigo': 37, 'nome': 'Física', 'tipo': 'ciências exatas', 'valor': 15.00},
    {'codigo': 38, 'nome': 'Química', 'tipo': 'ciências exatas', 'valor': 12.00},
    {'codigo': 39, 'nome': 'Biologia', 'tipo': 'ciências exatas', 'valor': 10.00},
    {'codigo': 40, 'nome': 'História', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 41, 'nome': 'Geografia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 42, 'nome': 'Sociologia', 'tipo': 'ciências humanas', 'valor': 12.00},
    {'codigo': 43, 'nome': 'Filosofia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 44, 'nome': 'Literatura Brasileira', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 45, 'nome': 'Literatura Portuguesa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 46, 'nome': 'Literatura Inglesa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 47, 'nome': 'Literatura Espanhola', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 48, 'nome': 'Literatura Francesa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 49, 'nome': 'Literatura Alemã', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Literatura Italiana', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 51, 'nome': 'Literatura Russa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 52, 'nome': 'Literatura Japonesa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 53, 'nome': 'Literatura Chinesa', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 54, 'nome': 'Arte', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 55, 'nome': 'Música', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 56, 'nome': 'Cinema', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 57, 'nome': 'Teatro', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 58, 'nome': 'Dança', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 59, 'nome': 'Fotografia', 'tipo': 'artes', 'valor': 10.00},
    {'codigo': 60, 'nome': 'Direito', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 61, 'nome': 'Economia', 'tipo': 'ciências exatas', 'valor': 12.00},
    {'codigo': 62, 'nome': 'Administração', 'tipo': 'gestão', 'valor': 10.00},
    {'codigo': 63, 'nome': 'Contabilidade', 'tipo': 'gestão', 'valor': 12.00},
    {'codigo': 64, 'nome': 'Marketing', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 65, 'nome': 'Publicidade e Propaganda', 'comunicação': 'ti', 'valor': 10.00},
    {'codigo': 66, 'nome': 'Recursos Humanos', 'tipo': 'gestão', 'valor': 10.00},
    {'codigo': 67, 'nome': 'Relações Públicas', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 68, 'nome': 'Comunicação', 'tipo': 'comunicação', 'valor': 10.00},
    {'codigo': 69, 'nome': 'Jornalismo', 'tipo': 'comunicação', 'valor': 12.00},
    {'codigo': 70, 'nome': 'Psicologia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 71, 'nome': 'Sociologia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 72, 'nome': 'Antropologia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Ciência Política', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 74, 'nome': 'História da Arte', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 75, 'nome': 'História da Música', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 76, 'nome': 'História do Cinema', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 77, 'nome': 'História do Teatro', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 78, 'nome': 'História da Dança', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 79, 'nome': 'História da Fotografia', 'tipo': 'ciências humanas','valor': 10.00},
    {'codigo': 80, 'nome': 'Filosofia da Arte', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 81, 'nome': 'Filosofia da Música', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 82, 'nome': 'Filosofia do Cinema', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 83, 'nome': 'Filosofia do Teatro', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 84, 'nome': 'Filosofia da Dança', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 85, 'nome': 'Filosofia da Fotografia', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 86, 'nome': 'Ética', 'tipo': 'ciências humanas','valor': 10.00},
    {'codigo': 87, 'nome': 'Ética Profissional', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 88, 'nome': 'Ética e Responsabilidade Social', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 89, 'nome': 'Lógica para Alunos', 'tipo': 'ciências exatas', 'valor': 10.00},
    {'codigo': 90, 'nome': 'Pensamento Crítico', 'tipo': 'ciências humanas', 'valor': 10.00},
    {'codigo': 91, 'nome': 'Introdução ao Direito', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 92, 'nome': 'Direito Constitucional', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 93, 'nome': 'Direito Civil', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 94, 'nome': 'Direito Penal', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 95, 'nome': 'Direito Processual', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 96, 'nome': 'Direito do Trabalho', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 97, 'nome': 'Direito Tributário', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 98, 'nome': 'Direito Empresarial', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 99, 'nome': 'Direito Internacional', 'tipo': 'ciências humanas', 'valor': 15.00},
    {'codigo': 100, 'nome': 'Direito Ambiental', 'tipo': 'ciências humanas', 'valor': 15.00},
]

#função que serve para pegar qualquer numero inteiro digitado no terminal de 1 - 100 
#usá-lo como input para procurar o produto pelo seu código.
def produto_codigo(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto

#pelo que entendi essa função existe para guardar a quantidade de itens que compramos, 
#num dicionário
def novo_produto(produto, quantidade):
    return {
                'codigo': produto['codigo'],
                'nome': produto['nome'],
                'valor': produto['valor'],
                'quantidade': quantidade
            }

#esta função imprime as compras fechadas e a soma de todas essas compras
# quando o caixa estiver fechado com a opção 'e'
def imprime_fechamento_caixa(compras):
    #essas três linhas seguintes servem para imprimir o cabeçalho do que vai
    #ser impresso na função
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')  
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')  
    pr.imprimir('valor', tamanho=20, alinhar='centro')
    total = 0
    total_desconto = 0 #inicializando com 0
    for compra in compras:#pelo que entendi compra e compras são variaveis a serem declaradas
        #mais abaixo na função menu
        total += compra['total'] #o que significa aqui esse 'total' em colchetes?
        total_desconto += compra['desconto'] # acumular o desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim')
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')# o que significca aqui esse 'itens' em colchetes? de onde isso saiu?
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')
    pr.separador(120, caracter='-')  
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|') 
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')

    #imprime total de desconto
    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')

#esta função imprime o total da compra quando damos o comando 'f' no terminal
def imprime_compra_fechada(compra, total, desconto):
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')  
    pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')  
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')  
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')  
    pr.imprimir('valor', tamanho=12, alinhar='centro')
    for produto in compra:
        imprimir_produto(produto)  # chamou uma função dentro de uma função!
        total_compra += produto['valor'] * produto['quantidade']
        # esta linha faz com que esta variável armazene o total da compra
    
    pr.separador(120, caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    #imprimir valor do desconto
    if desconto > 0:
        pr.imprimir('Desconto aplicado', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('- R$', str(round(desconto, 2)), tamanho=12, alinhar='fim', cor_texto='vermelho negrito')
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito')  
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

#esta função imprime a compra, os produtos que vamos adiconando as compras sempre que 
#digitamos um código no terminal
def imprime_compra(compra):
    if len(compra) > 0: #se uma compra for registrada no terminal
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
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')  # Imprimimos a mensagem de lista vazia
    pr.pular_linha()
    pr.pular_linha()

#esta função imprime os produtos linha após linha e é usada em outras funções acima
#como 'imprime_compra' e 'imprime_compra_fechada'
def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|') 
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|') 
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

def imprimir_cabecalho(erro): #porque o parametro e (abaixo) variável 'erro' é chamada aqui?
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado\nTerminal de Vendas', sv = 1, tamanho = 100, cor_texto = 'azul negrito', cor_barra = 'magenta')
    pr.separador(100, cor_texto = 'ciano')
    if(erro != ''):
        pr.imprimir(erro, tamanho = 120, alinhar = 'centro', cor_texto = 'vermelho negrito') 
        pr.separador(100, cor_texto = 'ciano')
    erro = ''

def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=100)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=100)
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=100)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=100)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=100)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=100)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=100)
    pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=100)
    pr.pular_linha(quantidade=2)

def imprimir_rodape():
    pr.imprimir('[H] Ajuda', '[Q] Sair', caracter = '=', tamanho = 98, alinhar = 'fim', end = '✨\n')

    return input().lower()

#função principal, seria o corpo do programa, só não entendi porque precisa ser
#transformado em função
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
            tela = '' #faz retornar à tela inicial
        elif tela == 'compra':
            imprime_compra(compra)#imprime a lista de produtos atual
        elif tela == 'fechar':
            total, desconto = calcula_total_desconto(compra)
            imprime_compra_fechada(compra, total, desconto)
        elif tela == 'encerrar':
            imprime_fechamento_caixa(compras)
            compras = [] #forma para atribuir a variavel compras um valor de 0, 
            #retornando-a a sua versão original acima
            tela = ''
            pr.pular_linha(quantidade=2)
        opcao = imprimir_rodape() # para ler a impressão do usuário
        if opcao == 'h':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'#não entendo como isso consegue ativar uma tela de nova compra?
        elif opcao == 'f':
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif opcao == 'e':
            tela = 'encerrar'
        elif opcao == 'p':
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
        desconto = total * 0.1
        total *= 0.9
    else:#verificar desconto para combos
        for codigo in set([item['codigo'] for item in compra]):
                    quantidade_codigo = sum([item['quantidade'] for item in compra if item ['codigo']])
                    # sum = soma
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
            total -= desconto
    return total, desconto

def remover_item(compra, codigo):
    #remove o item da lista de compras
    compra[:] = [item for item in compra if item['codigo']!= codigo]
    return compra

menu()
