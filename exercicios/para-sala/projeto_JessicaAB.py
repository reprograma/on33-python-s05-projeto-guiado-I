# Criar pasta __init__.py na pasta de origem do arquivo 
#Após isso é possivel usar a biblioteca contida dentro da pasta material
import sys
sys.path.append('material')
import print_reprograma as pr
from datetime import datetime


# Nossa loja tem vários produtos:
produtos = [
    {'codigo': 1, 'nome': 'Introdução à Computação - Volume 1', 'valor': 10.00},
    {'codigo': 2, 'nome': 'Introdução à Computação - Volume 2', 'valor': 10.00},
    {'codigo': 3, 'nome': 'Linguagens de Programação Web', 'valor': 10.00},
    {'codigo': 4, 'nome': 'Tecnologias de Scripting', 'valor': 10.00},
    {'codigo': 5, 'nome': 'Desenvolvimento Web com SQL', 'valor': 15.00},
    {'codigo': 6, 'nome': 'Desenvolvimento Web com C++', 'valor': 15.00},
    {'codigo': 7, 'nome': 'Desenvolvimento Web com Java', 'valor': 15.00},
    {'codigo': 8, 'nome': 'Desenvolvimento Web com .Net', 'valor': 15.00},
    {'codigo': 9, 'nome': 'Hardware e Redes de Computadores - Volume 1', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Hardware e Redes de Computadores - Volume 2', 'valor': 15.00},
    {'codigo': 11, 'nome': 'Hardware e Redes de Computadores - Volume 3', 'valor': 15.00},
    {'codigo': 12, 'nome': 'Hardware e Redes de Computadores - Volume 4', 'valor': 15.00},
    {'codigo': 13, 'nome': 'Dominando o Inglês', 'valor': 5.00},
    {'codigo': 14, 'nome': 'Comunicação Empresarial', 'valor': 10.00},
    {'codigo': 15, 'nome': 'Desenvolvimento Pessoal - Livro 1', 'valor': 15.00},
    {'codigo': 16, 'nome': 'Desenvolvimento Pessoal - Livro 2', 'valor': 15.00},
    {'codigo': 17, 'nome': 'Introdução à Computação - Volume 1', 'valor': 10.00},
    {'codigo': 18, 'nome': 'Introdução à Computação - Volume 2', 'valor': 10.00},
    {'codigo': 19, 'nome': 'Fundamentos da Programação', 'valor': 12.00},
    {'codigo': 20, 'nome': 'Algoritmos e Estruturas de Dados', 'valor': 15.00},
    {'codigo': 21, 'nome': 'Introdução à Engenharia de Software', 'valor': 18.00},
    {'codigo': 22, 'nome': 'Banco de Dados', 'valor': 12.00},
    {'codigo': 23, 'nome': 'Programação Web com Python', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Programação Web com JavaScript', 'valor': 15.00},
    {'codigo': 25, 'nome': 'Introdução à Ciência da Computação', 'valor': 18.00},
    {'codigo': 26, 'nome': 'Inteligência Artificial', 'valor': 20.00},
    {'codigo': 27, 'nome': 'Redes de Computadores', 'valor': 15.00},
    {'codigo': 28, 'nome': 'Segurança da Informação', 'valor': 18.00},
    {'codigo': 29, 'nome': 'Administração de Sistemas', 'valor': 15.00},
    {'codigo': 30, 'nome': 'Gestão de Projetos de TI', 'valor': 12.00},
    {'codigo': 31, 'nome': 'Introdução à Estatística', 'valor': 10.00},
    {'codigo': 32, 'nome': 'Probabilidade', 'valor': 10.00},
    {'codigo': 33, 'nome': 'Matemática Discreta', 'valor': 12.00},
    {'codigo': 34, 'nome': 'Cálculo', 'valor': 15.00},
    {'codigo': 35, 'nome': 'Álgebra Linear', 'valor': 12.00},
    {'codigo': 36, 'nome': 'Geometria Analítica', 'valor': 10.00},
    {'codigo': 37, 'nome': 'Física', 'valor': 15.00},
    {'codigo': 38, 'nome': 'Química', 'valor': 12.00},
    {'codigo': 39, 'nome': 'Biologia', 'valor': 10.00},
    {'codigo': 40, 'nome': 'História', 'valor': 10.00},
    {'codigo': 41, 'nome': 'Geografia', 'valor': 10.00},
    {'codigo': 42, 'nome': 'Sociologia', 'valor': 12.00},
    {'codigo': 43, 'nome': 'Filosofia', 'valor': 10.00},
    {'codigo': 44, 'nome': 'Literatura Brasileira', 'valor': 10.00},
    {'codigo': 45, 'nome': 'Literatura Portuguesa', 'valor': 10.00},
    {'codigo': 46, 'nome': 'Literatura Inglesa', 'valor': 10.00},
    {'codigo': 47, 'nome': 'Literatura Espanhola', 'valor': 10.00},
    {'codigo': 48, 'nome': 'Literatura Francesa', 'valor': 10.00},
    {'codigo': 49, 'nome': 'Literatura Alemã', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Literatura Italiana', 'valor': 10.00},
    {'codigo': 51, 'nome': 'Literatura Russa', 'valor': 10.00},
    {'codigo': 52, 'nome': 'Literatura Japonesa', 'valor': 10.00},
    {'codigo': 53, 'nome': 'Literatura Chinesa', 'valor': 10.00},
    {'codigo': 54, 'nome': 'Arte', 'valor': 10.00},
    {'codigo': 55, 'nome': 'Música', 'valor': 10.00},
    {'codigo': 56, 'nome': 'Cinema', 'valor': 10.00},
    {'codigo': 57, 'nome': 'Teatro', 'valor': 10.00},
    {'codigo': 58, 'nome': 'Dança', 'valor': 10.00},
    {'codigo': 59, 'nome': 'Fotografia', 'valor': 10.00},
    {'codigo': 60, 'nome': 'Direito', 'valor': 15.00},
    {'codigo': 61, 'nome': 'Economia', 'valor': 12.00},
    {'codigo': 62, 'nome': 'Administração', 'valor': 10.00},
    {'codigo': 63, 'nome': 'Contabilidade', 'valor': 12.00},
    {'codigo': 64, 'nome': 'Marketing', 'valor': 10.00},
    {'codigo': 65, 'nome': 'Publicidade e Propaganda', 'valor': 10.00},
    {'codigo': 66, 'nome': 'Recursos Humanos', 'valor': 10.00},
    {'codigo': 67, 'nome': 'Relações Públicas', 'valor': 10.00},
    {'codigo': 68, 'nome': 'Comunicação', 'valor': 10.00},
    {'codigo': 69, 'nome': 'Jornalismo', 'valor': 12.00},
    {'codigo': 70, 'nome': 'Psicologia', 'valor': 10.00},
    {'codigo': 71, 'nome': 'Sociologia', 'valor': 10.00},
    {'codigo': 72, 'nome': 'Antropologia', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Ciência Política', 'valor': 10.00},
    {'codigo': 74, 'nome': 'História da Arte', 'valor': 10.00},
    {'codigo': 75, 'nome': 'História da Música', 'valor': 10.00},
    {'codigo': 76, 'nome': 'História do Cinema', 'valor': 10.00},
    {'codigo': 77, 'nome': 'História do Teatro', 'valor': 10.00},
    {'codigo': 78, 'nome': 'História da Dança', 'valor': 10.00},
    {'codigo': 79, 'nome': 'História da Fotografia', 'valor': 10.00},
    {'codigo': 80, 'nome': 'Filosofia da Arte', 'valor': 10.00},
    {'codigo': 81, 'nome': 'Filosofia da Música', 'valor': 10.00},
    {'codigo': 82, 'nome': 'Filosofia do Cinema', 'valor': 10.00},
    {'codigo': 83, 'nome': 'Filosofia do Teatro', 'valor': 10.00},
    {'codigo': 84, 'nome': 'Filosofia da Dança', 'valor': 10.00},
    {'codigo': 85, 'nome': 'Filosofia da Fotografia', 'valor': 10.00},
    {'codigo': 86, 'nome': 'Ética', 'valor': 10.00},
    {'codigo': 87, 'nome': 'Ética Profissional', 'valor': 10.00},
    {'codigo': 88, 'nome': 'Ética e Responsabilidade Social', 'valor': 10.00},
    {'codigo': 89, 'nome': 'Lógica', 'valor': 10.00},
    {'codigo': 90, 'nome': 'Pensamento Crítico', 'valor': 10.00},
    {'codigo': 91, 'nome': 'Introdução ao Direito', 'valor': 15.00},
    {'codigo': 92, 'nome': 'Direito Constitucional', 'valor': 15.00},
    {'codigo': 93, 'nome': 'Direito Civil', 'valor': 15.00},
    {'codigo': 94, 'nome': 'Direito Penal', 'valor': 15.00},
    {'codigo': 95, 'nome': 'Direito Processual', 'valor': 15.00},
    {'codigo': 96, 'nome': 'Direito do Trabalho', 'valor': 15.00},
    {'codigo': 97, 'nome': 'Direito Tributário', 'valor': 15.00},
    {'codigo': 98, 'nome': 'Direito Empresarial', 'valor': 15.00},
    {'codigo': 99, 'nome': 'Direito Internacional', 'valor': 15.00},
    {'codigo': 100, 'nome': 'Direito Ambiental', 'valor': 15.00},
]

# Esta função procura um produto pelo código que você digitar.
def produto_codigo(codigo):  
    for produto in produtos:  
        if produto['codigo'] == codigo:  
            return produto  

# Esta função cria um novo item para a sua compra.
def novo_produto(produto, quantidade):
    return {  
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade 
    }

# Esta função imprime um resumo de todas as compras do dia.
def imprime_fechamento_caixa(compras):  
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|') 
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')  
    pr.imprimir('valor', tamanho=20, alinhar='centro')  
    total = 0
   
    for compra in compras:  
        total += compra['total']  
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim') 
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')  
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')  
    pr.separador(120, caracter='-') 
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')  
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')

# Esta função imprime uma compra fechada, mostrando todos os itens e o total a pagar.
def imprime_compra_fechada(compra, total):
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')  
    pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')  
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')  
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')  
    pr.imprimir('valor', tamanho=12, alinhar='centro')  
    
    for produto in compra:
        imprimir_produto(produto)
        total_compra += produto['valor'] * produto['quantidade']
    
    total_compra = calcula_total_desconto(compra)
    
    pr.separador(120, caracter='-')  
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')  
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito')
    pr.limpar_formatacao()  
    pr.pular_linha()
    pr.pular_linha()

# Esta função mostra os produtos que você adicionou à sua compra.
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

# Esta função imprime as informações de um produto, como código, nome, quantidade e valor.
def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

# Esta função imprime o cabeçalho do nosso sistema de vendas.
def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=100, margem=10, cor_texto='azul negrito', cor_barra='magenta')
    pr.separador(120, cor_texto='ciano')
    # Se houver uma mensagem de erro
    if erro != '':
        pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(120, cor_texto='ciano')
    erro = ''

# Esta função mostra as opções de ajuda do sistema.
def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[H]'
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[Q]'
    pr.imprimir('[N]   >> Cria uma Nova Compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[F]   >> Fechar a Compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[P]   >> Confirmar que a compra foi paga', alinhar='centro', tamanho=120)  
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado', alinhar='centro', tamanho=120)  
    pr.imprimir('[E]   >> Encerar caixa', alinhar='centro', tamanho=120)  
    pr.pular_linha(quantidade=2)

# Esta função imprime o rodapé do sistema, com as opções de ajuda e sair.
def imprimir_rodape():
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=115, alinhar='fim', end='╣')
    return input().lower()

# Esta é a função principal do nosso programa, onde o menu de vendas é exibido.
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
            imprime_compra_fechada(compra, total)  
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
            compras.append({'itens': compra, 'total': total, 'data': datetime.now()}) 
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

def calcula_total_desconto(compra):  # Esta função recebe a compra como entrada
    # Inicializamos a variável 'total'
    total = 0
    lista_codigos = []
    for produto in compra: 
        lista_codigos.append(produto['codigo'])
    for produto in compra:  # Para cada produto na lista de produtos
        contagem_produto = 0
        for cod in lista_codigos:
            if produto['codigo'] == cod :
                contagem_produto += 1
        if contagem_produto > 1:
            total += (produto['valor'] + produto['valor'] * 0.5 * (produto['quantidade'] - 1))
        else:
            total += (produto['valor'] produto['quantidade']  )  # Somamos o valor total do produto ao total da compra
    # Aplicamos a regra de desconto (implemente aqui a lógica para aplicar desconto)
    # ...        return total
    if total > 100:
        total *= 0.9
    # Retornamos o total da compra com desconto
    return total


# Chamamos a função 'menu' para iniciar o programa
menu()
# Esta função calcula o total da compra, aplicando um desconto se necessário.
