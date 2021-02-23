class Colaborador:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome

class Desenvolvedor(Colaborador):
    def __init__(self, nome, salario, outro_parametro=None):
        super(Desenvolvedor, self).__init__(nome, salario)
        self.__outro_parametro = outro_parametro

class Designer(Colaborador):
    def __init__(self, nome, salario, mais_um_parametro=None):
        super(Designer, self).__init__(nome, salario)
        self.__mais_um_parametro = mais_um_parametro

class Organizacao:
    def __init__(self):
        self.__colaboradores = list()

    def add_colaborador(self, colaborador):
        self.__colaboradores.append(colaborador)

    def total_salarios(self):
        salarios = 0
        for colaborador in self.__colaboradores:
            print(f"Colaborador: {colaborador.nome}, salário atual: {colaborador.salario}")
            salarios += colaborador.salario
        return salarios

if __name__ == "__main__":
    joao = Desenvolvedor("Yuri Oliveira", 1200)
    carla = Designer("Ariel Maria", 1900)

    organizacao = Organizacao()
    organizacao.add_colaborador(joao)
    organizacao.add_colaborador(carla)

    print(f"Total salários: {organizacao.total_salarios()}")