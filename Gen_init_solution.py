def generate_initial_solution(np, nm, hours, availability):
    assignment = [[0 for j in range(nm)] for i in range(np)]
    availability_aux = availability[:]
    for j in range(nm):
        i = 0
        while availability_aux[i]-hours[i][j]<0 and i < np-1:
            i += 1
        assignment[i][j] = 1
        availability_aux[i] -= hours[i][j]
    return assignment