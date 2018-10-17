# -*- coding: utf-8 -*-
# 1 - Inicializar uma população de R indivíduoes(partículas)
# 2 - Determinar constantes
# 3 - Verificar se o critério de parada já foi atingido, senão, continuar
# 4 - Sortear dois números aleatórios r1 e r2
# 5 - Determinar a melhor posição individual e global
# 6 - Atualizar velocidade
# 7 - Atualizar posições
# 8 - Voltar ao 3

# velocidade
#
# V(k+1) = w * V(k) + c1r1 (Pbest Xk)
#
# Xk+1 = Xk + Vk
#
# w = coeficiente de inercia
# c1,c2 = constantes (2.05.2.1 ...)
# xk = posicao individual
# pbest = melhor individual
# gbest = melhor globall
# r1,r2 = numeros aleatorias entre 0 e 1

import math
import random

def f(x):
    return x * (math.sin(10 * math.pi * x))+1

class Particle:
    def __init__(self):
        self.x = random.uniform(-1.0, 2.0)
        self.fitnnes = f(self.x)
        self.pbest = self.fitnnes #particle best
        self.v = random.uniform(0.1, 0.5)
        self.fit = 0

class Swarm:
    def __init__(self,c1 = 0.2,c2 = 0.3,w = 0.6 ,particle_number = 10):

        self.gbest  = (0,0) #global best
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.population = []
        for i in range(particle_number):
            self.population.append(Particle())

    def run(self):
        for i in range(50):
            for h,i in enumerate(self.population):

                #  *** Topography = full graph
                # i.v = self.w * i.v + self.c1 * random.uniform(0.5, 1.9) * (i.pbest - i.x) + self.c2 * random.uniform(0.5, 1.9) * (self.gbest[0] - i.x)
                #  ***

                #  *** Topography = circle
                if h == len(self.population)-1:
                    best = max(i.pbest,self.population[h-1].pbest,self.population[0].pbest)
                else:
                    best = max(i.pbest,self.population[h-1].pbest,self.population[h+1].pbest)

                i.v = self.w * i.v + self.c1 * random.uniform(0.5, 1.9) * (i.pbest - i.x) + self.c2 * random.uniform(0.5, 1.9) * (best - i.x)

                #  *** 

                if i.fitnnes > i.pbest:
                    i.pbest = i.x

                if i.fitnnes > self.gbest[1]:
                    self.gbest = (i.x,i.fitnnes)


                i.x = i.x + i.v
                i.fitnnes = f(i.x)

                print 'x',self.gbest[0],'y',self.gbest[1]
        return

s = Swarm()
s.run()
