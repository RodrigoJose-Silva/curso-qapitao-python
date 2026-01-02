# Este programa demonstra como criar um menu interativo usando while True
# while True cria um loop infinito que só termina com break

# Loop infinito que continua executando até ser interrompido
while True:
    # Exibe o menu de opções para o usuário
    print("Menu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    # Solicita ao usuário que escolha uma opção
    escolha = input("Escolha uma opção: ")
    
    # Verifica qual opção foi escolhida usando if/elif/else
    if escolha == '1':
        # Se escolheu opção 1, exibe mensagem e continua o loop
        print("Você escolheu a Opção 1 \n")
    elif escolha == '2':
        # Se escolheu opção 2, exibe mensagem e continua o loop
        print("Você escolheu a Opção 2 \n")
    elif escolha == '3':
        # Se escolheu opção 3, exibe mensagem e sai do loop
        print("Saindo do menu...")
        break  # break interrompe o loop while e continua após ele
    else:
        # Se nenhuma opção válida foi escolhida, exibe mensagem de erro
        print("Opção inválida, tente novamente. \n")