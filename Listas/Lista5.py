#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números
#pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
lista=[]
lPar =[]
lImpar = []
while len(lista) < 20:
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if (numero % 2 == 0):
        lPar.append(numero)
    else:
        lImpar.append(numero)
print(lista)
print("Numeros pares digitados:", lPar)
print("Numeros impares digitados:", lImpar)