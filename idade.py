# Este programa demonstra o uso de estruturas condicionais (if/else)
# Estruturas condicionais permitem que o programa tome decisões baseadas em condições

# Solicita a idade do usuário (input sempre retorna string)
idade = input('Digite sua idade: ')

# A estrutura if verifica uma condição
# int(idade) converte a string para número inteiro para fazer a comparação
# >= verifica se a idade é maior ou igual a 18
if int(idade) >= 18:
    # Este bloco executa se a condição for verdadeira
    print(f'Você tem {idade} anos, é maior de idade!')
else:
    # Este bloco executa se a condição for falsa
    print(f'Você tem {idade} anos, é menor de idade!')