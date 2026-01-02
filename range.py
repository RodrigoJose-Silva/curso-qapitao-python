# Este programa demonstra o uso da função range() com loops for
# A função range() gera uma sequência de números, muito útil para loops

# range(5) gera números de 0 até 4 (5 números no total)
# Quando range tem um único argumento, começa em 0 e vai até (argumento - 1)
for numero in range(5):
    # Exibe cada número gerado: 0, 1, 2, 3, 4
    print(numero)

# Exibe uma linha em branco para separar os resultados
print('\n')

# range(1, 10) gera números de 1 até 9 (não inclui o 10)
# Quando range tem dois argumentos: início (1) e fim (10, não incluso)
for numero in range(1, 10):
    # Exibe cada número gerado: 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(numero)