import print_reprograma as pr
from datetime import datetime

produtos = [
    {'codigo': 1, 'nome': 'The Legend of Zelda: Breath of the Wild', 'valor': 299.99},
    {'codigo': 2, 'nome': 'Super Mario Odyssey', 'valor': 199.99},
    {'codigo': 3, 'nome': 'Red Dead Redemption 2', 'valor': 249.99},
    {'codigo': 4, 'nome': 'The Witcher 3: Wild Hunt', 'valor': 99.99},
    {'codigo': 5, 'nome': 'God of War', 'valor': 179.99},
    {'codigo': 6, 'nome': 'Final Fantasy VII Remake', 'valor': 279.99},
    {'codigo': 7, 'nome': 'Persona 5 Royal', 'valor': 199.99},
    {'codigo': 8, 'nome': 'Minecraft', 'valor': 89.99},
    {'codigo': 9, 'nome': 'Animal Crossing: New Horizons', 'valor': 299.99},
    {'codigo': 10, 'nome': 'Cyberpunk 2077', 'valor': 299.99},
    {'codigo': 11, 'nome': 'GTA V', 'valor': 149.99},
    {'codigo': 12, 'nome': 'Horizon Zero Dawn', 'valor': 99.99},
    {'codigo': 13, 'nome': 'FIFA 23', 'valor': 299.99},
    {'codigo': 14, 'nome': 'Call of Duty: Modern Warfare', 'valor': 199.99},
    {'codigo': 15, 'nome': 'Assassin\'s Creed Valhalla', 'valor': 249.99},
    {'codigo': 16, 'nome': 'Resident Evil Village', 'valor': 279.99},
    {'codigo': 17, 'nome': 'Halo Infinite', 'valor': 299.99},
    {'codigo': 18, 'nome': 'Forza Horizon 5', 'valor': 199.99},
    {'codigo': 19, 'nome': 'Spider-Man: Miles Morales', 'valor': 179.99},
    {'codigo': 20, 'nome': 'Doom Eternal', 'valor': 149.99},
    {'codigo': 21, 'nome': 'Sekiro: Shadows Die Twice', 'valor': 199.99},
    {'codigo': 22, 'nome': 'Ghost of Tsushima', 'valor': 299.99},
    {'codigo': 23, 'nome': 'Apex Legends', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 24, 'nome': 'Fortnite', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 25, 'nome': 'Overwatch', 'valor': 199.99},
    {'codigo': 26, 'nome': 'Battlefield V', 'valor': 149.99},
    {'codigo': 27, 'nome': 'Dark Souls III', 'valor': 129.99},
    {'codigo': 28, 'nome': 'Bloodborne', 'valor': 99.99},
    {'codigo': 29, 'nome': 'Nioh 2', 'valor': 249.99},
    {'codigo': 30, 'nome': 'Death Stranding', 'valor': 299.99},
    {'codigo': 31, 'nome': 'Control', 'valor': 199.99},
    {'codigo': 32, 'nome': 'Half-Life: Alyx', 'valor': 299.99},
    {'codigo': 33, 'nome': 'Cuphead', 'valor': 89.99},
    {'codigo': 34, 'nome': 'Hades', 'valor': 149.99},
    {'codigo': 35, 'nome': 'Celeste', 'valor': 79.99},
    {'codigo': 36, 'nome': 'Stardew Valley', 'valor': 49.99},
    {'codigo': 37, 'nome': 'Terraria', 'valor': 39.99},
    {'codigo': 38, 'nome': 'Undertale', 'valor': 29.99},
    {'codigo': 39, 'nome': 'Among Us', 'valor': 19.99},
    {'codigo': 40, 'nome': 'Fall Guys: Ultimate Knockout', 'valor': 79.99},
    {'codigo': 41, 'nome': 'Rocket League', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 42, 'nome': 'Valorant', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 43, 'nome': 'League of Legends', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 44, 'nome': 'Dota 2', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 45, 'nome': 'PUBG', 'valor': 99.99},
    {'codigo': 46, 'nome': 'Dead by Daylight', 'valor': 79.99},
    {'codigo': 47, 'nome': 'Rainbow Six Siege', 'valor': 149.99},
    {'codigo': 48, 'nome': 'Monster Hunter: World', 'valor': 199.99},
    {'codigo': 49, 'nome': 'Metro Exodus', 'valor': 149.99},
    {'codigo': 50, 'nome': 'Control', 'valor': 199.99},
    {'codigo': 51, 'nome': 'Ori and the Will of the Wisps', 'valor': 99.99},
    {'codigo': 52, 'nome': 'Hollow Knight', 'valor': 49.99},
    {'codigo': 53, 'nome': 'Subnautica', 'valor': 79.99},
    {'codigo': 54, 'nome': 'ARK: Survival Evolved', 'valor': 149.99},
    {'codigo': 55, 'nome': 'Rust', 'valor': 99.99},
    {'codigo': 56, 'nome': 'No Man\'s Sky', 'valor': 199.99},
    {'codigo': 57, 'nome': 'The Outer Worlds', 'valor': 249.99},
    {'codigo': 58, 'nome': 'Slay the Spire', 'valor': 59.99},
    {'codigo': 59, 'nome': 'The Elder Scrolls V: Skyrim', 'valor': 99.99},
    {'codigo': 60, 'nome': 'Dragon Age: Inquisition', 'valor': 79.99},
    {'codigo': 61, 'nome': 'Mass Effect: Andromeda', 'valor': 59.99},
    {'codigo': 62, 'nome': 'Star Wars Jedi: Fallen Order', 'valor': 199.99},
    {'codigo': 63, 'nome': 'The Sims 4', 'valor': 59.99},
    {'codigo': 64, 'nome': 'Civilization VI', 'valor': 149.99},
    {'codigo': 65, 'nome': 'XCOM 2', 'valor': 129.99},
    {'codigo': 66, 'nome': 'Divinity: Original Sin 2', 'valor': 199.99},
    {'codigo': 67, 'nome': 'Baldur\'s Gate 3', 'valor': 299.99},
    {'codigo': 68, 'nome': 'Disco Elysium', 'valor': 149.99},
    {'codigo': 69, 'nome': 'Hades', 'valor': 149.99},
    {'codigo': 70, 'nome': 'Celeste', 'valor': 79.99},
    {'codigo': 71, 'nome': 'Stardew Valley', 'valor': 49.99},
    {'codigo': 72, 'nome': 'Terraria', 'valor': 39.99},
    {'codigo': 73, 'nome': 'Undertale', 'valor': 29.99},
    {'codigo': 74, 'nome': 'Among Us', 'valor': 19.99},
    {'codigo': 75, 'nome': 'Fall Guys: Ultimate Knockout', 'valor': 79.99},
    {'codigo': 76, 'nome': 'Rocket League', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 77, 'nome': 'Valorant', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 78, 'nome': 'League of Legends', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 79, 'nome': 'Dota 2', 'valor': 0.00},  # Jogo gratuito
    {'codigo': 80, 'nome': 'PUBG', 'valor': 99.99},
    {'codigo': 81, 'nome': 'Dead by Daylight', 'valor': 79.99},
    {'codigo': 81, 'nome': 'Dead by Daylight', 'valor': 79.99},
    {'codigo': 82, 'nome': 'Rainbow Six Siege', 'valor': 149.99},
    {'codigo': 83, 'nome': 'Monster Hunter: World', 'valor': 199.99},
    {'codigo': 84, 'nome': 'Metro Exodus', 'valor': 149.99},
    {'codigo': 85, 'nome': 'Control', 'valor': 199.99},
    {'codigo': 86, 'nome': 'Ori and the Will of the Wisps', 'valor': 99.99},
    {'codigo': 87, 'nome': 'Hollow Knight', 'valor': 49.99},
    {'codigo': 88, 'nome': 'Subnautica', 'valor': 79.99},
    {'codigo': 89, 'nome': 'ARK: Survival Evolved', 'valor': 149.99},
    {'codigo': 90, 'nome': 'Rust', 'valor': 99.99},
    {'codigo': 91, 'nome': 'No Man\'s Sky', 'valor': 199.99},
    {'codigo': 92, 'nome': 'The Outer Worlds', 'valor': 249.99},
    {'codigo': 93, 'nome': 'Slay the Spire', 'valor': 59.99},
    {'codigo': 94, 'nome': 'The Elder Scrolls V: Skyrim', 'valor': 99.99},
    {'codigo': 95, 'nome': 'Dragon Age: Inquisition', 'valor': 79.99},
    {'codigo': 96, 'nome': 'Mass Effect: Andromeda', 'valor': 59.99},
    {'codigo': 97, 'nome': 'Star Wars Jedi: Fallen Order', 'valor': 199.99},
    {'codigo': 98, 'nome': 'The Sims 4', 'valor': 59.99},
    {'codigo': 99, 'nome': 'Civilization VI', 'valor': 149.99},
    {'codigo': 100, 'nome': 'XCOM 2', 'valor': 129.99}
    
]

