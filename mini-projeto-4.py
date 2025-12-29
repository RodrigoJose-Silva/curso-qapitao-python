senha_secreta = "python123"
senha_digitada = "" 

while senha_digitada != senha_secreta:
    print("--- Sistema de Segurança ---")
    senha_digitada = input("Digite a senha secreta: ")

    if senha_digitada == senha_secreta:
        print("Acesso Permitido! Bem-vindo ao sistema.")
    else:
        print("Senha incorreta! Tente novamente.\n")

print("Sistema encerrado.")
