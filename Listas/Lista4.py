#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

lista=[]
lConsoantes =[]
consoante = 0
while len(lista) < 9:
    letra = input("Digite um caracter: ")
    lista.append(letra)
    if  letra not in 'aeiou':
        consoante +=1
        lConsoantes.append(letra)
print(lista)
print("O numero de consoantes digitadas é:", consoante)
print(lConsoantes)