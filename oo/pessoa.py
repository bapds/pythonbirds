class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estático():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'



if __name__ == '__main__':
    person = Pessoa('Feijão', 5)
    print(person.cumprimentar())
    print(person.nome)
    print(person.__dict__)
    print(person.nome_e_atributos_de_classe())
