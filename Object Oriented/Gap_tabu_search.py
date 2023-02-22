from Solution import Solution
from copy import deepcopy
from Get_neighbors import get_neighbors
from Read_input_file import read_input_file

def tabu_search(file_name, max_iter=100, tabu_size=10, P=1.3, verbose=True):
    #Separando os dados do arquivo
    num_prog, num_mod, costs, hours, availability = read_input_file(file_name)

    #Gerando a solução inicial
    best_solution = Solution([[0 for j in range(num_mod)] for i in range(num_prog)], costs, hours, availability, num_prog, num_mod, P)
    best_solution.gen_init_sol()
    best_solution.update()

    #Copiando os resultados iniciais para a primeira solução global
    #Aqui ficarão os melhores resultados válidos (Sem estouro)
    best_global_solution = deepcopy(best_solution)

    #Printa a solução inicial, mostrando se é válida ou não
    best_solution.print_results(initial=True)
    
    #Iniciando a lista tabu
    tabu_list = []

    #Iniciando a busca tabu, com o máximo de iterações definido
    for it in range(max_iter):
        #Gerando os vizinhos para a melhor solução da iteração anterior
        #Cada vizinho bagunça um bit da solução
        neighbors = get_neighbors(best_solution)

        #Inicialmente, melhor vizinho é vazio e melhor custo infinito
        #Para qualquer valor sobrescrevê-los
        best_neighbor = None
        best_cost = float("inf")

        #Percorrendo os vizinhos, para encontrar o melhor (válido ou não, considerando penalidade)
        for neighbor in neighbors:
            #Se o vizinho for melhor que os demais e não estiver na lista tabu, vira o melhor da iteração
            if neighbor.total_cost < best_cost and neighbor.assignment not in tabu_list:
                best_neighbor = deepcopy(neighbor)
                best_cost = best_neighbor.total_cost

        #Critério de parada, quando não encontra nenhum melhor vizinho em alguma iteração
        if best_neighbor is None:
            break

        #Atribui o melhor vizinho encontrado como melhor solução da busca, para usá-lo na próxima iteração
        best_solution = deepcopy(best_neighbor)

        #Se a melhor solução da iteração for válida e for melhor que a solução global, vira a melhor global
        if best_solution.total_cost < best_global_solution.total_cost and best_solution.infeasibility==0:
            best_global_solution = deepcopy(best_solution)

        #Inclui na lista tabu, a melhor solução encontrada na iteração
        tabu_list.append(best_solution.assignment)
        #Se a lista estiver maior que o limite, tira o mais antigo
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        #Se verbose, printa os melhores resultados da iteração e informa se a solução é válida ou não
        if verbose:
            best_solution.print_results(it)
           
    #Retorna a melhor solução global
    return best_global_solution