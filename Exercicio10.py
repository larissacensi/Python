#Programa que pede a temperatura em graus celsius, transforme e mostre a temperatura em graus fahrenheit
#f=9*c/5+32
celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit= round((9*celsius/5+32),2)
print(celsius,"graus celsius é igual a",fahrenheit,"graus fahrenheit")
