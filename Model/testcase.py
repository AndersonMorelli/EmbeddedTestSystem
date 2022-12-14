class TestSequence(object):
    def __init__(self, acao, parametro, tipo):
        self.acao = acao
        self.parametro = parametro
        self.tipo = tipo

class Testcase(object):
    def __init__(self, nome, test_steps = None):
        self.nome = nome
        self.test_steps = []

    def refatorar_teststeps(self):
        i = 1
        for test in self.test_steps:
            test.index = i

    def adicionar_teststep(self, acao, parametro, tipo):
        self.test_steps.append(TestSequence(acao,parametro,tipo))


    def remover_teststep(self):
        self.test_steps.pop()
