from igraph import *
import random


g = Graph.Read_GraphML('dj38.gml')


class Ant:
    def __init__(self,start):
        self.vertex = start # initial vertex or current vertex
        self.path = []
        self.path.append(start)

        self.cost = 0



class Colony:

    def __init__(self,g,ant_number = 10,alpha = 0.8,beta = 0.2,evaporation_rate = 0.02,max_iterations = 50):

        self.g = g
        # g.es['weight'] = 2
        g.es['feromony'] = 1


        self.ant_number = ant_number if self.g.vcount() > ant_number else self.g.vcount()-1
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.max_iterations = max_iterations
        # self.target = target
        self.ants = []

        initial_verttices = random.sample(range(self.g.vcount()-1),self.ant_number)

        # Creating a Colony

        for i in range(self.ant_number):
            self.ants.append(Ant(initial_verttices.pop()))
        # for i in self.ants:
        #     print 'formigas',i.vertex,i.path,i.cost


    def deleting_path(self):
        for ant in self.ants:
            # print 'path',ant.path
            ant.cost = 0.0
            del(ant.path[1:]) #deleting_path except the first element

    def roulette(self,vet):

        x = random.random()

        y = 0
        for i,j  in enumerate(sorted(vet,reverse = True)):
            y += j
            if y >= x:
                return i


    def spreading_pheromone(self):

        # Evaporating

        for i in g.es():
            i['feromony'] -= self.evaporation_rate

        #  Depositing

        self.ants.sort(key = lambda X:X.cost)
        # for i in self.ants:
        #     print i.path,i.cost
        print 'menor caminho',self.ants[0].path,self.ants[0].cost

        feromony = [1/float(i.cost) if float(i.cost) != 0 else 1 for i in self.ants]

        for i,j in enumerate(self.ants):
            path = self.g.get_eids( path = j.path, directed=False) # geting ids of edges that compose the path
            for k in path:
                self.g.es[k]['feromony'] += feromony[i]

        self.deleting_path()


    def run(self):
        for it in range(self.max_iterations):
            print 'iterando',it,self.max_iterations-1

            for ant in self.ants:

                while len(ant.path) < self.g.vcount() -1 :


                    nv_neighbors = self.g.neighbors(g.vs[ant.path[-1]]) # non visited neighbors
                    prob_edge = []
                    edge_vet = []
                    for j in list(set(nv_neighbors) - set(ant.path)):
                        edge = self.g.get_eid(ant.path[-1] , j)
                        p = self.g.es[edge]['feromony'] ** self.alpha * (1 / self.g.es[edge]['weight']) ** self.beta # p = probability
                        prob_edge.append(p)
                        edge_vet.append(edge)
                    prob_edge = [k/sum(prob_edge) for k in prob_edge]
                    edge_pos = self.roulette(prob_edge)

                    e = self.g.es[edge_vet[edge_pos]]

                    vertex_chosen = e.target if e.target != ant.path[-1] else e.source

                    ant.cost += e['weight']
                    ant.path.append(vertex_chosen)

            self.spreading_pheromone()
        

if __name__ == '__main__' :
    c = Colony(g,ant_number = 10,alpha = 0.8,beta = 0.2,evaporation_rate = 0.000002,max_iterations = 10)
    print c.run()
