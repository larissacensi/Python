import calculadora

while True:
    print('Operações')
    print('1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação')
    operacao = int(input('Qual a operação deseja?'))

    if operacao < 5 and operacao != 0:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        if operacao == 1:
            print('A soma é igual a: ', calculadora.somar(numero1, numero2))
        elif operacao == 2:
            print('A subtração é igual a:', calculadora.subtrair(numero1, numero2))
        elif operacao == 3:
            print('A divisão é igual a:', calculadora.divir(numero1, numero2))
        elif operacao == 4:
            print('A multiplicação é igual a:', calculadora.multiplicar(numero1, numero2))

    else:
        if operacao == 0:
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print("Fechando calculadora...")
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            break
        else:
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print('Operação invalida')
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
