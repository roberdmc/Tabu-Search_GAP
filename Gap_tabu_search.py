from Gen_init_solution import generate_initial_solution
from Get_neighbors import get_neighbors
from Calculations import calculate_cost, calculate_hours, calculate_infeasibility
from Read_input_file import read_input_file
from Results import print_results

def tabu_search(file_name, max_iter=100, tabu_size=10, P=1.3, verbose=True):
    #Separando os dados do arquivo
    num_prog, num_mod, costs, hours, availability = read_input_file(file_name)

    #Gerando a solução inicial
    best_assignment = generate_initial_solution(num_prog, num_mod, hours, availability)
    #Calculando as horas gastas por cada programador
    best_hours = calculate_hours(best_assignment, hours, num_mod)
    #Calculando inviabilidade (horas estouradas)
    best_infeasibility = calculate_infeasibility(best_hours, availability)
    #Calculando custo total
    best_cost = calculate_cost(best_assignment, best_infeasibility, costs, P)

    #Copiando os resultados iniciais para a primeira solução global
    #Aqui ficarão os melhores resultados válidos (Sem estouro)
    best_global_assignment = best_assignment[:]
    best_global_hours = best_hours[:]
    best_global_infeasibility = best_infeasibility
    best_global_cost = best_cost

    #Printa a solução inicial, mostrando se é válida ou não
    if best_infeasibility==0:
        print_results(best_assignment, int(best_cost-(best_infeasibility*P)), best_hours, availability, feasible=True, initial=True)
    else:
        print_results(best_assignment, int(best_cost-(best_infeasibility*P)), best_hours, availability, initial=True)
    
    #Iniciando a lista tabu
    tabu_list = []

    #Iniciando a busca tabu, com o máximo de iterações definido
    for it in range(max_iter):
        #Gerando os vizinhos para a melhor solução da iteração anterior
        #Cada vizinho bagunça um bit da solução
        neighbors = get_neighbors(best_assignment)

        #Inicialmente, melhor vizinho é vazio e melhor custo infinito
        #Para qualquer valor sobrescrevê-los
        best_neighbor = None
        best_neighbor_cost = float('inf')
        #Armazena as horas gastas por cada programador do melhor vizinho
        best_neighbor_hours = []
        #Armazena a inviabilidade (horas estouradas pela solução). Se 0, a solução é válida
        best_neighbor_infeasibility = 0

        #Armazena as horas gastas por cada programador, em cada vizinho
        neighbors_hours = []

        #Calcula as horas gastas por programdor, em cada vizinho
        for neighbor in neighbors:
            aux = calculate_hours(neighbor, hours, num_mod)
            neighbors_hours.append(aux)

        #Calcula a inviabilidade de cada vizinho
        neighbors_infeasibility = [calculate_infeasibility(neighbor_hours, availability) for neighbor_hours in neighbors_hours]

        #Calcula o custo total de cada vizinho
        neighbors_cost = [calculate_cost(neighbor, neighbor_infeasibility, costs, P) for neighbor, neighbor_infeasibility in zip(neighbors, neighbors_infeasibility)]

        #Percorrendo os vizinhos, para encontrar o melhor (válido ou não, considerando penalidade)
        for neighbor, neighbor_cost, neighbor_hours, neighbor_infeasibility in zip(neighbors, neighbors_cost, neighbors_hours, neighbors_infeasibility):
            #Se o vizinho for melhor que os demais e não estiver na lista tabu, vira o melhor da iteração
            if neighbor_cost < best_neighbor_cost and neighbor not in tabu_list:
                best_neighbor = neighbor
                best_neighbor_cost = neighbor_cost
                best_neighbor_hours = neighbor_hours
                best_neighbor_infeasibility = neighbor_infeasibility

        #Critério de parada, quando não encontra nenhum melhor vizinho em alguma iteração
        if best_neighbor is None:
            break

        #Atribui o melhor vizinho encontrado como melhor solução da busca, para usá-lo na próxima iteração
        best_assignment = best_neighbor
        best_cost = best_neighbor_cost
        best_hours = best_neighbor_hours
        best_infeasibility = best_neighbor_infeasibility

        #aux = calculate_hours(best_assignment, hours, num_mod)
        #valid = True
        #for n_hours, n_avaib in zip(best_hours, availability):
        #    if n_hours > n_avaib:
        #        valid = False
        #        break

        #Se a melhor solução da iteração for válida e for melhor que a solução global, vira a melhor global
        if best_cost < best_global_cost and best_infeasibility==0:
            best_global_infeasibility = best_infeasibility
            best_global_assignment = best_assignment
            best_global_cost = best_cost
            best_global_hours = best_hours

        #Inclui na lista tabu, a melhor solução encontrada na iteração
        tabu_list.append(best_assignment)
        #Se a lista estiver maior que o limite, tira o mais antigo
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        #Se verbose, printa os melhores resultados da iteração e informa se a solução é válida ou não
        if verbose:
            if best_neighbor_infeasibility == 0:
                print_results(best_assignment, int(best_cost-(best_neighbor_infeasibility*P)), best_hours, availability, it, feasible=True)
            else:
                print_results(best_assignment, int(best_cost-(best_neighbor_infeasibility*P)), best_hours, availability, it)

    #Retorna a melhor solução global, melhor custo (corrigindo a penalidade), horas gastas e disponibilidade
    return best_global_assignment, int(best_global_cost-(best_global_infeasibility*P)), best_global_hours, availability