import sys
sys.path.append("material")
import print_reprograma as pr
from datetime import datetime   

produtos = [
    {'codigo': 1, 'nome': 'Carro de Controle Remoto', 'valor': 50.00},
    {'codigo': 2, 'nome': 'Boneca Barbie', 'valor': 60.00},
    {'codigo': 3, 'nome': 'Lego Star Wars', 'valor': 120.00},
    {'codigo': 4, 'nome': 'Quebra-Cabeça 1000 Peças', 'valor': 30.00},
    {'codigo': 5, 'nome': 'Carrinho Hot Wheels', 'valor': 10.00},
    {'codigo': 6, 'nome': 'Bola de Futebol', 'valor': 40.00},
    {'codigo': 7, 'nome': 'Jogo de Tabuleiro Monopoly', 'valor': 80.00},
    {'codigo': 8, 'nome': 'Boneco de Ação Superman', 'valor': 45.00},
    {'codigo': 9, 'nome': 'Pista de Carrinhos Hot Wheels', 'valor': 70.00},
    {'codigo': 10, 'nome': 'Patinete Infantil', 'valor': 150.00},
    {'codigo': 11, 'nome': 'Pelúcia Mickey Mouse', 'valor': 35.00},
    {'codigo': 12, 'nome': 'Kit de Pintura Infantil', 'valor': 25.00},
    {'codigo': 13, 'nome': 'Blocos de Montar Mega Bloks', 'valor': 100.00},
    {'codigo': 14, 'nome': 'Triciclo Infantil', 'valor': 200.00},
    {'codigo': 15, 'nome': 'Jogo da Memória', 'valor': 20.00},
    {'codigo': 16, 'nome': 'Lança-Dardos Nerf', 'valor': 80.00},
    {'codigo': 17, 'nome': 'Boneca Baby Alive', 'valor': 90.00},
    {'codigo': 18, 'nome': 'Castelo de Brinquedo', 'valor': 150.00},
    {'codigo': 19, 'nome': 'Play-Doh Massinha', 'valor': 25.00},
    {'codigo': 20, 'nome': 'Quebra-Cabeça 3D', 'valor': 50.00},
    {'codigo': 21, 'nome': 'Boneco Transformers', 'valor': 60.00},
    {'codigo': 22, 'nome': 'Kit Médico Infantil', 'valor': 40.00},
    {'codigo': 23, 'nome': 'Brinquedo Educativo de Madeira', 'valor': 70.00},
    {'codigo': 24, 'nome': 'Brinquedo de Banho', 'valor': 15.00},
    {'codigo': 25, 'nome': 'Carrinho de Bebê de Brinquedo', 'valor': 55.00},
    {'codigo': 26, 'nome': 'Robô de Brinquedo', 'valor': 130.00},
    {'codigo': 27, 'nome': 'Casa de Bonecas', 'valor': 250.00},
    {'codigo': 28, 'nome': 'Jogo de Construção K¨NEX', 'valor': 100.00},
    {'codigo': 29, 'nome': 'Kit de Cozinha Infantil', 'valor': 80.00},
    {'codigo': 30, 'nome': 'Boneca Elsa (Frozen)', 'valor': 60.00},
    {'codigo': 31, 'nome': 'Bicicleta Infantil', 'valor': 300.00},
    {'codigo': 32, 'nome': 'Trenzinho de Brinquedo', 'valor': 50.00},
    {'codigo': 33, 'nome': 'Cubo Mágico', 'valor': 20.00},
    {'codigo': 34, 'nome': 'Mochila Escolar com Rodinhas', 'valor': 90.00},
    {'codigo': 35, 'nome': 'Jogo de Xadrez', 'valor': 40.00},
    {'codigo': 36, 'nome': 'Mini Cozinha Infantil', 'valor': 120.00},
    {'codigo': 37, 'nome': 'Balanço de Brinquedo', 'valor': 150.00},
    {'codigo': 38, 'nome': 'Kit de Ferramentas Infantil', 'valor': 50.00},
    {'codigo': 39, 'nome': 'Brinquedo de Empilhar', 'valor': 30.00},
    {'codigo': 40, 'nome': 'Bola de Basquete Infantil', 'valor': 25.00},
    {'codigo': 41, 'nome': 'Roupão de Super-Herói', 'valor': 35.00},
    {'codigo': 42, 'nome': 'Trator de Brinquedo', 'valor': 55.00},
    {'codigo': 43, 'nome': 'Fantasia de Princesa', 'valor': 80.00},
    {'codigo': 44, 'nome': 'Piscina de Bolinhas', 'valor': 200.00},
    {'codigo': 45, 'nome': 'Patins Infantil', 'valor': 120.00},
    {'codigo': 46, 'nome': 'Miniatura de Carro de Bombeiros', 'valor': 30.00},
    {'codigo': 47, 'nome': 'Livro Interativo Infantil', 'valor': 40.00},
    {'codigo': 48, 'nome': 'Bicicleta com Rodinhas', 'valor': 250.00},
    {'codigo': 49, 'nome': 'Brinquedo Musical', 'valor': 60.00},
    {'codigo': 50, 'nome': 'Conjunto de Fazendinha', 'valor': 100.00},
    {'codigo': 51, 'nome': 'Brinquedo de Arremesso de Argolas', 'valor': 20.00},
    {'codigo': 52, 'nome': 'Dinossauro de Brinquedo', 'valor': 50.00},
    {'codigo': 53, 'nome': 'Tenda Infantil', 'valor': 150.00},
    {'codigo': 54, 'nome': 'Móbile para Berço', 'valor': 40.00},
    {'codigo': 55, 'nome': 'Jogo da Velha', 'valor': 15.00},
    {'codigo': 56, 'nome': 'Bola de Vôlei Infantil', 'valor': 25.00},
    {'codigo': 57, 'nome': 'Kit de Jardinagem Infantil', 'valor': 35.00},
    {'codigo': 58, 'nome': 'Mini Mercado de Brinquedo', 'valor': 80.00},
    {'codigo': 59, 'nome': 'Pelúcia Ursinho', 'valor': 30.00},
    {'codigo': 60, 'nome': 'Jogo de Damas', 'valor': 20.00},
    {'codigo': 61, 'nome': 'Labirinto de Bolinhas', 'valor': 50.00},
    {'codigo': 62, 'nome': 'Mini Robô de Brinquedo', 'valor': 70.00},
    {'codigo': 63, 'nome': 'Brinquedo de Fazendinha', 'valor': 60.00},
    {'codigo': 64, 'nome': 'Lança-Bolhas', 'valor': 20.00},
    {'codigo': 65, 'nome': 'Carrinho de Controle Remoto', 'valor': 90.00},
    {'codigo': 66, 'nome': 'Microfone Infantil', 'valor': 30.00},
    {'codigo': 67, 'nome': 'Fantoches', 'valor': 40.00},
    {'codigo': 68, 'nome': 'Barraca de Brincar', 'valor': 120.00},
    {'codigo': 69, 'nome': 'Tablet Educativo Infantil', 'valor': 150.00},
    {'codigo': 70, 'nome': 'Lousa Magnética', 'valor': 35.00},
    {'codigo': 71, 'nome': 'Blocos de Construção', 'valor': 45.00},
    {'codigo': 72, 'nome': 'Livro de Colorir', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Quebra-Cabeça Infantil', 'valor': 25.00},
    {'codigo': 74, 'nome': 'Brinquedo de Empurrar', 'valor': 50.00},
    {'codigo': 75, 'nome': 'Brinquedo de Montar', 'valor': 60.00},
    {'codigo': 76, 'nome': 'Mochila com Rodinhas', 'valor': 70.00},
    {'codigo': 77, 'nome': 'Brinquedo de Cozinha', 'valor': 80.00},
    {'codigo': 78, 'nome': 'Bicicleta para Criança', 'valor': 200.00},
    {'codigo': 79, 'nome': 'Caminhão de Brinquedo', 'valor': 55.00},
    {'codigo': 80, 'nome': 'Brinquedo de Equilíbrio', 'valor': 45.00},
    {'codigo': 81, 'nome': 'Conjunto de Animais de Brinquedo', 'valor': 40.00},
    {'codigo': 82, 'nome': 'Brinquedo Educativo', 'valor': 70.00},
    {'codigo': 83, 'nome': 'Pista de Corrida', 'valor': 100.00},
    {'codigo': 84, 'nome': 'Kit de Polícia Infantil', 'valor': 60.00},
    {'codigo': 85, 'nome': 'Brinquedo Musical Infantil', 'valor': 50.00},
    {'codigo': 86, 'nome': 'Quebra-Cabeça de Madeira', 'valor': 30.00},
    {'codigo': 87, 'nome': 'Boneca Princesa', 'valor': 70.00},
    {'codigo': 88, 'nome': 'Jogo de Cartas Uno', 'valor': 20.00},
    {'codigo': 89, 'nome': 'Kit de Ciência Infantil', 'valor': 80.00},
    {'codigo': 90, 'nome': 'Super-Herói de Brinquedo', 'valor': 50.00},
    {'codigo': 91, 'nome': 'Brinquedo Interativo', 'valor': 90.00},
    {'codigo': 92, 'nome': 'Brinquedo de Construção', 'valor': 100.00},
    {'codigo': 93, 'nome': 'Carrinho de Brinquedo', 'valor': 30.00},
    {'codigo': 94, 'nome': 'Patinete com Luzes', 'valor': 120.00},
    {'codigo': 95, 'nome': 'Kit de Pintura a Dedo', 'valor': 20.00},
    {'codigo': 96, 'nome': 'Boneco de Super-Herói', 'valor': 45.00},
    {'codigo': 97, 'nome': 'Carrinho de Brinquedo com Controle Remoto', 'valor': 90.00},
    {'codigo': 98, 'nome': 'Brinquedo de Montagem', 'valor': 60.00},
    {'codigo': 99, 'nome': 'Blocos de Montagem Educativos', 'valor': 80.00},
    {'codigo': 100, 'nome': 'Quebra-Cabeça Gigante', 'valor': 120.00}
]

def produto_codigo(codigo): 
    for produto in produtos:
        if produto['codigo'] == codigo:   
            return produto
    return None

def novo_produto(produto, quantidade):
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
    }

