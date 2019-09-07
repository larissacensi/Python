#2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista=[]
i=0
while i< 10:
    num = float(input("Digite um numero: "))
    lista.insert(i, num)
    i+=1
print(lista)
print(lista[::-1])