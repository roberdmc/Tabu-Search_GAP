def get_neighbors(assignment):
    neighbors = []
    for i in range(len(assignment)):
        for j in range(len(assignment[i])):
            if assignment[i][j] == 1:
                for k in range(len(assignment)):
                    if k != i:
                        neighbor = [row.copy() for row in assignment]
                        neighbor[i][j] = 0
                        neighbor[k][j] = 1
                        neighbors.append(neighbor)
    return neighbors