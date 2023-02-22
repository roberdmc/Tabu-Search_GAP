from tkinter import filedialog
import pandas as pd
from os import system, name

class Solution:
    assignment=[]; costs=[]; hours=[]; used_hours=[]; availability=[]
    num_prog=0; num_mod=0; total_cost=0; P=0; infeasibility=0
    
    def __init__(self, assignment, costs, hours, availability, num_prog, num_mod, P):
        self.assignment = assignment
        self.costs=costs
        self.hours=hours
        self.availability=availability
        self.num_prog=num_prog
        self.num_mod=num_mod
        self.P = P
        self.update()

    #Atualiza os custos, horas usadas e inviabilidades
    def update(self):
        self.calculate_hours()
        self.calculate_infeasibility()
        self.calculate_cost()

    #Gera a solução inicial para o problema (sem se preocupar se é válida ou não)
    def gen_init_sol(self):
        self.assignment = [[0 for j in range(self.num_mod)] for i in range(self.num_prog)]
        availability_aux = self.availability[:]
        #Para cada módulo, atribui um programador
        for j in range(self.num_mod):
            i = 0
            #Verifica cada programador e atribui o primeiro que estiver com horas disponíveis
            while availability_aux[i]-self.hours[i][j]<0 and i < self.num_prog-1:
                i += 1
            #Marca como 1 a linha e coluna referente ao módulo e programador atribuído
            self.assignment[i][j] = 1
            #Subtrai as horas utilizadas
            availability_aux[i] -= self.hours[i][j]
    
    #Calcula as horas gastas por cada programador da solução
    def calculate_hours(self):
        self.used_hours.clear()
        #Percorre as atribuições e lista de horas de cada programador
        for assign,prog_hours in zip(self.assignment, self.hours):
            sum_hours = 0
            #Percorre as atribuições do programador
            for mod in range(self.num_mod):
                #Multiplica o valor da atribuição (0 ou 1) pelas horas que ele gasta no módulo
                #Armazenar as horas totais gastas pelo programador
                sum_hours += assign[mod]*prog_hours[mod]
            self.used_hours.append(sum_hours)

    #Calcula a inviabilidade da solução (horas estouradas por cada programador)
    def calculate_infeasibility(self):
        self.infeasibility = 0
        #Percorre as horas de cada programador e, se houve estouro, soma em infeasibility
        for prog in range(self.num_prog):
            if self.used_hours[prog] > self.availability[prog]:
                self.infeasibility += self.used_hours[prog] - self.availability[prog]
    
    #Calcula o custo total da solução
    def calculate_cost(self):
        self.total_cost = 0
        #Percorre os programadores
        for prog in range(self.num_prog):
            #Percorre os módulos do programador
            for mod in range(self.num_mod):
                #Multiplica a atribuição pelo custo e soma em total_cost (Se 1 soma o custo, se 0 soma 0)
                self.total_cost += self.assignment[prog][mod] * self.costs[prog][mod]
        #Verifica se há estouro de horas
        #Se sim, calcula a penalidade (considerando o fator P) e inclui no custo da solução
        if self.infeasibility > 0:
            self.total_cost += self.infeasibility * self.P
    
    #Printa os resultados, mostrando se é válido ou não
    def print_results(self, it=0, initial=False, final=False):
        if final:
            print("\n")
            print("---- Tabu Search completed successfully ----")
            print("\n")
            print("--- Best result found: ---")
        elif initial:
            print()
            if self.infeasibility==0:
                print("--- Initial solution (Valid): ---")
            else:
                print("--- Initial solution (Not valid): ---")
        else:
            print()
            print(f"--- Iteration {it}: ---")
            if self.infeasibility==0:
                print("--- Best neighbor (Valid): ---")
            else:
                print("--- Best neighbor (Not valid): ---")
        print("Assignment:")
        for row in self.assignment:
            print("\t\t",row)
        print(f"Cost: {int(self.total_cost-(self.infeasibility*self.P))}")
        if self.infeasibility > 0:
            print(f"Cost+penalty: {self.total_cost}")
        print(f"Hours used:\t {self.used_hours}")
        print(f"Availability:\t {self.availability}")
        print()