def calcula_total_desconto(compra):
    total = 0
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])
        
    desconto = 0
    
    if total >= 100:
        desconto = total * 0.1 # calcula o valor do desconto
        total -= desconto 
    else:
        # Verificar desconto para combos
        for codigo in set([item['codigo'] for item in compra]):
            quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo])
            if quantidade_codigo > 1:
                desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
                total-= desconto
                
    return total, desconto  # Retorna o total e o desconto

def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')
    total = 0
    total_desconto = 0 # inicializando com 0
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
    pr.imprimir('[R]   >> Remover o codigo do produto da compra', alinhar='centro', tamanho=120)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra', alinhar='centro', tamanho=120)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado', alinhar='centro', tamanho=120)
    pr.imprimir('[E]   >> Encerar caixa', alinhar='centro', tamanho=120)
    pr.pular_linha(quantidade=2)

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=115, alinhar='fim', end=' 🍒 : ')
    return input().lower()

def remover_produto(compra, codigo):
    codigo = int(input("Digite o código do produto a ser removido: "))
    for produto in compra:
        if produto['codigo'] == codigo:
            compra.remove(produto)
            return True
    return False


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
            pr.imprimir('Pressione [H] para ajuda com o Sistema', alinhar='centro', tamanho=120)
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
            print("\nConfirma pagamento da compra? (s/n)")
            confirmacao = input().lower()
            compra = []
            tela = ''
        elif opcao.startswith('r'):
            try:
                codigo = int()
                if remover_produto(compra, codigo):
                    pr.imprimir(f'Produto com código {codigo} removido da compra.', alinhar='centro', tamanho=120)
                else:
                    pr.imprimir(f'Produto com código {codigo} não encontrado na compra.', alinhar='centro', tamanho=120)
            except ValueError:
                erro = 'O código do produto deve ser numérico'
        elif opcao.isdigit():
            quantidade = 1
            if opcao.startswith('x'):
                _, quantidade = opcao[1:].split('x')
                quantidade = int(quantidade)
            
            codigo = int(opcao)
            produto = produto_codigo(codigo)
            
            if produto:
                compra.append(novo_produto(produto, quantidade))
            else:
                erro = 'Produto não encontrado. Por favor, tente novamente.'
        
        else:
            erro = 'Opção inválida. Por favor, escolha uma opção válida.'
        

menu()
