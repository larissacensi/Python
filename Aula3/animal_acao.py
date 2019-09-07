import animal_estimacao as animal

lulu = animal.AnimalEstimação('Meise', 'Dog', 'Larissa')
print(f'{lulu.nome}, Especie {lulu.especie}, Dono: {lulu.dono}')
print(lulu.correr())
print("-------------------------------------------------------")
chile = animal.AnimalEstimação("Lola", "Cat", "Larissa")
print(f'{chile.nome}, Especie {chile.especie}, Dono: {chile.dono}')
print(chile.brincar())
print("-------------------------------------------------------")
thor = animal.AnimalEstimação("Thor", "Dog", "Larissa")
print(f'{thor.nome}, Especie {thor.especie}, Dono: {thor.dono}')
print(thor.comer())
print("-------------------------------------------------------")
fish = animal.PeixeDeEstimacao('Fish', 'Lari')
print(f'Nome: {fish.nome}, Espécie {fish.especie}, Dono: {fish.dono}')
print(fish.nadar())
fish.correr()

