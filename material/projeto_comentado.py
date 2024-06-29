import print_reprograma as pr  # Importa o módulo 'print_reprograma' e o renomeia como 'pr' para facilitar o uso.
from datetime import datetime  # Importa a biblioteca 'datetime' para trabalhar com datas e horas.

produtos = [  # Define uma lista de dicionários chamada 'produtos'
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

def produto_codigo(codigo): # Define a função produto_codigo que recebe um código como argumento
    for produto in produtos: # Itera sobre a lista produtos
        if produto['codigo'] == codigo: # Verifica se o código do produto é igual ao código passado como argumento
            return produto # Retorna o produto se o código corresponder
    # Se o código não for encontrado na lista produtos, retorna None
    return None

def novo_produto(produto, quantidade): # Define a função novo_produto que recebe um produto e uma quantidade como argumentos
    return { # Retorna um novo dicionário com as informações do produto e a quantidade
        'codigo':produto['codigo'], # O código do novo produto é o mesmo do produto recebido como argumento
        'nome':produto['nome'], # O nome do novo produto é o mesmo do produto recebido como argumento
        'valor':produto['valor'], # O valor do novo produto é o mesmo do produto recebido como argumento
        'quantidade':quantidade # A quantidade do novo produto é a quantidade recebida como argumento
    }


def imprime_compra(compra): # Define a função imprime_compra que recebe uma lista de compras como argumento
    if(len(compra) > 0): # Verifica se a lista de compras não está vazia
        total = 0 # Inicializa a variável total com 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|') # Imprime o cabeçalho da tabela com a coluna 'codigo'
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|') # Imprime o cabeçalho da tabela com a coluna 'produto'
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|') # Imprime o cabeçalho da tabela com a coluna 'qtd'
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|') # Imprime o cabeçalho da tabela com a coluna 'valor un.'
        pr.imprimir('valor', tamanho=12, alinhar='centro')   # Imprime o cabeçalho da tabela com a coluna 'valor'
        for produto in compra: # Itera sobre cada produto na lista de compras
            total += produto['valor'] * produto['quantidade'] # Calcula o valor total do produto e adiciona ao total da compra
            imprimir_produto(produto) # Chama a função imprimir_produto para imprimir as informações do produto
        pr.separador(120,caracter='-') # Imprime uma linha separadora
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|') # Imprime o subtotal da compra
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim') # Imprime o valor do subtotal da compra
    else: # Se a lista de compras estiver vazia
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center') # Imprime uma mensagem informando que a lista de compras está vazia
    pr.pular_linha() # Imprime uma linha em branco
    pr.pular_linha() # Imprime uma linha em branco

def imprimir_produto(produto): # Define a função imprimir_produto que recebe um produto como argumento
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|') # Imprime o código do produto
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|') # Imprime o nome do produto
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|') # Imprime a quantidade do produto
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|') # Imprime o valor unitário do produto
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim') # Imprime o valor total do produto


#imprimir cabeçalho
def imprimir_cabecalho(erro): # Define a função imprimir_cabecalho que recebe um erro como argumento
    pr.limpar() # Limpa a tela do terminal
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=100, margem=5, cor_texto='azul negrito', cor_barra='magenta') # Imprime o cabeçalho do programa
    pr.separador(108, cor_texto='ciano') # Imprime uma linha separadora
    if(erro != ''): # Verifica se há um erro a ser exibido
        pr.imprimir(erro, tamanho =100, alinhar='centro', cor_texto='vermelho negrito') # Imprime a mensagem de erro
        pr.separador(108, cor_texto='ciano') # Imprime uma linha separadora
    erro = '' # Reseta a variável erro para uma string vazia

def imprimir_ajuda(): # Define a função imprimir_ajuda que imprime a tela de ajuda do programa
    pr.pular_linha(quantidade=2) # Imprime duas linhas em branco
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando H
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando Q
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando N
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando F
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando P
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando nnn
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando Xnn
    pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=108) # Imprime a mensagem de ajuda para o comando E
    pr.pular_linha(quantidade=2) # Imprime duas linhas em branco


#imprimir rodape
def imprimir_rodape(): # Define a função imprimir_rodape que imprime o rodapé do programa
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='=', tamanho=105, alinhar='fim', end='╣') # Imprime o rodapé do programa

    return input().lower() # Retorna a opção digitada pelo usuário em letras minúsculas

def menu(): # Define a função menu que controla o fluxo do programa
    opcao = '' # Inicializa a variável opcao com uma string vazia
    erro = '' # Inicializa a variável erro com uma string vazia
    tela = '' # Inicializa a variável tela com uma string vazia
    compra = [] # Inicializa a lista compra com uma lista vazia
    while(opcao != 'q'): # Inicia um loop while que continua a executar enquanto a variável opcao for diferente de 'q'
        imprimir_cabecalho(erro) # Chama a função imprimir_cabecalho para imprimir o cabeçalho e, se houver erro, imprime a mensagem de erro
        if(tela == ''): # Verifica se a variável tela está vazia
            pr.pular_linha(quantidade=4) # Se a variável tela estiver vazia, imprime quatro linhas em branco
        elif(tela == 'ajuda'): # Verifica se a variável tela é igual a 'ajuda'
            imprimir_ajuda() # Se a variável tela for igual a 'ajuda', chama a função imprimir_ajuda para imprimir a tela de ajuda
            tela = '' # Reseta a variável tela para uma string vazia
        elif(tela == 'compra'): # Verifica se a variável tela é igual a 'compra'
            imprime_compra(compra) # Se a variável tela for igual a 'compra', chama a função imprime_compra para imprimir a lista de compras
        opcao = imprimir_rodape() # Chama a função imprimir_rodape para imprimir o rodapé e obter a opção digitada pelo usuário. A opção digitada é armazenada na variável opcao
        if(opcao == 'h'): # Verifica se a opção digitada pelo usuário é 'h'
            tela = 'ajuda' # Se a opção digitada pelo usuário for 'h', define a variável tela como 'ajuda'
        elif(opcao == 'n'): # Verifica se a opção digitada pelo usuário é 'n'
            tela = 'compra' # Se a opção digitada pelo usuário for 'n', define a variável tela como 'compra'
        else: # Se a opção digitada pelo usuário não for 'h' ou 'n'
            try: # Tenta converter a opção para um inteiro
                codigo = int(opcao) # Converte a opção para um inteiro
                produto = produto_codigo(codigo) # Chama a função produto_codigo para obter o produto correspondente
                compra.append(novo_produto(produto,1)) # Adiciona o produto à lista compra
                quantidade = 1 # Reseta a variável quantidade para 1
            except ValueError: # Se a conversão para inteiro falhar
                erro = 'A opção selecionada não existe no sistema' # Define a variável erro com uma mensagem de erro


menu()      # Chama a função menu para iniciar a execução do programa