# Este programa demonstra o uso do loop while (enquanto)
# O loop while repete um bloco de código enquanto uma condição for verdadeira

# Inicializa a variável contador com valor zero
contador = 0

# Loop while para contar até 5
# O loop continua executando enquanto a condição (contador < 5) for verdadeira
# IMPORTANTE: caso não informe o incremento (contador += 1), o loop será infinito
# Um loop infinito pode travar a aplicação ou até mesmo a máquina
while contador < 5:
    # Exibe o valor atual do contador
    print(f'Contador: {contador}')
    # Incrementa o contador em 1 (equivalente a: contador = contador + 1)
    # Sem este incremento, o loop nunca terminaria
    contador += 1 
    
# Esta mensagem é exibida após o loop terminar
print("Loop While Terminado!")