calc = eval(input("Operação: "))
if (calc > 5):
  print("É maior que 5")
else:
  print("Não é maior que 5")
#---------------------------------------------------------------------------------------------------------

nome = "Larissa"
print("Seu nome é", "maior" if (len(nome)> len("Alexandre")) else "menor", "que o meu")

#Seu nome é menor que o meu
#---------------------------------------------------------------------------------------------------------

i = 1
while (i<10):
  print(i)
  i+=1

#Resultado
#1
#2
#3
#4
#5
#6
#7
#8
#9

#---------------------------------------------------------------------------------------------------------

empresa = "WEG"
for letra in empresa:
  print(letra, end=' ')

#Resultado: W E G

#---------------------------------------------------------------------------------------------------------

for n in range(2,11,2):
  print(n)

#Resultado:
#2
#4
#6
#8
#10

#---------------------------------------------------------------------------------------------------------

for n in range(11):
  if (n == 5):
    print("Interrupção...")
    break;
  print(n)

  print()

  for n in range(11):
      if (n % 2 == 1):
          continue
      print(n)

#0
# 1
# 2
# 3
# 4
# Interrupção...


# 0
# 2
# 4
# 6
# 8
# 10