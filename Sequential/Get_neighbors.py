#Gera os vizinhos para a solução
def get_neighbors(assignment):
    neighbors = []
    #Percorre cada programador
    for prog in range(len(assignment)):
        #Percorre cada módulo do programador
        for mod in range(len(assignment[prog])):
            #Se o programador estiver atribuído ao módulo, tira e atribui para outro programador
            if assignment[prog][mod] == 1:
                for prog_sub in range(len(assignment)):
                    if prog_sub != prog:
                        neighbor = [row.copy() for row in assignment]
                        neighbor[prog][mod] = 0
                        neighbor[prog_sub][mod] = 1
                        neighbors.append(neighbor)
    return neighbors