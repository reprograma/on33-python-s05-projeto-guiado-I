import print_reprograma as pr
from datetime import datetime

produtos = [
    {"codigo": 1, "nome": "Orgulho e Preconceito", "valor": 10.00},
    {"codigo": 2, "nome": "A República", "valor": 11.00},
    {"codigo": 3, "nome": "Pai Rico, Pai Pobre", "valor": 12.00},
    {"codigo": 4, "nome": "O Poder do Hábito", "valor": 13.00},
    {"codigo": 5, "nome": "O Iluminado", "valor": 14.00},
    {"codigo": 6, "nome": "Sapiens: Uma Breve História da Humanidade", "valor": 15.00},
    {"codigo": 7, "nome": "O Livro de Receitas da Dona Benta", "valor": 16.00},
    {"codigo": 8, "nome": "O Pequeno Príncipe", "valor": 17.00},
    {"codigo": 9, "nome": "Harry Potter e a Pedra Filosofal", "valor": 18.00},
    {"codigo": 10, "nome": "Introdução à Computação para Alunos Inteligentes - Volume 1", "valor": 19.00},
    {"codigo": 11, "nome": "1984", "valor": 20.00},
    {"codigo": 12, "nome": "Dom Quixote", "valor": 21.00},
    {"codigo": 13, "nome": "O Segredo", "valor": 22.00},
    {"codigo": 14, "nome": "A Arte da Guerra", "valor": 23.00},
    {"codigo": 15, "nome": "O Diário de Anne Frank", "valor": 24.00},
    {"codigo": 16, "nome": "Cem Anos de Solidão", "valor": 25.00},
    {"codigo": 17, "nome": "O Hobbit", "valor": 10.00},
    {"codigo": 18, "nome": "A História Secreta", "valor": 11.00},
    {"codigo": 19, "nome": "O Senhor dos Anéis: A Sociedade do Anel", "valor": 12.00},
    {"codigo": 20, "nome": "Mentes Perigosas", "valor": 13.00},
    {"codigo": 21, "nome": "A Cabana", "valor": 14.00},
    {"codigo": 22, "nome": "Steve Jobs", "valor": 15.00},
    {"codigo": 23, "nome": "O Alquimista", "valor": 16.00},
    {"codigo": 24, "nome": "Inferno", "valor": 17.00},
    {"codigo": 25, "nome": "As Aventuras de Sherlock Holmes", "valor": 18.00},
    {"codigo": 26, "nome": "O Código Da Vinci", "valor": 19.00},
    {"codigo": 27, "nome": "A Breve História do Tempo", "valor": 20.00},
    {"codigo": 28, "nome": "O Monge e o Executivo", "valor": 21.00},
    {"codigo": 29, "nome": "O Morro dos Ventos Uivantes", "valor": 22.00},
    {"codigo": 30, "nome": "Em Busca de Sentido", "valor": 23.00},
    {"codigo": 31, "nome": "A Revolução dos Bichos", "valor": 24.00},
    {"codigo": 32, "nome": "O Nome da Rosa", "valor": 25.00},
    {"codigo": 33, "nome": "A Menina que Roubava Livros", "valor": 10.00},
    {"codigo": 34, "nome": "O Amor nos Tempos do Cólera", "valor": 11.00},
    {"codigo": 35, "nome": "A Divina Comédia", "valor": 12.00},
    {"codigo": 36, "nome": "Jogos Vorazes", "valor": 13.00},
    {"codigo": 37, "nome": "As Crônicas de Nárnia", "valor": 14.00},
    {"codigo": 38, "nome": "Vinte Mil Léguas Submarinas", "valor": 15.00},
    {"codigo": 39, "nome": "O Senhor das Moscas", "valor": 16.00},
    {"codigo": 40, "nome": "Um Estudo em Vermelho", "valor": 17.00},
    {"codigo": 41, "nome": "O Sol é para Todos", "valor": 18.00},
    {"codigo": 42, "nome": "O Pequeno Príncipe", "valor": 19.00},
    {"codigo": 43, "nome": "O Conto da Aia", "valor": 20.00},
    {"codigo": 44, "nome": "A Bíblia Sagrada", "valor": 21.00},
    {"codigo": 45, "nome": "Moby Dick", "valor": 22.00},
    {"codigo": 46, "nome": "O Apanhador no Campo de Centeio", "valor": 23.00},
    {"codigo": 47, "nome": "Guerra e Paz", "valor": 24.00},
    {"codigo": 48, "nome": "E o Vento Levou", "valor": 25.00},
    {"codigo": 49, "nome": "O Perfume", "valor": 10.00},
    {"codigo": 50, "nome": "Neuromancer", "valor": 11.00},
    {"codigo": 51, "nome": "A Metamorfose", "valor": 12.00},
    {"codigo": 52, "nome": "A Roda do Tempo", "valor": 13.00},
    {"codigo": 53, "nome": "Uma Breve História de Quase Tudo", "valor": 14.00},
    {"codigo": 54, "nome": "O Homem Invisível", "valor": 15.00},
    {"codigo": 55, "nome": "A Casa dos Espíritos", "valor": 16.00},
    {"codigo": 56, "nome": "Anna Karenina", "valor": 17.00},
    {"codigo": 57, "nome": "Drácula", "valor": 18.00},
    {"codigo": 58, "nome": "Frankenstein", "valor": 19.00},
    {"codigo": 59, "nome": "Os Miseráveis", "valor": 20.00},
    {"codigo": 60, "nome": "A Montanha Mágica", "valor": 21.00},
    {"codigo": 61, "nome": "O Velho e o Mar", "valor": 22.00},
    {"codigo": 62, "nome": "O Senhor dos Anéis: As Duas Torres", "valor": 23.00},
    {"codigo": 63, "nome": "O Lobo da Estepe", "valor": 24.00},
    {"codigo": 64, "nome": "Memórias Póstumas de Brás Cubas", "valor": 25.00},
    {"codigo": 65, "nome": "Cem Anos de Solidão", "valor": 10.00},
    {"codigo": 66, "nome": "O Processo", "valor": 11.00},
    {"codigo": 67, "nome": "Coração das Trevas", "valor": 12.00},
    {"codigo": 68, "nome": "Os Três Mosqueteiros", "valor": 13.00},
    {"codigo": 69, "nome": "O Senhor dos Anéis: O Retorno do Rei", "valor": 14.00},
    {"codigo": 70, "nome": "Madame Bovary", "valor": 15.00},
    {"codigo": 71, "nome": "Viagem ao Centro da Terra", "valor": 16.00},
    {"codigo": 72, "nome": "O Retrato de Dorian Gray", "valor": 17.00},
    {"codigo": 73, "nome": "O Conde de Monte Cristo", "valor": 18.00},
    {"codigo": 74, "nome": "Jane Eyre", "valor": 19.00},
    {"codigo": 75, "nome": "O Som e a Fúria", "valor": 20.00},
    {"codigo": 76, "nome": "Grande Sertão: Veredas", "valor": 21.00},
    {"codigo": 77, "nome": "A Insustentável Leveza do Ser", "valor": 22.00},
    {"codigo": 78, "nome": "Admirável Mundo Novo", "valor": 23.00},
    {"codigo": 79, "nome": "O Estrangeiro", "valor": 21.00},
    {"codigo": 80, "nome": "As Vinhas da Ira", "valor": 25.00},
    {"codigo": 81, "nome": "O Sol é para Todos", "valor": 10.00},
    {"codigo": 82, "nome": "Cem Anos de Solidão", "valor": 11.00},
    {"codigo": 83, "nome": "O Nome do Vento", "valor": 12.00},
    {"codigo": 84, "nome": "A Vida Secreta das Abelhas", "valor": 13.00},
    {"codigo": 85, "nome": "A Trégua", "valor": 14.00},
    {"codigo": 86, "nome": "A Biblioteca Invisível", "valor": 15.00},
    {"codigo": 87, "nome": "O Feitiço do Tempo", "valor": 16.00},
    {"codigo": 88, "nome": "A Dança dos Dragões", "valor": 17.00},
    {"codigo": 89, "nome": "A Guerra dos Tronos", "valor": 18.00},
    {"codigo": 90, "nome": "O Jogo do Exterminador", "valor": 19.00},
    {"codigo": 91, "nome": "A Torre Negra", "valor": 20.00},
    {"codigo": 92, "nome": "O Último Desejo", "valor": 21.00},
    {"codigo": 93, "nome": "O Silmarillion", "valor": 22.00},
    {"codigo": 94, "nome": "O Nome da Rosa", "valor": 23.00},
    {"codigo": 95, "nome": "A Dama das Camélias", "valor": 24.00},
    {"codigo": 96, "nome": "O Morro dos Ventos Uivantes", "valor": 25.00},
    {"codigo": 97, "nome": "A Montanha Mágica", "valor": 10.00},
    {"codigo": 98, "nome": "O Grande Gatsby", "valor": 11.00},
    {"codigo": 99, "nome": "O Lobo das Estepes", "valor": 12.00},
    {"codigo": 100, "nome": "Cem Anos de Solidão", "valor": 13.00}  
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
    for compra in compras:
        total += compra['total']
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.separador(120,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')


def imprime_compra_fechada(compra,total,desconto):
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
        pr.imprimir ('Desconto aplicado', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('- R$', str(round(desconto, 2)), tamanho=12, alinhar='fim', cor_texto='vermelho negrito')
    
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
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
    pr.separador(110,cor_texto='ciano')
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
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=90,alinhar='fim',end='╣')

    return input().lower()

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
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif(opcao == 'e'):
            tela = 'encerar'
        elif('p' in opcao):
            compras.append({'itens':compra, 'total':total, 'data': datetime.now()})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                compra.append(novo_produto(produto,1))
            except ValueError:
                erro = 'A opção selecionada não existe no sistema'

def calcula_total_desconto(compra):
    total = 0
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])
    
    desconto = 0
    
    if total >= 100:
        desconto = total * 0.1
        total *= 0.9
    else:
        for codigo in set([item['codigo'] for item in compra]):
            quantidade_codigo = sum([item['quantidade'] for item in compra if item['codigo'] == codigo])
            if quantidade_codigo > 1:
                desconto += (produto_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
                total-= desconto
    
    return total, desconto

menu()




