import print_reprograma as pr
from datetime import datetime

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

def produto_codigo(codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

def novo_produto (produto, quantidade):
    return{
        "codigo":produto["codigo"],
        "nome":produto["nome"],
        "valor":produto["valor"],
        "quantidade":quantidade
    }

def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro')
    total = 0
    total_desconto = 0 #inicializando com 0
    for compra in compras:
        total += compra['total']
        total_desconto+= compra["desconto"] #acumular desconto de cada compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "),tamanho=89,end='|',alinhar='fim')
        pr.imprimir(str(len(compra['itens'])),tamanho=9,end='|',alinhar='centro')
        pr.imprimir('R$',str(round(compra['total'],2)),tamanho=20,alinhar='fim')
    pr.separador(120,caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(total, 2)), tamanho=20, alinhar='fim')

    #imprime total de desconto
    pr.imprimir('Total de desconto aplicado', tamanho=99, alinhar='fim', end='|')
    pr.imprimir(' - R$',str(round(total, 2)), tamanho=20, alinhar='fim', cor_texto= "vermelhor negrito")


def imprime_compra_fechada(compra, total, desconto):
    """Imprime a compra fechada, mostrando o total e o total a pagar."""
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
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim', cor_texto='vermelhor negrito')
    
    #imprimir valor do desconto
    if desconto >0:
        pr.imprimir("Desconto aplicado", tamanho=107, alinha="fim", end="|")
        pr.imprimir('- R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim', cor_texto='vermelhor negrito')
     
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

def imprime_compra(compra):
    """Imprime uma compra mockada."""
    if len(compra) > 0:
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')
        for produto in compra:
            total += produto['valor'] * produto ['quantidade']
            imprimir_produto(produto)
        pr.separador(120, caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim')
    else:        
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')
        pr.pular_linha()
        pr.pular_linha()
       
def imprimir_produto(produto):
    """Imprime um produto da compra."""
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

#imprimir cabeçalho
def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo("{reprograma}\nProjeto Guiado 1\nTerminal de Vendas", 
                 sv=1, tamanho=100, margem=4, cor_texto="azul negrito",cor_barra="magenta"
                 )
    pr.separador(110, cor_texto="ciano")
   
    if(erro != ""): #essa linha verifica se o argumento é diferente de uma string vazia, o programa entende o erro
        pr.imprimir(erro, tamanho =120, alinhar="centro",cor_texto="Vermelho negrito")
        pr.separador(100, cor_texto="ciano")
    erro=""
    opcao = imprimir_rodape()

#imprimir ajuda 
def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o sistema',alinhar='centro', tamanho=108)
    pr.imprimir('[Q]   >> Sair da Tela ou sistema',alinhar='centro', tamanho=108)
    pr.imprimir('[N]   >> Criar uma Nova Compra',alinhar='centro', tamanho=108)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro', tamanho=108)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro', tamanho=108)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro', tamanho=108)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro', tamanho=108)
    pr.imprimir('[C]   >> Cancela item de compra',alinhar='centro', tamanho=108)
    pr.imprimir('[E]   >> Encerra caixa',alinhar='centro', tamanho=108)
    pr.pular_linha(quantidade=2)

#imprimir rodapé
def imprimir_rodape():
    pr.imprimir("[H] Ajuda", "[Q] Sair",caracter= "=" , tamanho=105, alinhar="fim", end="⁞")

    return input().lower()

#imprimir produto
def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

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
        elif(tela == "compra"):
            imprime_compra("compra")
        elif tela == "fechar":
            total, desconto = calculo_total_desconto(compra)
            imprime_compra_fechada (compra, total, desconto)
        elif tela== "encerar":
            imprime_fechamento_caixa(compras)
            compras = []
            tela = "" 
            pr.pular_linha(quantidade=2)
        opcao = imprimir_rodape()
        if opcao =='h':
            tela = "ajuda"
        elif opcao == "n":
            tela = "codigo"
        elif opcao == "f":
            total = calculo_total_desconto(compra)
            tela = "fechar"
        elif opcao == "e":
            tela = "encerar"
        elif "p" in opcao:
            compras.append ({"itens": compra, "total": total, "data": datetime.now(),"desconto": desconto})
            compra = []
            tela = ""
        else:
            try: 
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                compra.append(novo_produto(produto,1))
                quantidade = 1
            except ValueError:
                erro = "A opção selecionada não existe no sistema"
            except TypeError:
                 erro = "O código do produto não existe"

def calculo_total_desconto(compra):
        total = 0
        for produto in compra:
            total += (produto["valor"] * produto["quantidade"])
        
        desconto = 0
        
        if total >=100:
            desconto =total *0.1 #Calcula o valor do desconto
            total*= 0.9 #Multiplicando o total por 0.9
        else:
            #verificar descontos para combos
            for codigo in set([item["codigo"]for item in compra]):
                quantidade_codigo = sum([item["quantidade"] for item in compra if item["codigo"] == codigo])
            if quantidade_codigo > 1:
                desconto += (produto_codigo(codigo)["valor"] * (quantidade_codigo - 1)) *0.5



        return total, desconto

def remover_item(compra, codigo):
    compra[:] = [item for item in compra if item["codigo"] != codigo]
    return compra

menu()