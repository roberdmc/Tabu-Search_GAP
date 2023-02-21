#Calcula a inviabilidade da solução (horas estouradas por cada programador)
def calculate_infeasibility(assignment_hours, availability):
    infeasibility = 0
    #Percorre as horas de cada programador e, se houve estouro, soma em infeasibility
    for prog in range(len(assignment_hours)):
        if assignment_hours[prog] > availability[prog]:
            infeasibility += assignment_hours[prog] - availability[prog]
    #Retorna o total de horas estouradas pela solução
    return infeasibility

#Calcula o custo total da solução
def calculate_cost(assignment, infeasibility, costs, P):
    total_cost = 0
    #Percorre os programadores
    for prog in range(len(assignment)):
        #Percorre os módulos do programador
        for mod in range(len(assignment[prog])):
            #Multiplica a atribuição pelo custo e soma em total_cost (Se 1 soma o custo, se 0 soma 0)
            total_cost += assignment[prog][mod] * costs[prog][mod]
    
    #Verifica se há estouro de horas
    #Se sim, calcula a penalidade (considerando o fator P) e inclui no custo da solução
    if infeasibility > 0:
        total_cost += infeasibility * P
    #Retorna o custo total da solução
    return total_cost

#Calcula as horas gastas por cada programador da solução
def calculate_hours(assignment, hours, nm):
    assign_hours = []
    #Percorre as atribuições e lista de horas de cada programador
    for assign,prog_hours in zip(assignment, hours):
        sum_hours = 0
        #Percorre as atribuições do programador
        for mod in range(nm):
            #Multiplica o valor da atribuição (0 ou 1) pelas horas que ele gasta no módulo
            #Armazenar as horas totais gastas pelo programador
            sum_hours += assign[mod]*prog_hours[mod]
        assign_hours.append(sum_hours)
    #Retorna o vetor de horas totais gastas por cada programador na solução
    return assign_hours