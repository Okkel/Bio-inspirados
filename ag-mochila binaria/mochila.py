# -*- coding: utf-8 -*-
from ag import AG

mochila = { 0:[11,1],
            1:[21,11],
            2:[31,21],
            3:[33,23],
            4:[43,33],
            5:[53,43],
            6:[55,45],
            7:[65,55]}
            # item_id : [utilidade (prioridade), peso]

def fitness(individuo,carga_mochila):
    # carga_mochila = carga maxima que a mochila suporta
    # carga = carga que o individuo a ser testado esta carregando
    # prioridade_cont = prioridade do conjunto carregado
    carga = 0
    prioridade_cont = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            carga += mochila[i][1]
            prioridade_cont += mochila[i][0]


    if carga > carga_mochila:
        excesso = ((carga*100)/carga_mochila)
        # print('carga',carga ,'-------','fit',prioridade_cont - (excesso * prioridade_cont))
        return (prioridade_cont - (excesso * prioridade_cont))
    else:
        # print('nao estourou',carga,'fit',prioridade_cont)
        return prioridade_cont

carga_mochila = 100

novoag = AG(100, 8)

melhores = []
while novoag.geracao <= 2000:

    #avalia cada solução do AG
    for i in range(len(novoag.populacao)):
        fit = fitness(novoag.populacao[i][0], carga_mochila)
        novoag.populacao[i][1] = fit

    melhores.append(novoag.melhor[1])

    novoag.selecionar()


import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()

print 'resposta : \n'
print 'itens: ',novoag.melhor[0]
print 'fit:',novoag.melhor[1]
