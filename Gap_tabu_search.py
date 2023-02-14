from Gen_init_solution import generate_initial_solution
from Get_neighbors import get_neighbors
from Calculations import calculate_cost, calculate_hours, calculate_infeasibility
from Read_input_file import read_input_file
from Results import print_results

def tabu_search(file_name, max_iter=100, tabu_size=10, P=1.3, verbose=True):
    np, nm, costs, hours, availability = read_input_file(file_name)

    best_assignment = generate_initial_solution(np, nm, hours, availability)
    best_hours = calculate_hours(best_assignment, hours, nm)
    best_infeasibility = calculate_infeasibility(best_hours, availability)
    best_cost = calculate_cost(best_assignment, best_infeasibility, costs, P)

    best_global_assignment = best_assignment[:]
    best_global_hours = best_hours[:]
    best_global_cost = best_cost

    print_results(best_assignment, best_cost, best_hours, availability, initial=True)
    
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
            print_results(best_assignment, best_cost, best_hours, availability, it)

    return best_global_assignment, best_global_cost, best_global_hours, availability