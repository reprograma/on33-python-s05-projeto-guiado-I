# 🛒🛍️ Projeto Guiado I - Terminal de Vendas (PDV)

## 📚 Descrição da Atividade

Exercicio da semana 05 para casa. Fazer um terminal de vendas (PDV), o pdv é responsavel por adicionar todos os produtos em uma compra e depois mostrar tudo o que foi vendido, adicionando tambem valor de porcentagem de cada pedido.

## 📋 Passo a Passo

## Cria uma lista de produtos com 100 itens:

            produtos = [
                {'codigo': 1, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 1', 'valor': 10.00},
                {'codigo': 2, 'nome': 'Introdução à Computação para Alunos Inteligentes - Volume 2', 'valor': 10.00},
                {'codigo': 3, 'nome': 'Linguagens de Programação Web para Alunos Inteligentes', 'valor': 10.00},
                {'codigo': 4, 'nome': 'Tecnologias de Scripting para Alunos Inteligentes', 'valor': 10.00},
                {'codigo': 5, 'nome': 'Desenvolvimento Web com SQL para Alunos Inteligentes', 'valor': 15.00},
                ...
                {'codigo': 99, 'nome': 'Direito Internacional para Alunos Inteligentes', 'valor': 15.00},
                {'codigo': 100, 'nome': 'Direito Ambiental para Alunos Inteligentes', 'valor': 15.00},
            ]

## Cria uma funcao para retorna o produto com o código especificado:

            def produto_codigo(codigo):
                for produto in produtos:
                    if produto['codigo'] == codigo:
                        return produto

## Cria uma funcao para cria um novo produto para a compra, com a quantidade especificada:

            def novo_produto(produto, quantidade):
                return {
                    'codigo':produto['codigo'],
                    'nome':produto['nome'],
                    'valor':produto['valor'],
                    'quantidade':quantidade
                }

## Cria uma funcao para imprimir o fechamento do caixa na tela:

            def imprimir_fechamento_caixa(compras):
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

## Cria uma funcao para mostrar o total na compra ao final:

            def imprimir_compra_fechada(compra,total):
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
                pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
                pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim',cor_texto='black negrito')
                pr.limpar_formatacao()
                pr.pular_linha()
                pr.pular_linha()

## Cria uma funcao para imprimir detalhes da compra:

            def imprimir_compra(compra):
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

## Cria uma funcao para imprimir produtos add na compra:

            def imprimir_produto(produto):
                pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
                pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
                pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
                pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
                pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')    

## Cria uma funcao para imprimir um cabecalho:

            def imprimir_cabecalho(erro):
                pr.limpar()
                pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='black negrito',cor_barra='amarelo negrito')
                pr.separador(120,cor_texto='ciano')
                if(erro != ''):
                    pr.imprimir(erro,tamanho=120,alinhar='centro',cor_texto='black negrito')
                    pr.separador(120,cor_texto='ciano')
                erro = ''

## Cria uma funcao para imprimir um sumario de ajuda na tela:

            def imprimir_ajuda():
                pr.pular_linha(quantidade=2)
                pr.imprimir('[A]   >> Ajuda com o Sistema',alinhar='centro',tamanho=120)
                pr.imprimir('[S]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=120)
                pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=120)
                pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=120)
                pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=120)
                pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=120)
                pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=120)
                pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=120)
                pr.pular_linha(quantidade=2)

## Cria uma funcao para imprimir rodape:

            def imprimir_rodape():
                pr.imprimir('[A] Ajuda ','[S] Sair ',caracter='═',tamanho=115,alinhar='fim',end='╣')

                return input().lower()

## Cria uma funcao para acessar o menu, que encerra o meu programa caso eu digite 'm' ou continua rodando caso eu digite qq outra letra:

            def menu():
                opcao = ''
                erro = ''
                tela = ''
                compra = []
                compras = []
                while(opcao != 'm'):
                    imprimir_cabecalho(erro)
                    if(tela == ''):
                        pr.pular_linha(quantidade=4)
                    elif(tela == 'ajuda'):
                        imprimir_ajuda()
                        tela=''
                    elif(tela == 'compra'):
                        imprimir_compra(compra)    
                    elif(tela == 'fechar'):
                        imprimir_compra_fechada(compra,total)
                    elif(tela == 'encerar'):
                        imprimir_fechamento_caixa(compras)
                        compras = []
                        tela=''
                        pr.pular_linha(quantidade=2)
                    opcao = imprimir_rodape()
                    if(opcao == 'a'):
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

## Cria uma funcao que calcula o total do desconto com base no valor na compra:

            def calcula_total_desconto(compra):
                total = 0
                for produto in compra:
                    total += (produto['valor'] * produto['quantidade'])
                    if total >= 100:
                        total *=0.9
                    
                return total # Retorna o total da compra com desconto!

## chamei minha funcao menu para iniciar meu programa!

            menu()   

## 👩🏻‍🏫 Profa. Camila Ribeiro Pinto.
Professora [Camila Ribeiro](https://github.com/camisarp " Camila Ribeiro")