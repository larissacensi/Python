#As organizações Tabajara resolveram dar aumento de salario ao seus colaboradores e lhe contrataram para desenvolver
#o programa que calculara  os reajustes. Faça um programa que recebe os o salario de um colaborador e o reajuste
#segundo o seguinte criterio, baseado no salario atual:
#Ate 280  - 20%
#Entre 280 e 700 - 15%
#Entre 700 a 1500 - 10%
#De 1500 em diante - 5%

salario = float(input("Digite seu salario atual: "))
if( salario <= 280):
    salario = salario + (salario*0.2)
    reajuste = "20%"
elif (salario > 280 and salario <= 700):
    salario = salario + (salario * 0.15)
    reajuste = "15%"
elif (salario > 700 and salario <= 1500):
    salario = salario + (salario * 0.1)
    reajuste = "10%"
else:
    salario = salario + (salario * 0.05)
    reajuste = "5%"
print("Apos o reajuste de", reajuste, "o seu salario será de", round(salario,2))