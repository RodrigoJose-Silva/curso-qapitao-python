# Mini Projeto 5: Sistema de Cadastro usando Dicionários
# Este projeto demonstra como usar dicionários para armazenar e exibir dados de forma organizada
# Versão melhorada do Mini Projeto 1, usando dicionário em vez de variáveis separadas

print('--- Sistema de Cadastro de Usuário (v2)---')

# Inicializa o dicionário de cadastro vazio
# Dicionários são ideais para armazenar dados relacionados (chave-valor)
cadastro = {}

# Coleta informações do usuário e armazena diretamente no dicionário
# Cada chave ('nome', 'comida', 'cidade') recebe o valor digitado pelo usuário
cadastro['nome'] = input('Digite seu nome: ')
cadastro['comida'] = input('Digite sua comida favorita: ')
cadastro['cidade'] = input('Digite sua cidade: ')

# Cria uma linha decorativa usando repetição de caractere
print('\n' + '=' * 30)
print('--- Dados Cadastrados ---')
print('=' * 30)

# Exibe os dados cadastrados percorrendo o dicionário
# items() retorna cada par chave-valor do dicionário
for chave, valor in cadastro.items():
    # Exibe cada item: capitalize() transforma a primeira letra em maiúscula
    # Exemplo: 'nome' vira 'Nome', 'comida' vira 'Comida'
    print(f"{chave.capitalize()}: {valor}")

print('\nSistema encerrado.')
