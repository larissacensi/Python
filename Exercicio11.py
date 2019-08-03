##Programa que pergunta quanto você ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre o total
#de seu salario no referido mês, sabendo-se que são descontados 11% para o imposto de renda, 8% para o INSS e 5% para o
#sindicato, faça um programa que nos dê: A: Salario bruto B:Quanto pagou de INSS C: Quanto pagou de sindicato
# D: O Salario liquido E: Calcule o desconto do salario liquido conforme a tabela abaixo.

salarioHora = float(input("Digite quanto você ganha por hora: "))
numHorasMes = float(input("Digite o numero de horas trabalhadas no mês: "))
salarioBruto = round((salarioHora*numHorasMes),2)
ImpostoRenda = (salarioBruto * 0.11)
INSS = (salarioBruto*0.08)
Sindicato = (salarioBruto*0.05)
Liquido = salarioBruto - ImpostoRenda - INSS - Sindicato

print("- Salario Bruto: R$",salarioBruto)
print("- IR (11%): R$", ImpostoRenda)
print("- INSS (8%): R$", INSS)
print("- Sindicato (5%): R$", Sindicato)
print("- Salario liquido: R$", Liquido)