def produto_codigo(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto

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
        total_desconto += compra['desconto']
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.separador(120,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')
        #imprime total de desconto
    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')

def imprime_compra_fechada(compra, total, desconto):
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
    pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')   
    for produto in compra:
        imprimir_produto(produto)
        total_compra += produto['valor'] * produto['quantidade']
    pr.separador(120,caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    if desconto > 0:
       pr.imprimir('Desconto aplicado', tamanho=107, alinhar='fim', end='|')
       pr.imprimir('- R$', str(round(desconto, 2)), tamanho=12, alinhar='fim', cor_texto='vermelho negrito')  
       total_compra -= desconto
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim',cor_texto='verde negrito')
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
    pr.retangulo('{reprograma}\nLoja de jogos da AGATHA \nTerminal de Vendas',sv=1,tamanho=120, margem=10,cor_texto='vermelho',cor_barra='verde')
    pr.separador(140,cor_texto='amarelo')
    if(erro != ''):
        pr.imprimir(erro,tamanho=120,alinhar='centro',cor_texto='vermelho negrito')
        pr.separador(120,cor_texto='margeta')
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
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=120,alinhar='fim',end='🧚‍♀️ : ')

    return input().lower()

def calcula_total_desconto(compra):
    total = 0
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])
        
    desconto = 0 
    
    if total >= 100:                
      desconto = total * 0.1 
      total *= 0.9
    else:
        for codigo in set([item['codigo']for item in compra]):
            quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo]) 
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
            total -= desconto
            
    return total, desconto
 
