class AnimalEstimação():
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono
    def correr(self):
        return f'{self.nome} está correndo!'

    def brincar(self):
        return f'{self.nome} está brincando!'
    def comer(self):
        return f'{self.nome} está comendo!'

class PeixeDeEstimacao(AnimalEstimação):
    def __init__(self, nome, dono):
        super().__init__(nome, 'Peixe', dono)

    def nadar(self):
        return f'{self.nome} está nadando!'

    def correr(self):
        pass
