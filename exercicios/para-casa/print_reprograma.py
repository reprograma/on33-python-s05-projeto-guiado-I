# Lista de produtos disponíveis
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
    {'codigo': 100, 'nome': 'Direito Ambiental', 'valor': 15.00}
]

# Função para calcular desconto para compras acima de R$ 100
def calcular_desconto_total(valor_total):
    if valor_total > 100:
        desconto = valor_total * 0.1  # 10% de desconto
        return desconto
    else:
        return 0

# Função para aplicar desconto para combos
def calcular_desconto_combo(carrinho):
    desconto_total = 0
    tipos = set()
    
    # Identificar quantidades de cada tipo de produto
    for item in carrinho:
        tipo = item['tipo']
        quantidade = item['quantidade']
        tipos.add(tipo)
        
    # Aplicar desconto para combos
    for tipo in tipos:
        quantidade_total = sum(item['quantidade'] for item in carrinho if item['tipo'] == tipo)
        if quantidade_total > 1:
            for item in carrinho:
                if item['tipo'] == tipo:
                    item['desconto'] = item['preco'] * 0.5  # 50% de desconto no segundo item em diante
                    desconto_total += item['desconto']
    
    return desconto_total

# Função para exibir o catálogo de produtos
def exibir_catalogo(produtos):
    print("\n=== Catálogo de Produtos ===")
    print("Código | Nome do Produto | Valor")
    for produto in produtos:
        print(f"{produto['codigo']} - {produto['nome']} - R$ {produto['valor']:.2f}")

# Função principal para o sistema de vendas
def main():
    carrinho = []
    total = 0
    
    while True:
        exibir_catalogo(produtos)
        
        print("\nOpções:")
        print("1 - Adicionar produto ao carrinho")
        print("2 - Finalizar compra")
        print("3 - Cancelar item da compra")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Digite o código do produto: "))
            produto_selecionado = next((produto for produto in produtos if produto['codigo'] == codigo), None)
            if produto_selecionado:
                quantidade = int(input("Digite a quantidade desejada: "))
                
                item = {
                    'codigo': codigo,
                    'nome': produto_selecionado['nome'],
                    'quantidade': quantidade,
                    'preco': produto_selecionado['valor'],
                    'tipo': 'livro',  # considerando todos os produtos como tipo 'livro' para exemplo
                    'desconto': 0
                }
                
                carrinho.append(item)
                print("Produto adicionado ao carrinho!")
            else:
                print("Código de produto inválido.")
        
        elif opcao == '2':
            # Calcular o total da compra
            total = sum(item['quantidade'] * item['preco'] - item['desconto'] for item in carrinho)
            
            # Aplicar descontos
            desconto_total = calcular_desconto_total(total)
            desconto_combo = calcular_desconto_combo(carrinho)
            
            total -= desconto_total
            total -= desconto_combo
            
            print(f"\nTotal da compra: R$ {total:.2f}")
            print("Compra finalizada!")
            break
        
        elif opcao == '3':
            # Cancelar item da compra
            print("\n=== Cancelar Item da Compra ===")
            for i, item in enumerate(carrinho):
                print(f"{i + 1} - Código: {item['codigo']}, Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: R$ {item['preco']:.2f}")
            
            if carrinho:
                cancelar = input("Digite o número do item que deseja cancelar ou 0 para cancelar tudo: ")
                if cancelar != '0':
                    try:
                        index = int(cancelar) - 1
                        if 0 <= index < len(carrinho):
                            del carrinho[index]
                            print("Item removido do carrinho!")
                        else:
                            print("Número do item inválido.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
            else:
                print("Não há itens no carrinho para cancelar.")
        
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o programa principal
if __name__ == "__main__":
    main()
