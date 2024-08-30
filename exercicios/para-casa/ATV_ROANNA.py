##Aplicação um desconto ao produto, atualizando as informações no dicionário do produto.
def aplica_desconto(produto, desconto):
    valor_desconto = produto['preco'] * (desconto / 100)
    preco_final = produto['preco'] - valor_desconto
    
    produto_atualizado = {
        'nome': produto['nome'],
        'preco_original': produto['preco'],
        'desconto_percentual': desconto,
        'valor_desconto': valor_desconto,
        'preco_final': preco_final
    }
    
    return produto_atualizado

###Cálculo o total de descontos aplicados em todas as compras.
def calcula_desconto_total(compras):
    total_desconto = 0.0
    
    for compra in compras:
        if 'valor_desconto' in compra:
            total_desconto += compra['valor_desconto']
    
    return total_desconto
### Imprimindo um resumo detalhado das compras, incluindo os descontos aplicados e o total de descontos do dia.
def imprime_fechamento_caixa(compras):
    print("\n--- Fechamento de Caixa ---")
    
    total_desconto = calcula_desconto_total(compras)
    
    # Imprime os detalhes de cada compra
    for compra in compras:
        nome = compra['nome']
        preco_original = compra.get('preco_original', compra['preco'])
        preco_final = compra.get('preco_final', preco_original)
        desconto = compra.get('valor_desconto', 0.0)
        
        print(f"Produto: {nome}")
        print(f"Preço Original: R$ {preco_original:.2f}")
        if desconto > 0:
            print(f"Desconto Aplicado: R$ {desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")
        print("-" * 30)
    
    # Imprime o valor total do desconto aplicado
    print(f"\nTotal de Desconto Aplicado: R$ {total_desconto:.2f}")
    print("-------------------------------")

###Interface principal para interação com o usuário.
#  Oferece opções para adicionar produtos, visualizar a lista de compras,
#  calcula o total de descontos, imprimi o fechamento de caixa, e sai do programa.
def menu():
    lista_compras = []
    
    while True:
        print("\nMenu de Compras:")
        print("1. Adicionar produto")
        print("2. Ver lista de compras")
        print("3. Ver total de desconto aplicado")
        print("4. Imprimir fechamento de caixa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome_produto = input("Digite o nome do produto: ")
            preco_produto = float(input("Digite o preço do produto: R$ "))
            
            produto = {'nome': nome_produto, 'preco': preco_produto}
            
            tem_desconto = input("Deseja adicionar um desconto ao produto? (s/n): ").lower()
            if tem_desconto == 's':
                desconto = float(input("Digite a porcentagem de desconto (0-100): "))
                if 0 <= desconto <= 100:
                    produto = aplica_desconto(produto, desconto)
                else:
                    print("Desconto inválido. O produto será adicionado sem desconto.")
            
            lista_compras.append(produto)
            print(f"Produto {produto['nome']} adicionado à lista de compras.")
        
        elif escolha == '2':
            if not lista_compras:
                print("Sua lista de compras está vazia.")
            else:
                print("\nLista de Compras:")
                for item in lista_compras:
                    print(item)
        
        elif escolha == '3':
            total_desconto = calcula_desconto_total(lista_compras)
            print(f"O valor total de descontos aplicados é: R$ {total_desconto:.2f}")
        
        elif escolha == '4':
            imprime_fechamento_caixa(lista_compras)
        
        elif escolha == '5':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
