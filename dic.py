# Este programa demonstra o uso de dicionários em Python
# Dicionários são estruturas que armazenam pares chave-valor
# Cada valor é associado a uma chave única, facilitando o acesso aos dados

# Criando um dicionário com informações de uma pessoa
# A estrutura é: 'chave': valor
pessoa = {
    'nome': 'João Silva',      # Chave 'nome' com valor 'João Silva'
    'idade': 30,                # Chave 'idade' com valor 30
    'cidade': 'São Paulo',      # Chave 'cidade' com valor 'São Paulo'
    'ative': True               # Chave 'ative' com valor booleano True
}

# Imprime o dicionário completo
print(pessoa)

# Acessa o valor associado à chave 'nome' usando colchetes
print(pessoa['nome'])

# Atualiza o valor da chave 'idade' existente
pessoa['idade'] = 23

# Adiciona uma nova chave-valor ao dicionário
pessoa['profissão'] = 'QA'

# Exibe o dicionário atualizado
print(pessoa)

# Loop for percorre as chaves do dicionário
for chave in pessoa:
    # Exibe cada chave do dicionário
    print(chave)

# Loop for usando items() para acessar chave e valor simultaneamente
# items() retorna cada par chave-valor do dicionário
for chave, valor in pessoa.items():
    # Exibe tanto a chave quanto o valor de cada item
    print(f"A chave '{chave}' contém o valor '{valor}'.")