def menu():
    opcao = ''
    erro = ''
    tela = ''
    compra = []
    compras = []
    while(opcao != 'q'):
        imprimir_cabecalho(erro)
        if(tela == ''):
            pr.pular_linha(quantidade=4)
        elif(tela == 'ajuda'):
            imprimir_ajuda()
            tela=''
        elif(tela == 'compra'):
            imprime_compra(compra)    
        elif(tela == 'fechar'):
            total, desconto = calcula_total_desconto(compra)
            imprime_compra_fechada(compra,total, desconto)
        elif(tela == 'encerar'):
            imprime_fechamento_caixa(compras)
            compras = []
            tela=''
            pr.pular_linha(quantidade=2)
        opcao = imprimir_rodape()
        if(opcao == 'h'):
            tela='ajuda'
        elif(opcao == 'n'):
            tela='compra'
        elif(opcao == 'f'):
             if compra:
                total = sum(produto['valor'] * produto['quantidade'] for produto in compra)
                print("\nConfirmar pagamento da compra? (s/n)")
                confirmacao = input().lower()
                total = calcula_total_desconto(compra)
                tela = 'fechar'
        elif(opcao == 'e'):
            tela = 'encerar'
        elif('p' in opcao):
            compras.append({'itens':compra, 'total':total, 'data': datetime.now(), 'desconto':desconto})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                compra.append(novo_produto(produto,1))
            except ValueError:
                erro = 'A opção selecionada não existe no sistema'

menu()