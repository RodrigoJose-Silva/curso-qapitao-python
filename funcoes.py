# Este programa demonstra o uso de funções em Python
# Funções são blocos de código reutilizáveis que realizam tarefas específicas

# Função simples sem parâmetros
# def define uma nova função
def mostra_nome():
    # Esta função apenas exibe uma mensagem fixa
    print("Função exibe o nome/texto hardcoded.")

# Chamando a função para executá-la
mostra_nome()

# Função com parâmetro (argumento)
# O parâmetro 'nome' recebe um valor quando a função é chamada
def mostra_nome_param(nome):
    # Esta função exibe uma mensagem usando o valor passado como parâmetro
    print(f"Função exibe o nome/texto passado como parâmetro: {nome}")

# Chamando a função e passando "Joãozin" como argumento
mostra_nome_param("Joãozin")

# Função com retorno (return)
# Esta função recebe um valor, faz um cálculo e retorna o resultado
def converter_para_real(valor_em_dolar):
    cotacao = 5.30  # Taxa de câmbio fixa
    resultado = valor_em_dolar * cotacao  # Multiplica o valor pela cotação
    return resultado  # Retorna o valor calculado

# Chama a função e armazena o resultado em uma variável
valor_convertido = converter_para_real(100)

# Exibe o resultado formatado com 2 casas decimais
print(f"O valor convertido é R$ {valor_convertido:.2f}")

# Função com múltiplos parâmetros e retorno
# Esta função recebe dois parâmetros e retorna uma string formatada
def criar_email_corporativo(nome, empresa):
    # Cria uma string com o formato de email
    email = f'{nome}@{empresa}.com'
    # Retorna o email convertido para minúsculas usando .lower()
    return email.lower()

# Chama a função passando dois argumentos e armazena o resultado
email_gerado = criar_email_corporativo("Maria", "Google")

# Exibe o email gerado
print(f"O email corporativo gerado é: {email_gerado}")