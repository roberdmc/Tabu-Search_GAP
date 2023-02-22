from Solution import Solution

#Gera os vizinhos para a solução
def get_neighbors(sol):
    neighbors = []
    #Percorre cada programador
    for prog in range(sol.num_prog):
        #Percorre cada módulo do programador
        for mod in range(sol.num_mod):
            #Se o programador estiver atribuído ao módulo, tira e atribui para outro programador
            if sol.assignment[prog][mod] == 1:
                for prog_sub in range(sol.num_prog):
                    if prog_sub != prog:
                        neighbor_assignment = [row.copy() for row in sol.assignment]
                        neighbor_assignment[prog][mod] = 0
                        neighbor_assignment[prog_sub][mod] = 1
                        neighbor = Solution(neighbor_assignment, sol.costs, sol.hours, sol.availability, sol.num_prog, sol.num_mod, sol.P)
                        neighbors.append(neighbor)
    return neighbors