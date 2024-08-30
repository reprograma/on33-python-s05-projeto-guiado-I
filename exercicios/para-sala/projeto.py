import sys
sys.path.append('material')
import print_reprograma as pr
#imprimir cabeçalho
def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=100, margem=5, cor_texto='azul negrito', cor_barra='magenta')
    pr.separador(108, cor_texto='ciano')
    if(erro != ''):
        pr.imprimir(erro, tamanho =100, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(108, cor_texto='ciano')
    erro = ''
#imprimir rodape
def imprimir_rodape():
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='=', tamanho=105, alinhar='fim', end='╣')
    return input().lower()
def menu():
    opcao = ''
    erro = ''
    while(opcao != 'q'):
        imprimir_cabecalho(erro)
        opcao = imprimir_rodape()
        if(opcao != 'q'):
            erro = 'A opção selecionada não existe no sistema'

menu()