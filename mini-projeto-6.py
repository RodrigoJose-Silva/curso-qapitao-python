# Mini Projeto 6: Sistema de Cálculo de Frete
# Este projeto demonstra como criar funções que realizam cálculos e retornam valores
# A função encapsula a lógica de cálculo, tornando o código mais organizado e reutilizável

# Define uma função para calcular o valor total do produto com frete
# A função recebe dois parâmetros: valor do produto e peso em quilos
def calcular_total(valor_produto, peso_kg):
    # Calcula o valor do frete: R$ 10,00 por quilo
    valor_frete = peso_kg * 10
    
    # Calcula o total somando o valor do produto com o frete
    total = valor_produto + valor_frete
    
    # Retorna o valor total calculado
    return total

# Exibe o cabeçalho do sistema
print("**** Sistema de Logistica ****")

# Solicita ao usuário o valor do produto
# float() converte a entrada para número decimal (pode ter casas decimais)
v_prod = float(input("Digite o valor do produto: R$ "))

# Solicita ao usuário o peso do produto em quilos
peso = float(input("Digite o peso do produto em kg: "))

# Chama a função calcular_total passando os valores informados
# O resultado é armazenado na variável valor_final
valor_final = calcular_total(v_prod, peso)

# Exibe o resultado formatado com 2 casas decimais
# :.2f formata o número com exatamente 2 casas decimais
print(f"O valor total do produto com frete é: R$ {valor_final:.2f}")