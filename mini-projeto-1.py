# Mini Projeto 1: Sistema de Cadastro Básico
# Este projeto demonstra como coletar dados do usuário e exibi-los formatados

# O que o programa deve fazer:
# 1. Perguntar o nome do usuário
# 2. Perguntar a comida favorita do usuário
# 3. Perguntar a cidade onde o usuário mora
# 4. No final, imprimir uma ficha de cadastro completa com todos os dados coletados

# Exibe uma mensagem de boas-vindas
print('\n--- Bem-vindo ao nosso sistema de cadastro ---')

# Coleta informações do usuário usando input() e armazena em variáveis
nome_usuario = input('Digite seu nome: ')
comida_favorita = input('Digite sua comida favorita: ')
cidade_usuario = input('Digite a cidade onde você mora: ')

# Exibe a ficha de cadastro formatada com os dados coletados
print('\n--- Sua ficha de cadastro ---')
print(f'Nome: {nome_usuario}')
print(f'Comida favorita: {comida_favorita}')
print(f'Cidade: {cidade_usuario}')