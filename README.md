<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Projeto Guiado I

Turma Online 33 | Semana 5 | 2024 | Professora [Camila Ribeiro](https://github.com/camisarp " Camila Ribeiro")

## Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* Abra o VSCode e na pasta Projeto abra o arquivo main

## Antes da Aula
Antes de começar a codar vamos dar uma olhada no modulo [print_reprograma](https://github.com/reprograma/on33-python-s05-projeto-guiado-I/tree/main/material "print_reprograma")

## O que vamos fazer
Nessa aula vamos fazer um terminal de vendas (PDV), o pdv é responsavel por adicionar todos os produtos em uma compra e depois mostrar tudo o que foi vendido

Para isso vamos por partes

### Resumo
O que veremos na aula de hoje?
* [P01/Imprimir Cabeçalho](#P01)
* [P02/Imprimir Rodapé](#P02)
* [P03/Sair do Sistema](#P03)
* [P04/Tratar erro](#P04)
* [P05/Imprimir Ajuda](#P05)
* [P06/Nova Compra](#P06)
* [P07/Imprimir Compra Mocada](#P07)
* [P08/Adicionar Produto](#P08)
* [P09/Fechar Compra](#P09)
* [P10/Encerar Caixa](#P10)
* [P11/Mudar Quantidade](#P11)

## Conteúdo

### P01 

Vamos começar imprimindo o cabeçalho, bem leve

```python
import print_reprograma as pr

def imprimir_cabecalho():
  """Imprime o cabeçalho do PDV."""
  pr.limpar()  # Limpa a tela do terminal
  pr.retangulo(
      '{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',
      sv=1,
      tamanho=100,
      margem=10,
      cor_texto='azul negrito',
      cor_barra='magenta'
  )
  pr.separador(120, cor_texto='ciano')

# Chama a função para imprimir o cabeçalho
imprimir_cabecalho()
```

**Explicação:**

1. **Importar `print_reprograma`:**
   * `import print_reprograma as pr`: Importa o módulo `print_reprograma` e o renomeia como `pr` para facilitar o uso.
2. **Definir a função `imprimir_cabecalho()`:**
   * `def imprimir_cabecalho():`: Define uma função chamada `imprimir_cabecalho`.
   * `"""Imprime o cabeçalho do PDV."""`:  Documentação da função, explicando sua finalidade.
3. **Chamar funções do `print_reprograma`:**
   * `pr.limpar()`:  Chama a função `limpar()` do módulo `print_reprograma` para limpar a tela do terminal.
   * `pr.retangulo(...)`:  Chama a função `retangulo()` para imprimir um retângulo com o texto do cabeçalho. Veja as opções de personalização:
      * `sv=1`:  Define se o texto deve ser centralizado (1) ou alinhado à esquerda (0).
      * `tamanho=100`:  Define a largura do retângulo.
      * `margem=10`:  Define a margem em torno do texto.
      * `cor_texto='azul negrito'`:  Define a cor e o estilo do texto.
      * `cor_barra='magenta'`:  Define a cor da barra do retângulo.
   * `pr.separador(120, cor_texto='ciano')`: Chama a função `separador()` para imprimir uma linha separadora com a cor `ciano`.
4. **Chamar a função `imprimir_cabecalho()`:**
   * `imprimir_cabecalho()`: Chama a função `imprimir_cabecalho` para executar o código dentro dela e imprimir o cabeçalho.

**Observações:**

* Você pode personalizar o cabeçalho da forma que desejar, alterando o texto, as cores, o tamanho e a margem.
* O módulo `print_reprograma` oferece diversas funções para formatar e organizar a saída no terminal. Explore as funções disponíveis na documentação do módulo.

**Lembre-se:** 
* Certifique-se de que o módulo `print_reprograma` esteja instalado no seu ambiente Python. Se não estiver, use o comando `pip install print-reprograma` no terminal.
* Você pode usar a função `imprimir_cabecalho()` em outros pontos do seu código para exibir o cabeçalho sempre que necessário.

### P02


Nesse ponto vamos imprimir o rodapé e tambem vamos pegar o caracter do comando

```python
import print_reprograma as pr

# ... (código do cabeçalho) ...

def imprimir_rodape():
    """Imprime o rodapé do PDV e retorna a opção do usuário."""
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=115, alinhar='fim', end='╣')
    return input().lower()

# ... (restante do código) ...
```

**Explicação:**

1. **Importar `print_reprograma`:**
   * `import print_reprograma as pr`: Importa o módulo `print_reprograma` e o renomeia como `pr` para facilitar o uso.

2. **Chamar `pr.imprimir()` para o rodapé:**
   * `pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=115, alinhar='fim', end='╣')`:  Chama a função `imprimir()` do módulo `print_reprograma` para imprimir o rodapé com as seguintes opções:
      * `'[H] Ajuda '`: O texto que será exibido à esquerda.
      * `'[Q] Sair '`: O texto que será exibido à direita.
      * `caracter='═'`: O caractere que será usado para criar a linha do rodapé.
      * `tamanho=115`: A largura da linha do rodapé.
      * `alinhar='fim'`: Alinha os textos à direita.
      * `end='╣'`: Define o caractere que será usado para finalizar a linha do rodapé.

3. **Obter a opção do usuário:**
   * `opcao = input().lower()`: Solicita ao usuário que digite uma opção e converte a entrada para letras minúsculas.

4. **Exibir a opção digitada:**
   * `pr.imprimir(opcao)`: Imprime a opção digitada pelo usuário usando a função `imprimir()`.

**Observações:**

* Você pode personalizar o rodapé da forma que desejar, alterando o texto, os caracteres, a largura e o alinhamento.
* O módulo `print_reprograma` oferece diversas funções para formatar e organizar a saída no terminal. Explore as funções disponíveis na documentação do módulo.

### P03


Nesse parte vamos montar o sistema em si, ele não vai parar até que o comando seja 'q'

```python
import print_reprograma as pr

# ... (funções imprimir_cabecalho() e imprimir_rodape() - já definidas) ...

def menu():
  """Exibe o menu principal do PDV."""
  opcao = ''
  while opcao != 'q':
    imprimir_cabecalho()
    opcao = imprimir_rodape()

menu()
```

**Explicação:**

1. **Funções `imprimir_cabecalho()` e `imprimir_rodape()`:** Essas funções já foram definidas anteriormente, e você pode reutilizá-las aqui.

2. **Função `menu()`:**
   * `def menu():`: Define a função `menu`, que representa o menu principal do PDV.
   * `opcao = ''`: Inicializa a variável `opcao` com um valor vazio.
   * `while opcao != 'q':`: Inicia um loop `while` que continua a executar enquanto `opcao` for diferente de 'q'.
      * `imprimir_cabecalho()`: Chama a função `imprimir_cabecalho()` para exibir o cabeçalho do PDV.
      * `opcao = imprimir_rodape()`: Chama a função `imprimir_rodape()` para exibir o rodapé e obter a opção digitada pelo usuário. A opção digitada é armazenada na variável `opcao`.
   * `menu()`: Chama a função `menu()` para iniciar a execução do menu principal.

**Como funciona:**

* O loop `while` continua a executar até que o usuário digite `q` (ou `Q`) e pressione Enter.
* A cada iteração do loop:
    * O cabeçalho do PDV é exibido.
    * O rodapé do PDV é exibido, solicitando ao usuário que escolha uma opção.
    * A opção digitada pelo usuário é armazenada na variável `opcao`.
    * Se `opcao` for igual a `q`, o loop é encerrado e o programa termina.

### P04


Um ponto principal de todos os sistemas é tratar o erro

```python
import print_reprograma as pr

# ... (funções imprimir_cabecalho(), imprimir_rodape() - já definidas) ...

def menu():
    """Exibe o menu principal do PDV."""
    opcao = ''
    erro = ''  # Inicializa a variável erro com uma string vazia
    while opcao != 'q':
        imprimir_cabecalho()
        if erro != '':  # Verifica se há algum erro a ser exibido
            pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
            pr.separador(120, cor_texto='ciano')
        erro = ''  # Reseta a variável erro para uma string vazia
        opcao = imprimir_rodape()

menu()
```

**Explicação:**

1. **Variável `erro`:**
   * `erro = ''`: Inicializa uma variável chamada `erro` com uma string vazia. Essa variável será usada para armazenar mensagens de erro que podem ocorrer durante a execução do programa.

2. **Tratamento de Erros no Loop `while`:**
   * `if erro != '':`:  Verifica se a variável `erro` contém algum valor. Se sim, significa que ocorreu um erro e a mensagem de erro deve ser exibida.
     * `pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')`: Exibe a mensagem de erro usando a função `imprimir()` do módulo `print_reprograma`.
     * `pr.separador(120, cor_texto='ciano')`:  Imprime uma linha separadora.
   * `erro = ''`: Reseta a variável `erro` para uma string vazia após exibir a mensagem de erro. Isso garante que a próxima iteração do loop não exiba a mesma mensagem de erro novamente.

### P05

Imprimir a tela de ajuda com todos os comandos disponiveis no sistema

```python
import print_reprograma as pr

# ... (funções imprimir_cabecalho(), imprimir_rodape(), imprimir_ajuda() - já definidas) ...

def menu():
    """Exibe o menu principal do PDV."""
    opcao = ''
    erro = ''
    tela = ''  # Inicializa a variável tela com uma string vazia
    while opcao != 'q':
        imprimir_cabecalho()
        if erro != '':
            pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
            pr.separador(120, cor_texto='ciano')
        erro = ''
        if tela == '':
            pr.pular_linha(quantidade=4)
        elif tela == 'ajuda':
            imprimir_ajuda()
            tela = ''
        opcao = imprimir_rodape()
        if opcao == 'h':
            tela = 'ajuda'
        else:
            erro = 'A opção selecionada não existe no sistema'

menu()
```

**Explicação:**

1. **Variável `tela`:**
   * `tela = ''`: Inicializa uma variável chamada `tela` com uma string vazia. Essa variável será usada para controlar qual tela deve ser exibida (a tela principal do menu ou a tela de ajuda).

2. **Função `imprimir_ajuda()`:**
   * `def imprimir_ajuda():`: Define a função `imprimir_ajuda`, que exibe a tela de ajuda do PDV.
   * A função usa a função `imprimir()` do módulo `print_reprograma` para exibir os comandos disponíveis e informações relevantes.

3. **Gerenciamento de Tela no Loop `while`:**
   * `if tela == '':`: Verifica se a variável `tela` está vazia. Se sim, significa que a tela principal do menu deve ser exibida. 
      * `pr.pular_linha(quantidade=4)`:  Insere um espaço em branco na tela.
   * `elif tela == 'ajuda':`: Verifica se a variável `tela` é igual a 'ajuda'. Se sim, significa que a tela de ajuda deve ser exibida.
      * `imprimir_ajuda()`: Chama a função `imprimir_ajuda()` para exibir a tela de ajuda.
      * `tela = ''`: Reseta a variável `tela` para uma string vazia, retornando para a tela principal do menu.
   * `opcao = imprimir_rodape()`: Chama a função `imprimir_rodape()` para exibir o rodapé e obter a opção digitada pelo usuário.
   * `if opcao == 'h':`: Verifica se a opção digitada pelo usuário é 'h'. Se sim, a tela de ajuda deve ser exibida.
      * `tela = 'ajuda'`: Define a variável `tela` como 'ajuda' para indicar que a próxima iteração do loop deve exibir a tela de ajuda.
   * `else:`: Se a opção digitada pelo usuário não for 'h', é exibido um erro.
      * `erro = 'A opção selecionada não existe no sistema'`: Define a mensagem de erro.

### P06


Fazer o fluxo de nova compra

```python
import print_reprograma as pr

# ... (funções imprimir_cabecalho(), imprimir_rodape(), imprimir_ajuda() - já definidas) ...

def imprimir_compra():
    """Imprime a tela de compra do PDV."""
    pr.pular_linha(quantidade=2)
    pr.imprimir("## Nova Compra ##", cor_texto='ciano negrito')
    pr.imprimir("**Opções:**", cor_texto='amarelo')
    pr.imprimir("- **[A]** - Adicionar produto", cor_texto='verde')
    pr.imprimir("- **[F]** - Fechar Compra", cor_texto='verde')
    pr.imprimir("- **[V]** - Voltar para o menu principal", cor_texto='verde')
    pr.pular_linha(quantidade=2)

def menu():
    """Exibe o menu principal do PDV."""
    opcao = ''
    erro = ''
    tela = ''
    while opcao != 'q':
        imprimir_cabecalho()
        if erro != '':
            pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')
            pr.separador(120, cor_texto='ciano')
        erro = ''
        if tela == '':
            pr.pular_linha(quantidade=4)
        elif tela == 'ajuda':
            imprimir_ajuda()
            tela = ''
        elif tela == 'compra':
            imprimir_compra()
            tela = ''
        opcao = imprimir_rodape()
        if opcao == 'h':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'
        else:
            erro = 'A opção selecionada não existe no sistema'

menu()
```

**Explicação:**

1. **Função `imprimir_compra()`:**
   * `def imprimir_compra():`: Define a função `imprimir_compra`, que exibe a tela de compra do PDV.
   * A função usa a função `imprimir()` do módulo `print_reprograma` para exibir as opções disponíveis para a tela de compra.

2. **Gerenciamento de Tela no Loop `while`:**
   * `elif tela == 'compra':`:  Verifica se a variável `tela` é igual a 'compra'. Se sim, significa que a tela de compra deve ser exibida.
      * `imprimir_compra()`: Chama a função `imprimir_compra()` para exibir a tela de compra.
      * `tela = ''`: Reseta a variável `tela` para uma string vazia, retornando para a tela principal do menu.
   * `elif opcao == 'n':`: Verifica se a opção digitada pelo usuário é 'n'. Se sim, a tela de compra deve ser exibida.
      * `tela = 'compra'`: Define a variável `tela` como 'compra' para indicar que a próxima iteração do loop deve exibir a tela de compra.

### P07


Imprimir compras mocadas (o termo mocado é quando é um valor fixo que vamos usar só para teste)

```python
import print_reprograma as pr
from datetime import datetime

compra_moc = [
    {'codigo': 1, 'nome': 'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 1', 'valor': 10.00, 'quantidade': 1},
    {'codigo': 2, 'nome': 'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 2', 'valor': 10.00, 'quantidade': 2},
    {'codigo': 3, 'nome': 'Book - Web Programming Languages For Smart Students', 'valor': 10.00, 'quantidade': 3}
]

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
            total += produto['valor'] * produto['quantidade']
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

# ... (resto do código) ...
```

**Explicação:**

1. **`compra_moc`:**
   * Uma lista de dicionários que representa uma compra mockada (de exemplo). Cada dicionário representa um produto, com as chaves `codigo`, `nome`, `valor` e `quantidade`.

2. **`imprime_compra(compra)`:**
   * Esta função recebe uma lista de dicionários de produtos (como `compra_moc`) como argumento.
   * **Verifica se a compra está vazia:** Se a lista estiver vazia (`len(compra) > 0`), exibe uma mensagem "Sem itens na lista ainda".
   * **Calcula o total:** Se houver itens na lista, a função itera sobre cada produto, calcula o valor total do produto (`produto['valor'] * produto['quantidade']`) e acumula o total.
   * **Imprime o cabeçalho da compra:**
     * `pr.imprimir('codigo', ...)`: Imprime o cabeçalho da tabela, com colunas para código, nome, quantidade, valor unitário e valor total.
   * **Imprime cada produto:**  Chama a função `imprimir_produto(produto)` para imprimir os detalhes de cada produto da compra.
   * **Imprime o subtotal:**  Exibe o subtotal da compra.

3. **`imprimir_produto(produto)`:**
   * Esta função recebe um dicionário que representa um produto e imprime os seus detalhes na tabela.

**Como usar:**

1. **Chame a função `imprime_compra()`:** 
   * Para exibir a compra mockada, chame a função `imprime_compra(compra_moc)`.

**Exemplo de uso:**

```python
# ... (resto do código) ...
def menu():
  # ... (código do menu) ...
  elif tela == 'compra_mockada':  # Adicione uma nova opção 'compra_mockada' ao menu
    imprime_compra(compra_moc)  # Exiba a compra mockada
    tela = ''
  # ... (resto do código) ...
```

### P08


Adicionar um novo produto dinamicamente na lista de compra

```python
import print_reprograma as pr
from datetime import datetime

produtos = [
    # ... (Lista de produtos - já definida) ...
]

def produto_codigo(codigo):
    """Retorna o produto com o código especificado."""
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None  # Retorna None se o produto não for encontrado

def novo_produto(produto, quantidade):
    """Cria um novo produto para a compra, com a quantidade especificada."""
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
    }

# ... (resto do código) ...

def menu():
    """Exibe o menu principal do PDV."""
    opcao = ''
    erro = ''
    tela = ''
    compra = []
    while opcao != 'q':
        imprimir_cabecalho(erro)
        if tela == '':
            pr.pular_linha(quantidade=4)
        elif tela == 'ajuda':
            imprimir_ajuda()
            tela = ''
        elif tela == 'compra':
            imprime_compra(compra)
        opcao = imprimir_rodape()
        if opcao == 'h':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                if produto:
                    compra.append(novo_produto(produto, 1))
                else:
                    erro = 'Produto não encontrado.'
            except ValueError:
                erro = 'A opção selecionada não existe no sistema'

menu()
```

**Explicação:**

1. **`produto_codigo(codigo)`:**
   * Busca um produto na lista `produtos` com base no `codigo` fornecido.
   * Se o produto for encontrado, a função retorna o dicionário do produto.
   * Se o produto não for encontrado, a função retorna `None`.

2. **`novo_produto(produto, quantidade)`:**
   * Cria um novo dicionário representando um produto para a compra, incluindo a `quantidade`.

3. **`menu()`:**
   * **Tratamento de entrada:** 
     * Tenta converter a opção digitada pelo usuário para um inteiro (`int(opcao)`).
     * Se a conversão for bem-sucedida, procura o produto com o código correspondente usando `produto_codigo(codigo)`.
     * Se o produto for encontrado, adiciona o produto à `compra` com a quantidade 1.
     * Se o produto não for encontrado, define uma mensagem de erro: `erro = 'Produto não encontrado.'`
     * Se a conversão para inteiro falhar, define uma mensagem de erro: `erro = 'A opção selecionada não existe no sistema'`.

### P09


Fechar a compra e mostrar o total e o total a pagar (o total a pagar é o total com desconto que será calculado mais pra frente)

```python
import print_reprograma as pr
from datetime import datetime

produtos = [
    # ... (Lista de produtos - já definida) ...
]

def produto_codigo(codigo):
    """Retorna o produto com o código especificado."""
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None  # Retorna None se o produto não for encontrado

def novo_produto(produto, quantidade):
    """Cria um novo produto para a compra, com a quantidade especificada."""
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
    }

def imprime_compra_fechada(compra, total):
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
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito')
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

# ... (resto do código) ...

def menu():
    """Exibe o menu principal do PDV."""
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
        opcao = imprimir_rodape()
        if opcao == 'h':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'
        elif opcao == 'f':
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif 'p' in opcao:
            compras.append({'itens': compra, 'total': total, 'data': datetime.now()})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                if produto:
                    compra.append(novo_produto(produto, 1))
                else:
                    erro = 'Produto não encontrado.'
            except ValueError:
                erro = 'A opção selecionada não existe no sistema'

def calcula_total_desconto(compra):
    """Calcula o total da compra com desconto (implemente a regra de desconto aqui)."""
    total = 0
    for produto in compra:
        total += (produto['valor'] * produto['quantidade'])
    # Adicione a lógica para aplicar o desconto aqui. 
    return total

menu()
```

**Explicação das mudanças:**

1. **`imprime_compra_fechada(compra, total)`:**
   * Imprime a compra fechada, mostrando o total e o total a pagar, com o total a pagar em verde e negrito para destacar.
   * Utiliza a função `pr.limpar_formatacao()` para remover a formatação de cores e negrito aplicada ao total a pagar.
   * Imprime a data da compra atual usando `datetime.now()`.

2. **`calcula_total_desconto(compra)`:**
   * Calcula o total da compra, mas você precisa implementar a lógica para aplicar o desconto aqui.
   * Substitua o comentário `# Adicione a lógica para aplicar o desconto aqui.` pela sua regra de desconto (por exemplo, 10% de desconto).

3. **`menu()`:**
   * Adiciona um novo estado `tela = 'fechar'` para exibir a compra fechada.
   * Quando o usuário digita `'f'`, a compra é fechada, o total com desconto é calculado e a tela 'fechar' é exibida.
   * Quando o usuário digita `'p'`, a compra é salva na lista `compras` com a data atual e a tela volta para o menu principal.

### P10

Encerrar o caixa, vamos totalizar todas a comprar mostrando o total que foi vendido naquele caixa

```python
import print_reprograma as pr
from datetime import datetime

produtos = [
    # ... (Lista de produtos - já definida) ...
]

def produto_codigo(codigo):
    """Retorna o produto com o código especificado."""
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None  # Retorna None se o produto não for encontrado

def novo_produto(produto, quantidade):
    """Cria um novo produto para a compra, com a quantidade especificada."""
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
    }

def imprime_fechamento_caixa(compras):
    """Imprime o fechamento do caixa, mostrando todas as compras."""
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

# ... (resto do código) ...

def menu():
    """Exibe o menu principal do PDV."""
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
            pr.pular
```

<p align="center">
Desenvolvido com :purple_heart:  
</p>



