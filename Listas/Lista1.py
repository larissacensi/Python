#1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
i=0
lista=[]
while i < 5:
    num = (input("Digite um numero:"))
    lista.insert(i, num)
    i+=1
print(lista)
