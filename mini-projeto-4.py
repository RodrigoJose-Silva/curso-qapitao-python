# Mini Projeto 4: Sistema de Autenticação com Senha
# Este projeto demonstra o uso de loops while com validação de entrada

# Define a senha correta do sistema
senha_secreta = "python123"

# Inicializa a variável que armazenará a senha digitada pelo usuário
senha_digitada = "" 

# Loop while continua executando enquanto a senha digitada for diferente da senha secreta
# O loop só termina quando o usuário digitar a senha correta
while senha_digitada != senha_secreta:
    # Exibe o cabeçalho do sistema a cada tentativa
    print("--- Sistema de Segurança ---")
    
    # Solicita ao usuário que digite a senha
    senha_digitada = input("Digite a senha secreta: ")

    # Verifica se a senha digitada está correta
    if senha_digitada == senha_secreta:
        # Se a senha estiver correta, exibe mensagem de acesso permitido
        print("Acesso Permitido! Bem-vindo ao sistema.")
    else:
        # Se a senha estiver incorreta, exibe mensagem de erro e continua o loop
        print("Senha incorreta! Tente novamente.\n")

# Esta mensagem é exibida após o usuário digitar a senha correta e o loop terminar
print("Sistema encerrado.")
