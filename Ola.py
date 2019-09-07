
#nome = "Larissa"
#print(f"Seu nome é {nome}")

#curso = list()
#curso = ['Larissa', ['Python', 15, 1.0, 'Catolica']]
#print(type (curso))
#cursos = ["Engenharia de software", "Blabla"]
#print(type (cursos))
#print(f"cursos tem {len(cursos)} elementos")
#print(f"curso tem {len(curso)} elementos")
#print(curso[0])
#print(curso[1][1])

#alunos = [['Fabio',20], ['Pedro', 21], ['Thiago', None]]
#print(alunos[1])
#print(alunos[-1])
#print(alunos[1:3])
#print(alunos[::-1])
#print(alunos[1][0])
#nome, idade = alunos[0]
#print(nome)
#print(idade)

#nome = "larissa"
#NomeLetras = list(nome)
#print(NomeLetras)
#for letras in NomeLetras:
 #   letras =letras.upper()
  #  print(letras)


#nome = "larissa"
#nomeLetras = list(nome)
#print(len(nomeLetras))
#nome = ''
#for i in range(len(nomeLetras)):
 #   nomeLetras[i] = nomeLetras[i].upper()
  #  nome += nomeLetras[i]
    #print(nomeLetras[i])
#print(nomeLetras)
#print(nome)

#texto = 'Teste'
#lTexto = list(texto)
#print(lTexto)
#del lTexto[3]
#print(lTexto)
#while lTexto.count('e'):
 #   lTexto.remove('e')
#print(lTexto)

#vogais = ['a']
#vogais.append('i')
#vogais.append('o')
#print(vogais)
#vogais.insert(1, 'e')
#print(vogais)
#vogais.extend(['u'])
#print(vogais)
#nome = 'Jaraguá do Sul'
#print([letra for letra in nome])
#print([letra for letra in nome if letra not in 'a'])
#print([numero for numero in range(11) if numero%2 ==0 ])

#numeros = [2,3,1,4]
#numeros.sort()
#print(numeros)

#t = 'a', 'b'
#t1 = ('a', 'b')
#t2 = 'a',
#t3 = tuple()
#t4 = tuple('Jaraguá')
#t4 = t4 + tuple('do sul')
#print(t4)

#legenda = {'+':'Soma','-':'Subtração','*':'Multiplicação','/':'Divisão'}
#meu_dic_1={}
#meu_dic_2= dict()
#print(type(legenda))
#print(type(meu_dic_1))
#print(type(meu_dic_2))
#alunos = dict(nome='Larissa', idade=21)
#print(alunos)

#print(legenda['+'])
#legenda['+'] = 'Adição'
#print(legenda['+'])

#cod = legenda.pop('+')
#print(cod)
#print(legenda)

#cod = legenda.popitem()
#print(cod)
#print(legenda)

#print('-' in legenda)
#chaves = legenda.keys()
#print('Listando todas as chaves: ')
#for chave in chaves:
 #   print(chave)

#print('Listando todas os valores: ')
#valores = legenda.values()
#for valor in valores:
 #   print(valor)

#print("Adicionado ou atualizando dados:")
#legenda.update({'sei la':'sl'})
#print(legenda)

#s = {'maça', 'uva', 'abacate', 'laranja','abacaxi'}
#s.add('melancia')
#print(s)
#s.remove('uva')
#print(s)

#pares = set((2,4,6,8,10))
#print("Pares: ", pares)
#impares = set((1,3,5,7,9))
#print("Impares: ", impares)
#numeros = pares.union(impares)
#print("União: ", numeros)
#intersec11 = pares.intersection((impares))
#print(intersec11)
#print(pares.difference(impares))

def menu():
    print(""" 
    Escolha um item
    1) Comprar Passagem
    2) Verificar destino
    3) Sair""")

def triplo(x):
    return 3*x

def curso(nome = "Python"):
    print("Curso de " + nome)

def repete(texto = "", vezes=0):
    print(texto* vezes)


menu()
print("o tripo de 3 é:", triplo(3))
curso()
repete('a', 10)


def soma(*valores):
    s=0
    for v in valores:
        s+=v
    return s
print(soma(1,2,3,4))

def fichaTec(diretor ="", autor = "", **elenco):
    print("diretor: " + diretor)
    print("Autor: " + autor)
    for pers, ator in elenco.items():
        print(f'{pers} {ator}')

fichaTec('Larissa', 'Susi', Heroina = 'Susi', Mocinha = 'gabi')



