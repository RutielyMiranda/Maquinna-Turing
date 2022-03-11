class Fita(object):

    simbolo_branco = " "

    def __init__(self,
                 fita_string=""):
        self.__fita = dict((enumerate(fita_string)))

    def __str__(self):
        s = ""
        min_usado_index = min(self.__fita.keys())
        max_usado_index = max(self.__fita.keys())
        for i in range(min_usado_index, max_usado_index):
            s += self.__fita[i]
        return s

    def __getitem__(self, index):
        if index in self.__fita:
            return self.__fita[index]
        else:
            return Fita.simbolo_branco

    def __setitem__(self, pos, char):
        self.__fita[pos] = char


class Maquina_Turing(object):

    def __init__(self,
                 fita="",
                 simbolo_branco=" ",
                 estado_inicial="",
                 estado_final=None,
                 funcao_transicao=None):
        self.__fita = Fita(fita)
        self.__posicao_cabeca = 0
        self.__simbolo_branco = simbolo_branco
        self.__estado_atual = estado_inicial
        if funcao_transicao == None:
            self.__funcao_transicao = {}
        else:
            self.__funcao_transicao = funcao_transicao
        if estado_final == None:
            self.__estado_final = set()
        else:
            self.__estado_final = set(estado_final)

    def get_fita(self):
        return str(self.__fita)

    def step(self):
        char_sob_cabeca = self.__fita[self.__posicao_cabeca]
        x = (self.__estado_atual, char_sob_cabeca)
        if x in self.__funcao_transicao:
            y = self.__funcao_transicao[x]
            self.__fita[self.__posicao_cabeca] = y[1]
            if y[2] == "R":
                self.__posicao_cabeca += 1
            elif y[2] == "L":
                self.__posicao_cabeca -= 1
            self.__estado_atual = y[0]

    def final(self):
        if self.__estado_atual in self.__estado_final:
            return True
        else:
            return False
