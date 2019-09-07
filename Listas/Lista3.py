#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista=[]
i=0
soma = 0
while len(lista) < 4:
    lista.append(float(input("Digite uma nota: ")))
print("Sua notas são: ")
while i < 4:
    print(lista[i])
    soma = soma + lista[i]
    i+=1
print("Sua media é: ")
media = soma/len(lista)
print(media)


#for var in lista:
 #   print(var)