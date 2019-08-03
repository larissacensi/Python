#Programa que pergunta quanto você ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre o total
#de seu salario no referido mês
salarioHora = float(input("Digite quanto você ganha por hora: "))
numHorasMes = float(input("Digite o numero de horas trabalhadas no mês: "))
salario = round((salarioHora*numHorasMes),2)
print("O seu salario no final do mês será de", salario, "reais")