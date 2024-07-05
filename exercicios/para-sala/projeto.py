import sys
sys.path.append('../../material')
import print_reprograma as pr
from datetime import datetime

produtos = [
    {'codigo': 1, 'nome': 'Matrix', 'valor': 10.00},
    {'codigo': 2, 'nome': 'Interestelar', 'valor': 10.00},
    {'codigo': 3, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 4, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 5, 'nome': 'Pulp Fiction', 'valor': 15.00},
    {'codigo': 6, 'nome': 'Fight Club', 'valor': 15.00},
    {'codigo': 7, 'nome': 'The Shawshank Redemption', 'valor': 15.00},
    {'codigo': 8, 'nome': 'Forrest Gump', 'valor': 15.00},
    {'codigo': 9, 'nome': 'The Godfather', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Schindler\'s List', 'valor': 15.00},
    {'codigo': 11, 'nome': 'Goodfellas', 'valor': 15.00},
    {'codigo': 12, 'nome': 'The Silence of the Lambs', 'valor': 15.00},
    {'codigo': 13, 'nome': 'Star Wars: Episode IV - A New Hope', 'valor': 5.00},
    {'codigo': 14, 'nome': 'The Lord of the Rings: The Fellowship of the Ring', 'valor': 10.00},
    {'codigo': 15, 'nome': 'The Matrix Reloaded', 'valor': 15.00},
    {'codigo': 16, 'nome': 'The Matrix Revolutions', 'valor': 15.00},
    {'codigo': 17, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 18, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 19, 'nome': 'Fight Club', 'valor': 12.00},
    {'codigo': 20, 'nome': 'The Shawshank Redemption', 'valor': 15.00},
    {'codigo': 21, 'nome': 'The Godfather', 'valor': 18.00},
    {'codigo': 22, 'nome': 'Schindler\'s List', 'valor': 12.00},
    {'codigo': 23, 'nome': 'Goodfellas', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Star Wars: Episode IV - A New Hope', 'valor': 15.00},
    {'codigo': 25, 'nome': 'The Lord of the Rings: The Fellowship of the Ring', 'valor': 18.00},
    {'codigo': 26, 'nome': 'The Matrix', 'valor': 20.00},
    {'codigo': 27, 'nome': 'Interstellar', 'valor': 15.00},
    {'codigo': 28, 'nome': 'The Dark Knight Rises', 'valor': 18.00},
    {'codigo': 29, 'nome': 'Pulp Fiction', 'valor': 15.00},
    {'codigo': 30, 'nome': 'Forrest Gump', 'valor': 12.00},
    {'codigo': 31, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 32, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 33, 'nome': 'Fight Club', 'valor': 12.00},
    {'codigo': 34, 'nome': 'The Shawshank Redemption', 'valor': 15.00},
    {'codigo': 35, 'nome': 'The Dark Knight', 'valor': 15.00},
    {'codigo': 36, 'nome': 'The Lord of the Rings: The Two Towers', 'valor': 10.00},
    {'codigo': 37, 'nome': 'Star Wars: Episode V - The Empire Strikes Back', 'valor': 15.00},
    {'codigo': 38, 'nome': 'Forrest Gump', 'valor': 12.00},
    {'codigo': 39, 'nome': 'Goodfellas', 'valor': 10.00},
    {'codigo': 40, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 41, 'nome': 'The Matrix', 'valor': 10.00},
    {'codigo': 42, 'nome': 'Fight Club', 'valor': 12.00},
    {'codigo': 43, 'nome': 'The Shawshank Redemption', 'valor': 10.00},
    {'codigo': 44, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 45, 'nome': 'Schindler\'s List', 'valor': 10.00},
    {'codigo': 46, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 47, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 48, 'nome': 'The Lord of the Rings: The Return of the King', 'valor': 10.00},
    {'codigo': 49, 'nome': 'Star Wars: Episode VI - Return of the Jedi', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Forrest Gump', 'valor': 10.00},
    {'codigo': 51, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 52, 'nome': 'Fight Club', 'valor': 10.00},
    {'codigo': 53, 'nome': 'The Shawshank Redemption', 'valor': 10.00},
    {'codigo': 54, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 55, 'nome': 'Schindler\'s List', 'valor': 10.00},
    {'codigo': 56, 'nome': 'Goodfellas', 'valor': 10.00},
    {'codigo': 57, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 58, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 59, 'nome': 'The Lord of the Rings: The Fellowship of the Ring', 'valor': 10.00},
    {'codigo': 60, 'nome': 'Star Wars: Episode IV - A New Hope', 'valor': 10.00},
    {'codigo': 61, 'nome': 'The Matrix', 'valor': 10.00},
    {'codigo': 62, 'nome': 'Interstellar', 'valor': 10.00},
    {'codigo': 63, 'nome': 'The Dark Knight Rises', 'valor': 10.00},
    {'codigo': 64, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 65, 'nome': 'Forrest Gump', 'valor': 10.00},
    {'codigo': 66, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 67, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 68, 'nome': 'Fight Club', 'valor': 10.00},
    {'codigo': 69, 'nome': 'The Shawshank Redemption', 'valor': 10.00},
    {'codigo': 70, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 71, 'nome': 'The Lord of the Rings: The Two Towers', 'valor': 10.00},
    {'codigo': 72, 'nome': 'Star Wars: Episode V - The Empire Strikes Back', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Forrest Gump', 'valor': 10.00},
    {'codigo': 74, 'nome': 'Goodfellas', 'valor': 10.00},
    {'codigo': 75, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 76, 'nome': 'The Matrix', 'valor': 10.00},
    {'codigo': 77, 'nome': 'Fight Club', 'valor': 10.00},
    {'codigo': 78, 'nome': 'The Shawshank Redemption', 'valor': 10.00},
    {'codigo': 79, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 80, 'nome': 'Schindler\'s List', 'valor': 10.00},
    {'codigo': 81, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 82, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 83, 'nome': 'The Lord of the Rings: The Return of the King', 'valor': 10},
    {'codigo': 84, 'nome': 'Star Wars: Episode VI - Return of the Jedi', 'valor': 10.00},
    {'codigo': 85, 'nome': 'Forrest Gump', 'valor': 10.00},
    {'codigo': 86, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 87, 'nome': 'Fight Club', 'valor': 10.00},
    {'codigo': 88, 'nome': 'The Shawshank Redemption', 'valor': 10.00},
    {'codigo': 89, 'nome': 'The Godfather', 'valor': 10.00},
    {'codigo': 90, 'nome': 'Schindler\'s List', 'valor': 10.00},
    {'codigo': 91, 'nome': 'Inception', 'valor': 10.00},
    {'codigo': 92, 'nome': 'The Dark Knight', 'valor': 10.00},
    {'codigo': 93, 'nome': 'The Lord of the Rings: The Fellowship of the Ring', 'valor': 10.00},
    {'codigo': 94, 'nome': 'Star Wars: Episode IV - A New Hope', 'valor': 10.00},
    {'codigo': 95, 'nome': 'The Matrix', 'valor': 10.00},
    {'codigo': 96, 'nome': 'Interstellar', 'valor': 10.00},
    {'codigo': 97, 'nome': 'The Dark Knight Rises', 'valor': 10.00},
    {'codigo': 98, 'nome': 'Pulp Fiction', 'valor': 10.00},
    {'codigo': 99, 'nome': 'Forrest Gump', 'valor': 10.00},
    {'codigo': 100, 'nome': 'Inception', 'valor': 10.00},
]

def produto_codigo(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None

def novo_produto(produto, quantidade):
    return {
        'codigo':produto['codigo'],
        'nome':produto['nome'],
        'valor':produto['valor'],
        'quantidade':quantidade
    }

def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')
    total = 0
    total_desconto = 0
    for compra in compras:
        total += compra['total']
        total_desconto += compra['desconto'] # Acumular o desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.separador(120,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')
    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')

def imprime_compra_fechada(compra,total, desconto):
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
    if(len(compra) > 0):
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')
        for produto in compra:
            imprimir_produto(produto)
            total += produto['valor'] * produto['quantidade']
        pr.separador(120,caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim')
    else:
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')
    pr.pular_linha()
    pr.pular_linha()

def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
    pr.separador(120,cor_texto='ciano')
    if(erro != ''):
        pr.imprimir(erro,tamanho=120,alinhar='centro',cor_texto='vermelho negrito')
        pr.separador(120,cor_texto='ciano')
    erro = ''

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

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=115,alinhar='fim',end='🎬 ')

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
       desconto = total * 0.1 # calcula o valor do desconto
       total *= 0.9 # multiplicando o total por 0.9
    else: #verificar desconto para combos
        for codigo in set([item['codigo'] for item in compra]):
            quantidade_codigo = sum([item['quantidade'] for item in compra if item ['codigo']])
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5

    return total, desconto

menu()