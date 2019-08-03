#Faça um programa que leia 3 numeros e mostre o maior deles

primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))
terceiro = int(input("Digite o terceiro numero: "))

maior = primeiro
# Achando o menor número

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('Maior: ',maior)

# Achando o menor número
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('Menor: ',menor)