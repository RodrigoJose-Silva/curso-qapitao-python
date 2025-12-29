print('--- Sistema de Cadastro de Usuário (v2)---')

# Inicializa o dicionário de cadastro vazio
cadastro = {}

# Coleta informações do usuário e armazena no dicionário
cadastro['nome'] = input('Digite seu nome: ')
cadastro['comida'] = input('Digite sua comida favorita: ')
cadastro['cidade'] = input('Digite sua cidade: ')

print('\n' + '=' * 30)
print('--- Dados Cadastrados ---')
print('=' * 30)
# Exibe os dados cadastrados
for chave, valor in cadastro.items():
    print(f"{chave.capitalize()}: {valor}")
    # capitalize() deixa a primeira letra maiúscula
print('\nSistema encerrado.')
