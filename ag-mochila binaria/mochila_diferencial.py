# -*- coding: utf-8 -*-
from ag_diferencial import AG

with open('mochila.txt','r') as f:
    a = f.readlines()
mochila = {}

for i,line in enumerate(a):
    mochila[i] = [float(line.split(' ')[0]),float(line.split(' ')[1])]

# mochila = { 0:[11,1],
#             1:[21,11],
#             2:[31,21],
#             3:[33,23],
#             4:[43,33],
#             5:[53,43],
#             6:[55,45],
#             7:[65,55]}
            # item_id : [utilidade (prioridade), peso]

def fitness(individuo,carga_mochila):
    # carga_mochila = carga maxima que a mochila suporta
    # carga = carga que o individuo a ser testado esta carregando
    # prioridade_cont = prioridade do conjunto carregado
    carga = 0
    prioridade_cont = 0
    for i in range(len(mochila)):
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

while novoag.geracao <= 200:
    print 'geracao',novoag.geracao
    novoag.selecionar()

    for i in range(len(novoag.populacao)):
        fit = fitness(novoag.populacao[i][0], carga_mochila)
        novoag.populacao[i][1] = fit

    melhores.append(novoag.melhor[1])

print 'itens: ',novoag.melhor[0],' - > ',
for i,j in enumerate(novoag.melhor[0]):
    if j == 1:
        print i,
print '\n'
print 'fit:',novoag.melhor[1]
# print melhores

# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# fig = plt.figure()
# ax = plt.axes()
# plt.plot(melhores)
# plt.show()
