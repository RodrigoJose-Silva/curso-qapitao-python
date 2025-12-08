# O que o seu programa deve fazer:
# Perguntar o nome do usuário.
# Perguntar a comida favorita do usuário.
# Perguntar a cidade onde o usuário mora.
# No final, imprimir uma ficha de cadastro completa com todos os dados coletados.

print('\n--- Bem-vindo ao nosso sistema de cadastro ---')
nome_usuario = input('Digite seu nome: ')
comida_favorita = input('Digite sua comida favorita: ')
cidade_usuario = input('Digite a cidade onde você mora: ')

print('\n--- Sua ficha de cadastro ---')
print(f'Nome: {nome_usuario}')
print(f'Comida favorita: {comida_favorita}')
print(f'Cidade: {cidade_usuario}')