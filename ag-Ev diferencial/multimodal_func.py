# -*- coding: utf-8 -*-
from ag import AG
from igraph import *
import math
import sys

# g = Graph.Read_GML(sys.argv[1])
# g = Graph.Read_GML("dj38.gml")
#
# print g.vcount()


def fitness(individuo):
    print 'individuo',individuo
    # temp = -20 * math.e**(0.2*math.sqrt(x**2)) - math.e ** (0.5 * math.cos(2 * math.pi * x)) + 20 + math.e
    somatorio = 0.0
    # print novoag.populacao
    # for i in individuo:
    #     # print i
    #     somatorio += (1.0/(i**2.0))
    somatorio += (1.0/(individuo[0]**2.0))
    return math.sqrt(somatorio)
    # return individuo[0]**4
    # return( temp )



novoag = AG(100, 1)


melhores = []
for i in range(len(novoag.populacao)):
    fit = fitness(novoag.populacao[i][0])
    novoag.populacao[i][1] = fit

novoag.mutar()

while novoag.geracao <= 2000:

    #avalia cada solução do AG
    for i in range(novoag.tam_populacao):
        print novoag.popIntermediaria[i]
        fit = fitness(novoag.popIntermediaria[i][0])
        novoag.popIntermediaria[i][1] = fit

    novoag.selecionar()

    melhores.append(novoag.melhor[1])


    # for i in novoag.populacao:
    #     print i, "---", i[0][0]**2


for melhor in melhores:
    print melhor

# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# fig = plt.figure()
# ax = plt.axes()
#
#
# ax.plot(range(len(melhores)), melhores);
# plt.show()
# print melhores[-1]
