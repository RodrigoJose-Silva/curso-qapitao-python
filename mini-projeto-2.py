# Se for maior que 65 → “entrada grátis”
# Se for maior que 18 → “paga inteira”
# Senão → “não pode entrar”

print('--- bem-vindo ao evento --- \n')
idade = input('Informe a sua idade: ')

if int(idade) >= 65:
    print('Entrada grátis!')
elif int(idade) >= 18:
    print('Paga inteira')
else:
    print('Não pode entrar')