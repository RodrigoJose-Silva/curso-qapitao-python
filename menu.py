
while True:
    print("Menu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        print("Você escolheu a Opção 1 \n")
    elif escolha == '2':
        print("Você escolheu a Opção 2 \n")
    elif escolha == '3':
        print("Saindo do menu...")
        break
    else:
        print("Opção inválida, tente novamente. \n")