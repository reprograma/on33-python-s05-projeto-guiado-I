# Exercício de Sala 🏫  

## Observações aluna:

- O código estava crashando quando abríamos o sistema para comprar e era digitado um código não válido.
- Para corrigir esse ponto, dentro do else no menu, no try, foi implementado um teste com
>>> try:
                codigo = int(opcao)
                produto = obtem_produto_pelo_codigo(codigo)
                if produto != None:
                    compra.append(novo_produto(produto,1))
                    quantidade = 1
                else:
                    print("ERRO! PRODUTO NÃO CADASTRADO. DIGITE UM CÓDIGO VÁLIDO")
                    opcao = input("Pressione enter para continuar.")
- Com isso o programa exibe na tela que o código é inexistente e permite que o usuário digite enter e continue adicionando produtos na lista.
- A opção pode não ser a melhor, mas permite que o programa siga, sem quebrar.

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
