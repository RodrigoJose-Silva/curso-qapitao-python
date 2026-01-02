# Mini Projeto 2: Sistema de Controle de Entrada por Idade
# Este projeto demonstra o uso de estruturas condicionais com múltiplas condições (if/elif/else)

# Regras de negócio do sistema:
# - Se a idade for maior ou igual a 65 → "entrada grátis"
# - Se a idade for maior ou igual a 18 → "paga inteira"
# - Caso contrário (menor que 18) → "não pode entrar"

# Exibe mensagem de boas-vindas
print('--- bem-vindo ao evento --- \n')

# Solicita a idade do usuário
idade = input('Informe a sua idade: ')

# Verifica a idade e aplica as regras usando if/elif/else
# A ordem é importante: primeiro verifica a condição mais específica (65+)
if int(idade) >= 65:
    # Se a idade for 65 ou mais, entrada é grátis
    print('Entrada grátis!')
elif int(idade) >= 18:
    # Se a idade for entre 18 e 64, paga inteira
    print('Paga inteira')
else:
    # Se a idade for menor que 18, não pode entrar
    print('Não pode entrar')