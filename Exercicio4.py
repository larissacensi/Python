#Faça um programa que peça as 4 notas bimestrais e mostre a média:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = ((nota1 + nota2 + nota3 + nota4)/4)
print("A media bimestral foi de: ", media)
if(media >6 ):
    print("Aprovado")
else:
    print("Reprovado")

