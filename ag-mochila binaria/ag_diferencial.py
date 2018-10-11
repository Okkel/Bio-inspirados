import random

class AG:
    def __init__(self, tam_populacao, tam_gene, taxa_cruzamento= 0.2,taxa_mutacao = 0.3):
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.populacao = []
        self.nova_populacao = []
        self.tam_populacao = tam_populacao
        self.tam_gene = tam_gene
        self.geracao = 0
        temp = [1 for i in range(tam_gene)]
        self.melhor = [temp,0.0]

        for i in range(self.tam_populacao):
            cromossomo = [random.randint(0,1) for i in range(self.tam_gene)]
            self.populacao.append([cromossomo, 0.0])
        self.nova_populacao =self.populacao[:]
        return

    def selecionar(self):

        a = max(self.populacao , key= lambda x:x[1])
        self.melhor = a[:]
        # print 'antes de mutar', a

        self.mutar()
        a = self.populacao[:]
        a.extend(self.nova_populacao)
        a = sorted(a,key = lambda x:x[1],reverse = True)
        self.populacao = a[:self.tam_populacao]

        # print 'populacao'
        # for i in self.populacao:
        #     print i


        self.geracao += 1



    def mutar(self):
        #print self.geracao
        pop_mutada = []

        # nova_populacao.append(self.melhor)

        # MUTACAO
        while len(pop_mutada) < self.tam_populacao:
            pai1 = random.choice(self.populacao)[0]
            pai2 = random.choice(self.populacao)[0]
            pai3 = random.choice(self.populacao)[0]

            filho = []
            for i in range(len(pai1)):
                # if random.random() <= taxa_mutacao:
                filho.append(pai1[i] or  (pai2[i] and pai3[i]))

            # filho = [i or (random.randint(0,1) and (j and k)) for i in pai1 for j in pai2 for k in pai3]

            filho = [filho,0.0]
            pop_mutada.append(filho)

            self.cruzar(pop_mutada)

    # CRUZAMENTO
    def cruzar(self,pop_mutada):
        pop_cruzada = []
        while len(pop_cruzada) < self.tam_populacao:

            filho = []

            pai1 = random.choice(self.populacao)[0]
            pai2 = random.choice(pop_mutada)[0]

            for i in range(len(pai1)):
                if random.random() < self.taxa_cruzamento:
                    filho.append(pai2[i])
                else:
                    filho.append(pai1[i])

            pop_cruzada.append([filho,0.0])

        self.nova_populacao = pop_cruzada[:]
