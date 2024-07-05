import print_reprograma as pr
from datetime import datetime

produtos = [
    {"codigo": 1, "nome": "Rosa Vermelha", "valor": 15.00},
    {"codigo": 2, "nome": "Orquídea Branca", "valor": 30.00},
    {"codigo": 3, "nome": "Girassol", "valor": 10.00},
    {"codigo": 4, "nome": "Lírio", "valor": 20.00},
    {"codigo": 5, "nome": "Tulipa Vermelha", "valor": 25.00},
    {"codigo": 6, "nome": "Margarida", "valor": 5.00},
    {"codigo": 7, "nome": "Lavanda", "valor": 15.00},
    {"codigo": 8, "nome": "Hortênsia", "valor": 18.00},
    {"codigo": 9, "nome": "Cravo", "valor": 8.00},
    {"codigo": 10, "nome": "Violeta", "valor": 7.00},
    {"codigo": 11, "nome": "Jasmim", "valor": 12.00},
    {"codigo": 12, "nome": "Camélia", "valor": 22.00},
    {"codigo": 13, "nome": "Azaleia", "valor": 14.00},
    {"codigo": 14, "nome": "Begônia", "valor": 16.00},
    {"codigo": 15, "nome": "Bromélia", "valor": 20.00},
    {"codigo": 16, "nome": "Girassol Mini", "valor": 8.00},
    {"codigo": 17, "nome": "Peônia", "valor": 30.00},
    {"codigo": 18, "nome": "Gardênia", "valor": 25.00},
    {"codigo": 19, "nome": "Petúnia", "valor": 10.00},
    {"codigo": 20, "nome": "Amor-perfeito", "valor": 6.00},
    {"codigo": 21, "nome": "Antúrio", "valor": 28.00},
    {"codigo": 22, "nome": "Dália", "valor": 12.00},
    {"codigo": 23, "nome": "Lisianto", "valor": 15.00},
    {"codigo": 24, "nome": "Azaleia Rosa", "valor": 18.00},
    {"codigo": 25, "nome": "Cravina", "valor": 7.00},
    {"codigo": 26, "nome": "Verônica", "valor": 9.00},
    {"codigo": 27, "nome": "Flor-de-maio", "valor": 15.00},
    {"codigo": 28, "nome": "Flor-de-lis", "valor": 20.00},
    {"codigo": 29, "nome": "Boca-de-leão", "valor": 10.00},
    {"codigo": 30, "nome": "Astromélia", "valor": 12.00},
    {"codigo": 31, "nome": "Flor-do-campo", "valor": 5.00},
    {"codigo": 32, "nome": "Camomila", "valor": 7.00},
    {"codigo": 33, "nome": "Flor-de-lótus", "valor": 25.00},
    {"codigo": 34, "nome": "Hemerocale", "valor": 20.00},
    {"codigo": 35, "nome": "Agerato", "valor": 8.00},
    {"codigo": 36, "nome": "Lisianthus", "valor": 15.00},
    {"codigo": 37, "nome": "Sempre-viva", "valor": 10.00},
    {"codigo": 38, "nome": "Flor-de-cera", "valor": 12.00},
    {"codigo": 39, "nome": "Gérbera", "valor": 8.00},
    {"codigo": 40, "nome": "Hortelã", "valor": 5.00},
    {"codigo": 41, "nome": "Maranta", "valor": 10.00},
    {"codigo": 42, "nome": "Echeveria", "valor": 12.00},
    {"codigo": 43, "nome": "Suculenta", "valor": 7.00},
    {"codigo": 44, "nome": "Flor-de-pessegueiro", "valor": 20.00},
    {"codigo": 45, "nome": "Flor-de-cerejeira", "valor": 22.00},
    {"codigo": 46, "nome": "Hibisco", "valor": 18.00},
    {"codigo": 47, "nome": "Alecrim", "valor": 5.00},
    {"codigo": 48, "nome": "Flor-de-laranjeira", "valor": 15.00},
    {"codigo": 49, "nome": "Palmarosa", "valor": 12.00},
    {"codigo": 50, "nome": "Manjericão", "valor": 6.00},
]


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
    total_desconto = 0 #inicializando com 0
    for compra in compras:
        total += compra['total']
        total_desconto += compra['desconto'] #acumular o desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim')
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')
    pr.separador(120, caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')

    #imprime total de desconto
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
    
    #imprimir o valor do desconto
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
    pr.retangulo('{Reflora}\nFloricultura e jardinagem\nTerminal de Vendas', sv=1, tamanho=80, margem=0, cor_texto='branco negrito', cor_barra='verde')
    pr.separador(80, cor_texto='ciano')
    if erro != '':
        pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(120, cor_texto='ciano')
    erro = ''

def imprimir_ajuda():
    pr.pular_linha(quantidade=1)
    pr.imprimir('[H]   >> Ajuda com o Sistema', alinhar='esquerda', tamanho=120)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema', alinhar='esquerda', tamanho=120)
    pr.imprimir('[N]   >> Cria uma Nova Compra', alinhar='esquerda', tamanho=120)
    pr.imprimir('[F]   >> Fechar a Compra', alinhar='esquerda', tamanho=120)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga', alinhar='esquerda', tamanho=120)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra', alinhar='esquerda', tamanho=120)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado', alinhar='esquerda', tamanho=120)
    pr.imprimir('[E]   >> Encerar caixa', alinhar='esquerda', tamanho=120)
    pr.pular_linha(quantidade=2)

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=80, alinhar='fim', end='🌹  ')
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
            pr.pular_linha(quantidade=2)
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
        desconto = total * 0.1 # calcula o valor do desconto
        total *= 0.9 # multiplicando o total por 0.9
    else:#verificar desconto para combos
        for codigo in set([item['codigo']for item in compra]):
           quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo]) 
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
            
    return total, desconto

menu()