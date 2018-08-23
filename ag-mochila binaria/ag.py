import random

class AG:
    def __init__(self, tam_populacao, tam_gene):
        self.populacao = []
        self.tam_populacao = tam_populacao
        self.tam_gene = tam_gene
        self.geracao = 0
        temp = [1 for i in range(tam_gene)]
        self.melhor = [temp,0.0]

        for i in range(self.tam_populacao):
            cromossomo = [random.randint(0,1) for i in range(self.tam_gene)]
            self.populacao.append([cromossomo, 0.0])

        return

    def selecionar(self):
        #  Torneio
        for ind in self.populacao:
            if ind[1] > self.melhor[1]:
                self.melhor = ind

        pais_selecionados = []
        while len(pais_selecionados) < (self.tam_populacao / 2):
            pais = random.sample(self.populacao, 2)
            if pais[0][1] > pais[1][1]:
                pais_selecionados.append(pais[0])
                # print pais[0]
            else:
                pais_selecionados.append(pais[1])
                # print pais[1]

        self.cruzar(pais_selecionados)


    def cruzar(self, pais_selecionados):
        #print self.geracao
        nova_populacao = []

        nova_populacao.append(self.melhor)

        for i in range(self.tam_populacao - 1):
            pai1 = random.choice(pais_selecionados)[0]
            pai2 = random.choice(pais_selecionados)[0]

            filho1 = pai1[:self.tam_gene/2] + pai2[self.tam_gene/2:]
            filho1 = [filho1,0.0]

            filho2 = pai2[:self.tam_gene/2] + pai1[self.tam_gene/2:]
            filho2 = [filho2,0.0]

            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        self.populacao = nova_populacao[:]
        self.mutar()

    def mutar(self):
        self.geracao += 1
        for i in self.populacao:
            if random.random() < 0.05: #0.05 = chance de mutacao
                pos = random.randint(0,self.tam_gene-1)
                i[0][pos] = 0 if i[0][pos] == 0 else 1
