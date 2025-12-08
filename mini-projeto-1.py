# O que o seu programa deve fazer:
# Perguntar o nome do usuário.
# Perguntar a comida favorita do usuário.
# Perguntar a cidade onde o usuário mora.
# No final, imprimir uma ficha de cadastro completa com todos os dados coletados.

nome_usuario = input('Digite seu nome: ')
comida_favorita = input('Digite sua comida favorita: ')
cidade_usuario = input('Digite a cidade onde você mora: ')

print('\n--- Sua ficha de cadastro ---')
print(f'O nome do usuário é {nome_usuario}.')
print(f'A cidade que que o {nome_usuario} mora é {cidade_usuario}.')
print(f'A comida favorita do {nome_usuario} é {comida_favorita}.')