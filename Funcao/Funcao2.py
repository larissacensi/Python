#2. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma
#desses três argumentos.

def soma(valor1, valor2, valor3):
    return valor1 + valor2 + valor3

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

print(f'A soma dos valores e {soma(valor1, valor2, valor3)}')


def verificaPositivo(valor):
    if (valor > 0):
        return 'P'
    else:
        return 'N'

numero = int(input('Informe um número: '))
print(f'Resultado: {verificaPositivo(numero)}')