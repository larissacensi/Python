#Programa para calcular a area de um circulo
import math
raio = float(input("Digite o raio do circulo: "))
unraio = input("Qual a unidade de medida do raio: ")
raioAoQuadrado = raio**2
area = round((raioAoQuadrado*math.pi),2)
print("A area do circulo é de", area, unraio)