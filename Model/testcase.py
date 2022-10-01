class TestSequence(object):
    def __init__(self, acao, parametro):
        self.acao = acao
        self.parametro = parametro

class Testcase(object):
    def __init__(self, nome, test_steps = None):
        self.nome = nome
        self.test_steps = []

    def refatorar_teststeps(self):
        i = 1
        for test in self.test_steps:
            test.index = i

    def adicionar_teststep(self, acao, parametro):
        self.test_steps.append(TestSequence(acao,parametro))
        #self.refatorar_teststeps()

    def remover_teststep(self):
        self.test_steps.pop()
        #for test in self.test_steps:
        #    if index == test.index:
        #        self.test_steps.pop(index)
        #        self.refatorar_teststeps()
