import random

def read_input_file(file_name):
    with open(file_name) as file:
        np = int(file.readline().strip())
        nm = int(file.readline().strip())
        costs = []
        for i in range(np):
            row = list(map(int, file.readline().strip().split()))
            costs.append(row)
        hours = []
        for i in range(np):
            row = list(map(int, file.readline().strip().split()))
            hours.append(row)
        availability = list(map(int, file.readline().strip().split()))
    return np, nm, costs, hours, availability

def calculate_cost(assignment, infeasibility, costs, P):
    total_cost = 0
    for i in range(len(assignment)):
        for j in range(len(assignment[i])):
            total_cost += assignment[i][j] * costs[i][j]
    
    if infeasibility > 0:
        total_cost += infeasibility * P

    return total_cost

def calculate_hours(assignment, hours, nm):
    ba_hours = []
    for a,a_h in zip(assignment, hours):
        sum_hours = 0
        for i in range(nm):
            sum_hours += a[i]*a_h[i]
        ba_hours.append(sum_hours)

    return ba_hours

def calculate_infeasibility(assignment_hours, availability):
    valid = True
    infeasibility = 0
    for i in range(len(assignment_hours)):
        if assignment_hours[i] > availability[i]:
            infeasibility += assignment_hours[i] - availability[i]

    return infeasibility

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

def tabu_search(file_name, max_iter=100, tabu_size=10, P=2, verbose=False):
    np, nm, costs, hours, availability = read_input_file(file_name)

    best_assignment = generate_initial_solution(np, nm, hours, availability)
    best_hours = calculate_hours(best_assignment, hours, nm)
    best_infeasibility = calculate_infeasibility(best_hours, availability)
    best_cost = calculate_cost(best_assignment, best_infeasibility, costs, P)

    best_global_assignment = best_assignment[:]
    best_global_hours = best_hours[:]
    best_global_cost = best_cost

    if verbose:
        print("Initial solution:")
        print("Best assignment:")
        for row in best_assignment:
            print(row)
        print(f"Best cost:\t {best_cost}")
        print(f"Hours used:\t {best_hours}")
        print(f"Availability:\t {availability}")
        print()
    
    tabu_list = []

    for it in range(max_iter):
        neighbors = get_neighbors(best_assignment)

        best_neighbor = None
        best_neighbor_cost = float('inf')
        best_neighbor_hours = []

        neighbors_hours = []

        for neighbor in neighbors:
            aux = calculate_hours(neighbor, hours, nm)
            neighbors_hours.append(aux)

        neighbors_infeasibility = [calculate_infeasibility(neighbor_hours, availability) for neighbor_hours in neighbors_hours]

        neighbors_cost = [calculate_cost(neighbor, neighbor_infeasibility, costs, P) for neighbor, neighbor_infeasibility in zip(neighbors, neighbors_infeasibility)]

        for neighbor, neighbor_cost, neighbor_hours in zip(neighbors, neighbors_cost, neighbors_hours):
            if neighbor_cost < best_neighbor_cost and neighbor not in tabu_list:
                best_neighbor = neighbor
                best_neighbor_cost = neighbor_cost
                best_neighbor_hours = neighbor_hours

        if best_neighbor is None:
            break

        best_assignment = best_neighbor
        best_cost = best_neighbor_cost
        best_hours = best_neighbor_hours

        aux = calculate_hours(best_assignment, hours, nm)
        valid = True
        for n_hours, n_avaib in zip(aux, availability):
            if n_hours > n_avaib:
                valid = False
                break

        if best_cost < best_global_cost and valid:
            best_global_assignment = best_assignment
            best_global_cost = best_cost
            best_global_hours = best_hours

        tabu_list.append(best_assignment)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        if verbose:
            print(f"Iteration {it}:")
            print("Best assignment:")
            for row in best_assignment:
                print(row)
            print(f"Best cost:\t {best_cost}")
            print(f"Hours used:\t {best_hours}")
            print(f"Availability:\t {availability}")
            print()

    return best_global_assignment, best_global_cost, best_global_hours, availability

best_assignment, best_cost, best_hours, availability = tabu_search('PDG1.txt', max_iter=100, tabu_size=10, P=1.3, verbose=True)
print("Best valid result:")
print("Assignment:")
for row in best_assignment:
    print(row)
print(f"Cost:\t {best_cost}")
print(f"Hours used:\t {best_hours}")
print(f"Availability:\t {availability}")
print()