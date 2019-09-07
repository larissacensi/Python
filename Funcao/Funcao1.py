#1. Faça um programa para imprimir:
#1
#2 2
#3 3 3
#.....
#n n n n n n ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a
#n-ésima linha.


def imprime(numeroVezes):
    for numero in range(numeroVezes+1):
        for i in range(numero):
            print(numero, end='')
        print("")


numeroVezes = int(input("Digite um numero de vezes para realizar a repetição: "))
imprime(numeroVezes)