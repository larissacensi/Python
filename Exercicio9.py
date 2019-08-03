#Programa que pede a temperatura em graus fahrenheit, transforme e mostre a temperatura em graus celsius
#C=(5*(F-32)/9)

fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))
celsius =round((5*(fahrenheit-32)/9),2)
print(fahrenheit,"graus fahrenheit é igual a",celsius,"graus celsius")
