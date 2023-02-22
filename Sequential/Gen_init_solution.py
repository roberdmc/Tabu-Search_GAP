#Gera a solução inicial para o problema (sem se preocupar se é válida ou não)
def generate_initial_solution(num_prog, num_mod, hours, availability):
    assignment = [[0 for j in range(num_mod)] for i in range(num_prog)]
    availability_aux = availability[:]
    #Para cada módulo, atribui um programador
    for j in range(num_mod):
        i = 0
        #Verifica cada programador e atribui o primeiro que estiver com horas disponíveis
        while availability_aux[i]-hours[i][j]<0 and i < num_prog-1:
            i += 1
        #Marca como 1 a linha e coluna referente ao módulo e programador atribuído
        assignment[i][j] = 1
        #Subtrai as horas utilizadas
        availability_aux[i] -= hours[i][j]
    return assignment