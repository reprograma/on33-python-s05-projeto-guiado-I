import print_reprograma as pr #aqui você está falando pro programa usar essa biblioteca - nesse caso ficou uma biblioteca local
from datetime import datetime #aqui você está dando um comando para usar o datetime que é uma função interna do Python

#Aqui foi criada uma lista de produtos que será usada nesse programa, ela foi criada com itens que são dicionários
produtos = [
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

#Essa funcao se refere à variável "produtos", criada na linha 5 que tem a lista dos produtos
#Ela se chama obtem_produto_pelo_codigo e espera receber como parâmetro alguma coisa (no caso um produto). 
#Dentro dessa função temos um for (estrutura de repetição) que vai percorrer a lista daqueles produtos. Essa função diz que, se o valor que eu digitar na variável opção for um código que está dentro desse dicionário, essa função vai fazer ele me retornar um "produto". 
#Essa função está sendo chamada lá embaixo (clicar com o command ou ctrl pra ver), e onde chama ela definse-se que produto = resultado da função.
def obtem_produto_pelo_codigo(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto

#Essa função vai inserir um produto da lista produtos na lista de compras. Ela é chamada lá embaixo e quando você a chama você pede que ela pegue aquele produto que foi obtido na função anterior, e retorne todos os dados dele que estão na lista "produtos".
def novo_produto(produto, quantidade):
    return {
        'codigo':produto['codigo'],
        'nome':produto['nome'],
        'valor':produto['valor'],
        'quantidade':quantidade
    }

#Essa função imprime o fechamento do caixa na tela e precisa receber um parâmetro, aqui deinido como "compra". Os primeiros argumentos são meramente estéticos para fazer com que a listagem fique esteticamente agradável na tela.
#Depois das formatações, você define uma variável dentro dessa função, chamada total. Essa variável inicia em 0. Dentro da função foi inserido um for que percorre cada compra que vai ficar dentro da listas "compras", em cada uma delas eu vou acessar o valor "total" e somar à variável total (ex: se a primeira compra tiver o total de 10 reais, eu somo 0 (valor inicial da variável) +10 (valor da primeira compra analisada). Para a próxima compra na lista, a mesma coisa, acho ela, pego o total dela e somo ao total que eu tenho, até fechar todos os itens da lista "compras".
#É chamada na tela "encerrar"
def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')  
    total = 0
    total_desconto = 0 #inicializando com 0 
    for compra in compras:
        total += compra['total']
        total_desconto += compra["desconto"] #acumula o desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir("R$",str(round(compra['total'],2)),tamanho=20,alinhar='fim')

    pr.separador(120,caracter='-')

    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')

    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')

    #imprime total de desconto
    pr.imprimir('Total de descontos aplicados', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('- R$',str(round(total_desconto, 2)), tamanho=20, alinhar='fim', cor_texto= 'vermelho negrito')

#Essa função precisa receber dois parâmetros, sendo 01 referente à compra e um referente ao total. Ela também começa com uma variável total dentro dela, que inicia com valor zerado (total_compra).
#Dentro dessa função foi inserido um for que vai percorrer cada produto que estiver dentro da compra (ex: livro 1, livro 2, livro 3 etc.) e vai chamar a função "imprimir_produto" para cada produto da lista. Além disso essa função aqui vai atualizar o valor da compra em curso, pegando a variável total_compra (iniciada em 0) e adicionando a ela o resultado do valor do produto vezes a quantidade daquele produto.
def imprime_compra_fechada(compra, total, desconto):
    total_compra = 0
    pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
    pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')
    for produto in compra:
        imprimir_produto(produto)
        total_compra += produto["valor"] * produto["quantidade"]
    pr.separador(120,caracter='-')
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    
    #imprimir valor do desconto
    if desconto > 0:
        pr.imprimir("Desconto aplicado", tamanho=107, alinhar="fim", end="|")
        pr.imprimir('- R$', str(round(desconto, 2)), tamanho=12, alinhar='fim', cor_texto='vermelho negrito')
        # total_compra -= desconto
    
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim',cor_texto='verde negrito')

    
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

#Essa função abaixo imprime os dados da compra na tela. No caso, essa função é chamada lá embaixo quando a opção digitada é n. Ela também possui uma variável total, que inicia em valor 0.
#Dentro dela temos um if/else que verifica se já tenho algum item inserido ou não. Se (if) eu tiver compra maior que 0, ele atualiza a variável "total" adicionando a ela o resultado do valor do produto pela quantidade. A diferença dessa função para a de cima, é que essa aqui imprime na tela conforme você vai colocando os itens, a de cima é chamada quando você der o comando de fechar a compra.
#Depois de atualizar o total, essa função chama a função "imprimir_produto" para que o item apareça listado na tela.
#Caso nenhum item tenha sido adicionado à lista de compras (else) ele imprime na tela os dizeres "Sem itens na lista ainda"

def imprime_compra(compra):
    if(len(compra) > 0):
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')   
        for produto in compra:
            total += produto['valor'] * produto['quantidade']
            imprimir_produto(produto)
        pr.separador(120,caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim')

    else:
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')

    pr.pular_linha()
    pr.pular_linha()

#Essa função abaixo tem como objetivo imprimir as informações detalhadas do produto na tela. Ela está sendo chamada em outras funções (compra fechada e compra), para que quando forem dados os comandos possamos visualizar os produtos na tela, formatados como abaixo.
# Basicamente ela acessa a informação que vai estar lá na lista "produtos" (que vai ter que ser chamada nas listas compra ou compra_fechada) e imprime na tela as informações de código, nome, quantidade, valor e de quantidade vezes o valor.
def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

#Essa função imprimie o cabeçalho
def imprimir_cabecalho(erro): #definindo essa funcao aqui quando chamarmos ela, ela vai imprimir o cabecalho
    pr.limpar()
    pr.retangulo("{reprograma}\nProjeto Guiado 1\nTerminal de Vendas", sv=1, tamanho=100, margem=10, cor_texto="azul negrito", cor_barra="magenta")
    pr.separador(120, cor_texto="ciano")
    
    if(erro != ""): #essa linha verifica se o argumento é diferente de uma string vazia, o programa entende como erro
        pr.imprimir(erro, tamanho=120, alinhar="centro", cor_texto="vermelho negrito")
        pr.separador(120, cor_texto="ciano")

    erro = ""

#Essa função imprime o menu de ajuda na tela, ela será chamada abaixo quando for digitada a opção h.
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

#Essa função imprime o rodapé, indicando as opções H e Q. Essa função também espera um input, porém trata as entradas do usuário para que o que ele digite fique em minúsculo (input().lower()) dessa forma não corre-se o risco que o usuário digite em maiúsculo e seja um comando inválido mesmo que esteja listado nas opções do menu ajuda.
def imprimir_rodape_e_recebe_opcao_input():
    pr.imprimir("[H] Ajuda", "[Q] Sair ", caracter="=", tamanho=120, alinhar="fim", end="╣")

    return input().lower() # lower converte a string para letras minúsculas


#Essa parte é como se fosse o coração do código, porque é ela que chama as funções e testa o que foi chamado. A última linha do código chama essa função (menu()).
#Abaixo ela será comentada linha a linha.
def menu():
    opcao = "" #aqui criamos "opcao" como uma variável e definimos que ela será uma uma string vazia (só com aspas), ela espera que o usuário digite uma opção (H, Q, ou as do menu de ajuda ou até mesmo entradas inválidas)
    erro = "" #Essa variável erro será chamada na função imprimir cabeçalho.
    tela = "" #O programa inicia com a variável "tela"vazia. O valor dessa variável vai mudar conforme a gente digitar um valor no cabeçalho (lá no input que deixa tudo minúsculo), aí quando eu digito um valor, o código pega aquela letrinha e vê se ela corresponde a algum "comando" ou não, se sim, ele faz algo
    compra = [] #Essa variável será equivalente à compra de um cliente apenas, a compra em curso. Ela é criada esperando uma lista.
    compras = [] #Essa variável aqui é uma lista de todas as compras feitas no dia (vários clientes).
    while(opcao != "q"): #Acima apenas declaramos as variáveis. Aqui colocamos um while que vai dar um comando para o programa de que ele vai ficar repetindo tudo o que estiver aqui dentro, até que o usuário digite "q", indicando que ele quer sair do sistema.
       imprimir_cabecalho(erro) #enquanto o usuário não digitar "q" o sistema volta a imprimir o cabeçalho.
       if(tela == ""): # Se a variável "tela" estiver vazia, o programa vai apenas pular 4 linhas só pra ficar esteticamente bonito (é a tela que vemos assim que executamos o programa)
           pr.pular_linha(quantidade=4)  

       elif(tela == "ajuda"): #se a variável tela tiver o valor "ajuda", o programa chama a função "imprimir_ajuda" e exibe na tela as opções de comando
            imprimir_ajuda()
            tela = ""

       elif(tela == "compra"): #se a variável tela tiver o valor "compra", o programa chama a função "imprime_compra" que te mostra se tem algum item na lista ou deixa você adicionar itens e te mostra o subtotal.
           imprime_compra(compra)
       
       elif(tela == "fechar"): #se a variável tela tiver o valor "fechar", o programa chama a função "imprime_compra_fechada" que corresponde à compra que o usuário fez,  mas indica o total que o usuário terá que pagar.
           total, desconto = calcula_total_desconto(compra)
           imprime_compra_fechada(compra, total, desconto)
           
       elif(tela == "encerrar"):  # Se a tela atual for a tela de encerrar o caixa
            imprime_fechamento_caixa(compras)  # Chamamos a função 'imprime_fechamento_caixa' para imprimir o fechamento do caixa
            compras = []  # Limpamos a lista de compras fechadas
            tela = ""  # Definimos a tela atual como vazia (retorna para a tela inicial)
            pr.pular_linha(quantidade=2)  # Pulamos 2 linhas

       opcao =  imprimir_rodape_e_recebe_opcao_input() #Aqui o programa determina que o valor da variável opção vai vir do que o usuário digitar no rodapé, porque ele define que "opção é igual à função que imprime o rodapé e aguarda o input"sempre vai imprimir o rodapé na tela e como ele espera um input ele fica aguardando o usuário digitar algo na tela"
       #aqui "fechou o ciclo de if e elif ali de cima"

       if(opcao == "h"): #aqui, se o valor da variável "opção" for h ele atribui à variável tela o valor "ajuda" que vai rodar o if lá de cima
           tela = "ajuda"

       elif(opcao == "n"): #n atribui à tela o valor compra
           tela = "compra"

       elif(opcao == "f"): #f atribui à tela o valor fechar e também chama a função calcula_total_desconto
            total = calcula_total_desconto(compra)
            tela = 'fechar'

       elif(opcao == "e"):  #e atribui à tela o valor "encerrar"
            tela = 'encerrar'

       elif('p' in opcao): #p é o comando de confirmação que a compra foi paga
            compras.append({'itens': compra, 'total': total, 'data': datetime.now(), "desconto": desconto})
            compra = []
            tela = ""

       else:
            try:
                codigo = int(opcao)
                produto = obtem_produto_pelo_codigo(codigo)
                if produto != None:
                    compra.append(novo_produto(produto,1))
                    quantidade = 1
                else:
                    print("ERRO! PRODUTO NÃO CADASTRADO. DIGITE UM CÓDIGO VÁLIDO")
                    opcao = input("Pressione enter para continuar.")

            except ValueError:
                erro = 'A opção selecionada não existe no sistema'

def calcula_total_desconto(compra):
    total = 0 #a função inicia o total em 0
    desconto = 0 #a função inicia o desconto em 0

    for produto in compra: #aqui é estabelecido um for que define que para todos os produtos listados em compra
        total += (produto["valor"] * produto["quantidade"]) # o total é igual ao valor do produto vezes a quantidade do produto, com isso, ao final da lista temos um valor total daquela compra
    
    if total >= 100: #caso o total da compra seja maior que 100
        desconto = total * 0.1 #você determina um desconto total de 10% 
        total *= 0.9 #e o valor total da compra será de 0.9 o valor inicial    POSSO COLOCAR ESSA LINHA NO FINAL E APLICAR QUE O TOTAL É IGUAL TOTAL MENOS O DESCONTO? 

    else: #caso o total da compra não seja maior que 100
        total = 0 #aqui ele inicia o total em 0 novamente porque ele será calculado
        
        quantidade_produto_por_codigo = {} #crio uma variável que vai verificar se tenho códigos repetidos nos produtos da compra, essa variável é um dicionário

        for produto in compra: #então, se a minha compra não deu mais que 100 reais para cada produto na compra eu vou ver se
            if produto["codigo"] in quantidade_produto_por_codigo: #já tem esse código do produto nessa lista (que começou vazia)?
                quantidade_produto_por_codigo[produto["codigo"]] += produto["quantidade"] #eu somo 1 à quantidade que eu já tinha
                total += (produto["valor"] * produto["quantidade"]*0.5)
                desconto +=  (produto["valor"] * produto["quantidade"]*0.5)
            else: #se eu já tenho aquele produto na lista que eu criei para verificar a quantidade
                quantidade_produto_por_codigo[produto["codigo"]] = produto["quantidade"] #se não tem, conte 1 para aquele produto
                total += (produto["valor"] * produto["quantidade"]) 


    #     for codigo in set([item['codigo']) for item in compra]):
    #                 quantidade_codigo = sum([item['quantidade'] for item in compra if item ['codigo'] == codigo])
    #     if quantidade_codigo > 1:
    #             desconto += (obtem_produto_pelo_codigo(codigo)['valor'] * (quantidade_codigo - 1)) * 0.5
    #             total -= desconto

    # return total, desconto

    return total, desconto
    







        #regra para aplicar desconto - PROVAVELMENTE É AQUI QUE VAMOS APLICAR OS DESCONTOS, QUE ACREDITO QUE SEJA SÓ COLOCAR QUE SE O TOTAL FOR MAIOR QUE 100 DÁ 10% DE DESCONTO, OU SE A QUANTIDADE DE UM ITEM FOR MAIOR QUE 1 ELE RECEBE UM DESCONTO DE  50% SOBRE O SEGUNDO PRODUTO


menu()