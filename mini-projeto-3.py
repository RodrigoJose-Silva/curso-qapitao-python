# Mini Projeto 3: Sistema de Lista de Convidados e Tabuada
# Este projeto demonstra o uso de listas, loops for e a função range()

# Criando uma lista com nomes de convidados
lista_de_convidados = ['Joãozin', 'Mariazinha', 'Pedrinho', 'Gersonin']

# Exibe mensagem de início da festa
print("--- Iniciando a festa! ---")

# Loop para percorrer cada convidado na lista de convidados
# O loop executa uma vez para cada item da lista
for nome in lista_de_convidados:
    # Exibe uma mensagem personalizada para cada convidado
    print(f'Olá, {nome}! Seja bem-vindo(a) a festa!')

# Exibe mensagem de fim da festa
print("--- Fim da festa! ---")

# Exibe uma linha em branco para separar as seções
print('\n')

# Exibe cabeçalho da tabuada
print("--- Tabuada do 5 ---")

# Loop para imprimir a tabuada do 5
# range(1, 11) gera números de 1 até 10
for i in range(1, 11):
    # Exibe cada multiplicação: 5 x 1 = 5, 5 x 2 = 10, etc.
    print(f'5 x {i} = {5 * i}')

