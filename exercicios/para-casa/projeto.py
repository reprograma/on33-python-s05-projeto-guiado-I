import print_reprograma as pr
from datetime import datetime

# Lista de produtos agora sendo mangás
produtos = [
    {'codigo': 1, 'nome': 'One Piece Vol. 1', 'valor': 29.99},
    {'codigo': 2, 'nome': 'Naruto Vol. 1', 'valor': 24.99},
    {'codigo': 3, 'nome': 'Attack on Titan Vol. 1', 'valor': 34.99},
    {'codigo': 4, 'nome': 'My Hero Academia Vol. 1', 'valor': 19.99},
    {'codigo': 5, 'nome': 'Dragon Ball Z Vol. 1', 'valor': 39.99},
    {'codigo': 6, 'nome': 'Demon Slayer Vol. 1', 'valor': 29.99},
    {'codigo': 7, 'nome': 'Tokyo Ghoul Vol. 1', 'valor': 34.99},
    {'codigo': 8, 'nome': 'Fullmetal Alchemist Vol. 1', 'valor': 24.99},
    {'codigo': 9, 'nome': 'Death Note Vol. 1', 'valor': 29.99},
    {'codigo': 10, 'nome': 'Bleach Vol. 1', 'valor': 24.99},
    {'codigo': 11, 'nome': 'Hunter x Hunter Vol. 1', 'valor': 34.99},
    {'codigo': 12, 'nome': 'Sword Art Online Vol. 1', 'valor': 19.99},
    {'codigo': 13, 'nome': 'Black Clover Vol. 1', 'valor': 24.99},
    {'codigo': 14, 'nome': 'The Promised Neverland Vol. 1', 'valor': 29.99},
    {'codigo': 15, 'nome': 'Chainsaw Man Vol. 1', 'valor': 34.99},
    {'codigo': 16, 'nome': 'JoJo\'s Bizarre Adventure Vol. 1', 'valor': 39.99},
    {'codigo': 17, 'nome': 'Blue Exorcist Vol. 1', 'valor': 19.99},
    {'codigo': 18, 'nome': 'Fairy Tail Vol. 1', 'valor': 24.99},
    {'codigo': 19, 'nome': 'One Punch Man Vol. 1', 'valor': 29.99},
    {'codigo': 20, 'nome': 'Re:Zero Vol. 1', 'valor': 34.99},
    {'codigo': 21, 'nome': 'Mob Psycho 100 Vol. 1', 'valor': 29.99},
    {'codigo': 22, 'nome': 'Berserk Vol. 1', 'valor': 39.99},
    {'codigo': 23, 'nome': 'Vinland Saga Vol. 1', 'valor': 34.99},
    {'codigo': 24, 'nome': 'Fruits Basket Vol. 1', 'valor': 24.99},
    {'codigo': 25, 'nome': 'Horimiya Vol. 1', 'valor': 19.99},
    {'codigo': 26, 'nome': 'Claymore Vol. 1', 'valor': 29.99},
    {'codigo': 27, 'nome': 'Neon Genesis Evangelion Vol. 1', 'valor': 34.99},
    {'codigo': 28, 'nome': 'Soul Eater Vol. 1', 'valor': 29.99},
    {'codigo': 29, 'nome': 'Akira Vol. 1', 'valor': 49.99},
    {'codigo': 30, 'nome': 'Dr. Stone Vol. 1', 'valor': 19.99},
    {'codigo': 31, 'nome': 'Haikyuu!! Vol. 1', 'valor': 24.99},
    {'codigo': 32, 'nome': 'Shaman King Vol. 1', 'valor': 29.99},
    {'codigo': 33, 'nome': 'Inuyasha Vol. 1', 'valor': 34.99},
    {'codigo': 34, 'nome': 'Kaguya-sama: Love is War Vol. 1', 'valor': 24.99},
    {'codigo': 35, 'nome': 'Mushishi Vol. 1', 'valor': 29.99},
    {'codigo': 36, 'nome': 'Yona of the Dawn Vol. 1', 'valor': 19.99},
    {'codigo': 37, 'nome': 'The Ancient Magus\' Bride Vol. 1', 'valor': 29.99},
    {'codigo': 38, 'nome': 'Beastars Vol. 1', 'valor': 24.99},
    {'codigo': 39, 'nome': 'Nisekoi Vol. 1', 'valor': 19.99},
    {'codigo': 40, 'nome': 'Toradora! Vol. 1', 'valor': 29.99},
    {'codigo': 41, 'nome': 'Golden Kamuy Vol. 1', 'valor': 34.99},
    {'codigo': 42, 'nome': 'Jujutsu Kaisen Vol. 1', 'valor': 29.99},
    {'codigo': 43, 'nome': 'The Rising of the Shield Hero Vol. 1', 'valor': 24.99},
    {'codigo': 44, 'nome': 'Noragami Vol. 1', 'valor': 19.99},
    {'codigo': 45, 'nome': 'Food Wars! Vol. 1', 'valor': 29.99},
    {'codigo': 46, 'nome': 'Spy x Family Vol. 1', 'valor': 34.99},
    {'codigo': 47, 'nome': 'Rent-A-Girlfriend Vol. 1', 'valor': 24.99},
    {'codigo': 48, 'nome': 'Trinity Seven Vol. 1', 'valor': 29.99},
    {'codigo': 49, 'nome': 'The Quintessential Quintuplets Vol. 1', 'valor': 19.99},
    {'codigo': 50, 'nome': 'Ao Haru Ride Vol. 1', 'valor': 24.99},
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