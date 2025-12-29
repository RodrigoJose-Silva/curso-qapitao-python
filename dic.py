pessoa = {
    'nome': 'João Silva',
    'idade': 30,
    'cidade': 'São Paulo',
    'ative': True
}

print(pessoa)  # Imprime o dicionário completo
print(pessoa['nome'])  # Acessa o valor associado à chave 'nome'

pessoa['idade'] = 23  # Atualiza o valor da chave 'idade'
pessoa['profissão'] = 'QA'  # Adiciona uma nova chave-valor

print(pessoa)

for chave in pessoa:
    print(chave)

for chave, valor in pessoa.items():
    print(f"A chave '{chave}' contém o valor '{valor}'.")