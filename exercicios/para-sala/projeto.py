import print_reprograma as pr # Podemos usar 'pr' para chamar as funções da biblioteca
from datetime import datetime # Importamos a biblioteca datetime para trabalhar com datas e horas

produtos = [
    {'codigo': 1, 'nome': 'Boneca Articulada', 'valor': 25.00},
    {'codigo': 2, 'nome': 'Carrinho de Controle Remoto', 'valor': 30.00},
    {'codigo': 3, 'nome': 'Jogo de Quebra-Cabeça', 'valor': 15.00},
    {'codigo': 4, 'nome': 'Bola de Futebol', 'valor': 20.00},
    {'codigo': 5, 'nome': 'Kit de Massinha de Modelar', 'valor': 12.00},
    {'codigo': 6, 'nome': 'Conjunto de Blocos de Montar', 'valor': 18.00},
    {'codigo': 7, 'nome': 'Boneco de Pelúcia', 'valor': 22.00},
    {'codigo': 8, 'nome': 'Cubo Mágico', 'valor': 10.00},
    {'codigo': 9, 'nome': 'Kit de Tintas e Pincéis', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Pista de Corrida de Carros', 'valor': 35.00},
    {'codigo': 11, 'nome': 'Jogo de Tabuleiro', 'valor': 25.00},
    {'codigo': 12, 'nome': 'Kit de Ferramentas de Brinquedo', 'valor': 20.00},
    {'codigo': 13, 'nome': 'Quebra-Cabeça 3D', 'valor': 18.00},
    {'codigo': 14, 'nome': 'Jogo de Mini-Golfe', 'valor': 28.00},
    {'codigo': 15, 'nome': 'Kit de Fantoches', 'valor': 15.00},
    {'codigo': 16, 'nome': 'Bicicleta Infantil', 'valor': 120.00},
    {'codigo': 17, 'nome': 'Patins com Rodinhas', 'valor': 50.00},
    {'codigo': 18, 'nome': 'Kit de Instrumentos Musicais', 'valor': 40.00},
    {'codigo': 19, 'nome': 'Pelúcia Interativa', 'valor': 30.00},
    {'codigo': 20, 'nome': 'Kit de Ciências para Crianças', 'valor': 25.00},
    {'codigo': 21, 'nome': 'Piano de Brinquedo', 'valor': 35.00},
    {'codigo': 22, 'nome': 'Kit de Construção de Avião', 'valor': 18.00},
    {'codigo': 23, 'nome': 'Kit de Médico ou Enfermeiro', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Mochila com Acessórios de Exploração', 'valor': 30.00},
    {'codigo': 25, 'nome': 'Lego de Tema Espacial', 'valor': 40.00},
    {'codigo': 26, 'nome': 'Boliche de Brinquedo', 'valor': 22.00},
    {'codigo': 27, 'nome': 'Kit de Arte com Giz de Cera', 'valor': 12.00},
    {'codigo': 28, 'nome': 'Fantoche de Dedo', 'valor': 8.00},
    {'codigo': 29, 'nome': 'Kit de Construção de Robô', 'valor': 35.00},
    {'codigo': 30, 'nome': 'Quebra-Cabeça Gigante', 'valor': 30.00},
    {'codigo': 31, 'nome': 'Kit de Artesanato em Papel', 'valor': 18.00},
    {'codigo': 32, 'nome': 'Jogo de Dama', 'valor': 12.00},
    {'codigo': 33, 'nome': 'Boneco Super-Herói Articulado', 'valor': 28.00},
    {'codigo': 34, 'nome': 'Kit de Maquiagem Infantil', 'valor': 20.00},
    {'codigo': 35, 'nome': 'Kit de Ferramentas de Madeira', 'valor': 25.00},
    {'codigo': 36, 'nome': 'Kit de Ciências Naturais', 'valor': 30.00},
    {'codigo': 37, 'nome': 'Jogo de Vôlei de Praia', 'valor': 40.00},
    {'codigo': 38, 'nome': 'Carrinho de Pedal', 'valor': 80.00},
    {'codigo': 39, 'nome': 'Kit de Fazendinha com Animais', 'valor': 35.00},
    {'codigo': 40, 'nome': 'Kit de Futebol de Botão', 'valor': 15.00},
    {'codigo': 41, 'nome': 'Patinete Infantil', 'valor': 60.00},
    {'codigo': 42, 'nome': 'Kit de Pintura em Tela', 'valor': 25.00},
    {'codigo': 43, 'nome': 'Kit de Construção de Castelo de Areia', 'valor': 20.00},
    {'codigo': 44, 'nome': 'Brinquedo de Conta Histórias', 'valor': 30.00},
    {'codigo': 45, 'nome': 'Jogo de Basquete de Mesa', 'valor': 18.00},
    {'codigo': 46, 'nome': 'Kit de Jardinagem Infantil', 'valor': 22.00},
    {'codigo': 47, 'nome': 'Mini Skate', 'valor': 25.00},
    {'codigo': 48, 'nome': 'Kit de Alimentos de Brinquedo', 'valor': 15.00},
    {'codigo': 49, 'nome': 'Jogo de Memória', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Kit de Maquete de Navio', 'valor': 35.00},
]



def produto_codigo(codigo): # Esta função procura um produto pelo código que você digitar
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto


def novo_produto(produto, quantidade): # Esta função cria um novo item para a sua compra.
    return { # Criamos um novo dicionário para guardar as informações do item da compra
        'codigo':produto['codigo'],
        'nome':produto['nome'],
        'valor':produto['valor'],
        'quantidade':quantidade
    }


def imprime_fechamento_caixa(compras): # Esta função imprime um resumo de todas as compras do dia.
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')  
    total = 0  # Inicializamos a variável 'total' para guardar o valor total das compras
    total_desconto = 0 
    for compra in compras:  # Percorremos a lista de compras, uma por uma
        total += compra['total'] # Somamos o valor total da compra ao total geral
        total_desconto += compra['desconto'] #acumular o desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro') # Imprimimos a quantidade de itens
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.separador(120,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|') # Imprimimos o total das compras
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')

    #imprime total de desconto no dia
    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')


def imprime_compra_fechada(compra, total, desconto): # Esta função imprime uma compra fechada, mostrando todos os itens e o total a pagar.
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|') # Imprimimos o cabeçalho da tabela de produtos da compra
    pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')
    for produto in compra:
        imprimir_produto(produto) # Chamamos a função 'imprimir_produto' para imprimir as informações do produto
        total_compra += produto['valor'] * produto['quantidade']
    pr.separador(120,caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    
    
    if desconto > 0: #imprimir o valor do desconto
         pr.imprimir('Desconto', tamanho=107, alinhar='fim', end='|')
         pr.imprimir('-R$',str(round(desconto, 2)), tamanho=12, alinhar='fim',cor_texto='magenta')

    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim',cor_texto='verde negrito')

    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()


def imprime_compra(compra):#imprime os detalhes do produto 
    if(len(compra) > 0): # Se a lista de produtos não estiver vazia
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')   
        for produto in compra: # Percorremos a lista de produtos da compra, um por um
            total += produto['valor'] * produto['quantidade'] # Somamos o valor total do produto ao subtotal da compra
            imprimir_produto(produto)
        pr.separador(120,caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim')
    else:
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')
    pr.pular_linha()
    pr.pular_linha()


def imprimir_produto(produto): # Esta função imprime as informações de um produto, como código, nome, quantidade e valor.
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')


def imprimir_cabecalho(erro): #para imprimir cabeçalho, recebe a mensagem de erro como entrada
    pr.limpar()
    pr.retangulo('{reprograma} \nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=92, margem=2, cor_texto='azul negrito', cor_barra='magenta')
    pr.separador(105, cor_texto='ciano')
    if(erro != ''): # Se a mensagem de erro não estiver vazia
        pr.imprimir(erro, tamanho= 120, alinhar= 'centro', cor_texto= 'vermelho negrito')
        pr.separador(105, cor_texto='ciano')
    erro = ''


def imprimir_ajuda(): #para aparecer menu ajuda, Esta função não recebe nenhuma entrada
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=108)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=108)
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=108)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=108)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=108)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=108)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=108)
    pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=108)
    pr.pular_linha(quantidade=2)


