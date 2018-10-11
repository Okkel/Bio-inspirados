import random

class AG:
    def __init__(self, tam_populacao, tam_gene, F = 0.3 , Cr = 0.2):
        self.F = F
        self.Cr = Cr
        self.populacao = []
        self.popIntermediaria = []
        self.tam_populacao = tam_populacao
        self.tam_gene = tam_gene
        self.geracao = 0
        temp = [i for i in range(tam_gene)]
        self.melhor = [temp,1.10]

        for i in range(tam_populacao):
            cromossomo = []
            for c in range(tam_gene):
                cromossomo.append(random.random()+ 0.001)
            self.populacao.append([cromossomo, 0.0])

        return

    def selecionar(self):
        #  Torneio
        for i in range(self.tam_populacao):
            if self.populacao[i][1] < self.popIntermediaria[i][1]:
                self.populacao[i] = self.popIntermediaria[i]

        temp = [0,0]
        for i in self.populacao:
            if i[1] > temp[1]:
                temp = i
        self.melhor = temp


    def cruzar(self, popIntermediaria):
        #print self.geracao
        nova_populacao = []

        for i in range(self.tam_populacao):

            novo_infividuo = []
            for j in range(self.tam_gene):

                if random.random() < self.Cr:
                    # print 'popIntermediaria[i][0][0]',popIntermediaria[i][0][0]
                    novo_infividuo.append([popIntermediaria[i][0][j],0.0])
                else:
                    novo_infividuo.append([self.populacao[i][0][j],0.0])
            nova_populacao.extend(novo_infividuo)

        self.popIntermediaria = nova_populacao[:]

        self.selecionar()

    def mutar(self):
        self.geracao += 1
        popIntermediaria = []

        while len(popIntermediaria) < self.tam_populacao:
            x,y,z = random.sample(self.populacao, 3)
            popMut = x[0][0] + self.F * (y[0][0] - z[0][0] )
            popIntermediaria.append([[popMut],0.0])
        self.cruzar(popIntermediaria)
