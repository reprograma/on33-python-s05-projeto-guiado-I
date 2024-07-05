# Exercício de Sala 🏫  

## Observações aluna:

### Crash quando digitava código inexistente
- O código estava quebrando quando abríamos o sistema para comprar (n) e era digitado um código não válido (fora de 0 a 100).
- Para corrigir esse ponto, dentro do else no menu que chama a tela de compra, implementado um teste nas linhas 302 a 311: 
       else:
            try:
                codigo = int(opcao)
                produto = obtem_produto_pelo_codigo(codigo)
                if produto != None:
                    compra.append(novo_produto(produto,1))
                    quantidade = 1
                else:
                    pr.imprimir("ERRO! PRODUTO NÃO CADASTRADO. DIGITE UM CÓDIGO VÁLIDO", cor_texto= "amarelo negrito")
                    opcao = input("Pressione enter para continuar.")
- Com isso o programa exibe na tela que o código é inexistente e permite que o usuário digite enter e continue adicionando produtos na lista.

### Implementações Exercícios:

1. Aplicado desconto de 10% para compras que ultrapassem R$ 100,00.
2. Aplicado desconto para itens repetidos, a partir do segundo item
    OBS: não foi utilizada a função set para isso, conforme sugerido pela professora em aula, mas implementado um teste dentro de um novo for
3. Implementada a impressão do desconto de cada compra na tela de fechamento, para facilitar ao caixa verificar o desconto por compra

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [X] Fiz o fork do repositório.
- [X] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [X] Resolvi o exercício.
- [X] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [X] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [X] Pushei os commits na minha branch (`git push origin nome-da-branch`)