def imprimir_rodape(): #para imprimir rodapé, Esta função não recebe nenhuma entrada
    pr.imprimir('[H] Ajuda', '[Q] Sair' , caracter='=', tamanho=108, alinhar='fim', end='🍀 ')

    return input().lower() # Lê a opção do usuário e converte para letras minúsculas


def menu(): # Esta função é a função principal do programa, não recebe nenhuma entrada
    opcao = '' # Inicializamos a variável 'opcao' como uma string vazia
    erro = ''
    tela = ''
    compra = [] #inicia vazia para armazenar a compra individual
    compras = [] #inicia vazia para armazenar fechamento do caixa, faturamento
    while(opcao != 'q'): #Enquanto a opção do usuário for diferente de 'q' (sair)
        imprimir_cabecalho(erro) # Chamamos a função 'imprimir_cabecalho' para imprimir o cabeçalho
        if(tela ==''): #se a tela atual for vazia
            pr.pular_linha(quantidade =4)
        elif(tela == 'ajuda'): #se a tela atual for ajuda
            imprimir_ajuda()
            tela = '' # Definimos a tela atual como vazia (retorna para a tela inicial)
        elif(tela == 'compra'):
            imprime_compra(compra)
        elif(tela == 'fechar'):
            total, desconto = calcula_total_desconto(compra)
            imprime_compra_fechada(compra, total, desconto)
        elif(tela =='encerrar'):
            imprime_fechamento_caixa(compras)
            compras = [] # Limpamos a lista de compras fechadas
            tela = '' # Definimos a tela atual como vazia (retorna para a tela inicial)
            pr.pular_linha(quantidade=2)
        opcao = imprimir_rodape() # Chamamos a função 'imprimir_rodape' para imprimir as opções do rodapé e ler a opção do usuário
        if(opcao == 'h'):
            tela = 'ajuda'
        elif(opcao =='n'):
            tela = 'compra'
        elif(opcao == 'f'):
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif(opcao == 'e'):
            tela = 'encerrar'
        elif('p' in opcao): # Se a opção do usuário contiver 'p' (pagar)
            compras.append({'itens': compra, 'total': total, 'data': datetime.now(), 'desconto': desconto}) # Adiciona(append) a compra atual à lista de compras fechadas
            compra = [] #limpamos a lista de produtos da tela atual
            tela = ''
        else:  # Caso contrário (opção inválida) 
            try: # Tentamos converter a opção do usuário para um número inteiro
                codigo = int(opcao) # Converte a opção para um número inteiro
                produto = produto_codigo(codigo) # Chamamos a função 'produto_codigo' para encontrar o produto com o código fornecido
                compra.append(novo_produto(produto,1)) # Adiciona o produto à lista de produtos da compra atual
            except ValueError: # Se a opção do usuário não for um número inteiro
                erro = 'A opção selecionada não existe no sistema'
            except TypeError:  # Se o produto não for encontrado
                erro = 'O código do produto não existe' # Define a mensagem de erro


def calcula_total_desconto(compra):
    total = 0 # Inicializamos a variável 'total' para armazenar o valor total da compra
    for produto in compra: # Percorre cada item na lista de compras, iteramos sobre cada produto na lista de compra
        total += (produto['valor'] * produto['quantidade'])

    desconto = 0
    
    if total >= 100: # regra para aplicar desconto
        desconto = total * 0.1 #calcula o valor do desconto
        total *= 0.9 # multiplica o total por 0.9 (que é 90% do produto)
   
    else: #verifica desconto para combo
        for codigo in set([item['codigo']for item in compra]):
            quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo]) 
        if quantidade_codigo > 1:
            desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5

    return total, desconto


def remover_item(compra, codigo):
    compra[:] = [item for item in compra if item ['codigo'] != codigo] #[:] está modificando a lista; 
    return compra
    

menu() # Chama a função 'menu' para iniciar o programa



