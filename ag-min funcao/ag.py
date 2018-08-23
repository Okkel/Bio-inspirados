import random

class AG:
    def __init__(self, tam_populacao, tam_gene):
        self.populacao = []
        self.tam_populacao = tam_populacao
        self.tam_gene = tam_gene
        self.geracao = 0
        temp = [i for i in range(tam_gene)]
        self.melhor = [temp,1.10]

        for i in range(tam_populacao):
            cromossomo = []
            for c in range(tam_gene):
                cromossomo.append(random.random() + 0.0001)
            self.populacao.append([cromossomo, 0.0])

        return

    def selecionar(self):
        #  Torneio
        for ind in self.populacao:
            if ind[1]< self.melhor[1]:
                self.melhor = ind

        pais_selecionados = []
        while len(pais_selecionados) < (self.tam_populacao / 2):
            pais = random.sample(self.populacao, 2)
            if pais[0][1] < pais[1][1]:
                pais_selecionados.append(pais[0])
                # print pais[0]
            else:
                pais_selecionados.append(pais[1])
                # print pais[1]

        self.cruzar(pais_selecionados)

    def selecionar_roleta(self):
        # Roleta

        for ind in self.populacao:
            if ind[1]< self.melhor[1]:
                self.melhor = ind

        for i in self.populacao:
            print i

        fit_sum = sum([1.0/i[1] for i in self.populacao])
        print 'menor'
        print min([i[1] for i in self.populacao]),'---'*10

        roleta = []
        roleta2 = []

        for i in self.populacao:
            roleta.append((1.0/i[1])/fit_sum)

        for i, ind in enumerate(self.populacao):
            roleta2.append( (1.0/ind[1]/fit_sum , i) )

        roleta2 = sorted(roleta2)

        pais_selecionados = []
        # while len(pais_selecionados) < (self.tam_populacao / 2):
        #
        #     fit = random.uniform(0.00001,fit_sum)
        #
        #     cont = 0
        #     for i in range(len(roleta)):
        #         cont += roleta[i]
        #         if cont >= fit:
        #             pais_selecionados.append(self.populacao[i])

        while len(pais_selecionados) < (self.tam_populacao / 2):

            fit = random.uniform(0.00001,fit_sum)

            cont = 0
            for i in range(len(roleta2)):
                cont += roleta2[i][0]
                if cont >= fit:
                    pais_selecionados.append(self.populacao[roleta2[i][1]])

        self.cruzar(pais_selecionados)


    def cruzar(self, pais_selecionados):
        #print self.geracao
        nova_populacao = []

        nova_populacao.append(self.melhor)

        for i in range(self.tam_populacao - 1):
            pai1 = random.choice(pais_selecionados)[0]
            pai2 = random.choice(pais_selecionados)[0]

            filho = [[sum(i)/2.0 for i in zip(pai1,pai2)],0.0]
            #print filho
            # filho = [np.zeros(self.tam_gene).tolist(), 0.0]
            # for i in range(self.tam_gene):
            #     filho[0][i] = (pai1[i] + pai2[i]) / 2.0

            # filho = [pai1[:self.tam_gene/2] + pai2[self.tam_gene/2:],0.0]

            nova_populacao.append(filho)

        self.populacao = nova_populacao[:]
        self.mutar()

    def mutar(self):
        self.geracao += 1
        for i in self.populacao:
            if random.random() < 0.05:
                i[0][0] += 0.5
                # i[0][random.choice(range(self.tam_gene-1))] = max(i[0]) + 0.1
