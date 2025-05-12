from deap import creator, base, tools, algorithms
import random
from consts import *
from funODSS import DSS

class FunAG:
    def __init__(self, valorCC):
        self.dss = DSS()
        self.dss.compileFile(linkFile)
        self.valorCC = valorCC
        self.barras = self.dss.BusNames()
        self.pmList = []
        creator.create("fitnessMulti", base.Fitness, weights=(-1.0, ))
        #Criando a classe do indivíduo
        creator.create("estrIndiv", list, fitness = creator.fitnessMulti)
      
        
    def FOBbat(self, indiv):
        potsBat = indiv
        potsBat.append(-potsBat[0]-potsBat[1])
        
        #========ALOCA A BATERIA========#
        #==Aloca as potências no barramento e os bancos de capacitores e resolve o sistema==#
        self.dss.alocaPot(barramento=barra, listaPoten=potsBat)
        self.dss.solve(self.valorCC)
        
        #==Recebe as tensões de sequência e as coloca em um dicionário==#
        dfSeqVoltages = self.dss.dfSeqVolt()
        dicSecVoltages = dfSeqVoltages.to_dict(orient = 'list')
        deseq = dicSecVoltages[' %V2/V1']
        
        #==Recebe o valor da função objetivo==#
        fobVal = max(deseq)
        
        restricoes = [
            abs(potsBat[0]) - self.pmList[0],
            abs(potsBat[1]) - self.pmList[1],
            abs(-potsBat[0] - potsBat[1]) - self.pmList[2],
            fobVal - 2
        ]
        #==Penalidade==#
        penalidade = sum(max(0, restricao) for restricao in restricoes)
        penalidadeVal = 1000
        
        return fobVal + penalidadeVal * penalidade,
        
    
    #==Método de cruzamento BLX==#
    def cruzamentoFunBLX(self, indiv1, indiv2):
        newIndiv1 = indiv1
        newIndiv2 = indiv2
        #==Recebe um valor de alfa aleatório==#
        alfa = random.uniform(0.3, 0.5)
        #==Cria um novo indivíduo==#
        for gene in range(len(indiv1)):
            #==calcula o delta==#
            print(f"indiv1: {indiv1} - indiv2: {indiv2}")
            delta = abs(indiv1[gene] - indiv2[gene])
            #==Calcula o mínimo e o máximo==#
            minGene = int(min(indiv1[gene], indiv2[gene]) - alfa*delta)
            maxGene = int(max(indiv1[gene], indiv2[gene]) + alfa*delta)
            if minGene != maxGene:
                #==Sorteia o novo gene entre o mínimo e o máximo==# 
                newIndiv1[gene] = random.randint(minGene, maxGene)
                newIndiv2[gene] = random.randint(minGene, maxGene)
            else:
                newIndiv1[gene] = minGene
                newIndiv2[gene] = minGene
            
        return newIndiv1, newIndiv2
    
    
    
    def criaCromBat(self):
        g1 = random.randint(-self.pmList[0], self.pmList[0])
        g2 = random.randint(-self.pmList[1], self.pmList[1])
        indiv = [g1, 
                g2]
        return indiv
    
    
    
    def mutateFun(self, indiv):
        indiv = self.criaCrom()
        return indiv
    
    
    
    def execAg(self, pms, probCruz=0.9, probMut=0, numGen=100, numRep=1):
            #Objeto toolbox
            toolbox = base.Toolbox()
            #Lista com os valores de Potencia máxima por fase
            self.pmList = pms
            #Criando uma classe de Fitness minimizado
            dicMelhoresIndiv = {"cromossomos": [],
                                "fobs": []}
            #Definindo maneiras de cruzamento e de mutação
            toolbox.register("mate", self.cruzamentoFunBLX)
            toolbox.register("mutate", self.mutateFun)
            
            #Definindo o tipo de seleção
            toolbox.register("select", tools.selTournament, tournsize=10)

            #Definindo a fob e as restrições
            toolbox.register("evaluate", self.FOBbat)

            for rep in range(numRep):
                #Definindo como criar um indivíduo (cromossomo) com 4 genes inteiros
                toolbox.register("indiv", tools.initIterate, creator.estrIndiv, self.criaCromBat)

                #Definindo a população
                toolbox.register("pop", tools.initRepeat, list, toolbox.indiv)

                #Criando uma população
                populacao = toolbox.pop(n=30)

                hof = tools.HallOfFame(1)
                result, log = algorithms.eaSimple(populacao, toolbox, cxpb=probCruz, mutpb=probMut, ngen=numGen, halloffame=hof, verbose=False)
                dicMelhoresIndiv["cromossomos"].append(hof[0])
                dicMelhoresIndiv["fobs"].append(hof[0].fitness.values[0])
                print(f"Rep: {rep+1} - FOB: {hof[0].fitness.values[0]}")
            
            return result, log, dicMelhoresIndiv