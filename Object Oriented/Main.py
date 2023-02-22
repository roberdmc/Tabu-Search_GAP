from Gap_tabu_search import tabu_search
from Menu import type_menu, menu, menu_default, rerun

if __name__ == "__main__":
    run = True
    while run:
        default_values = type_menu()
        if default_values:
            file_name = menu_default()
            best_solution = tabu_search(file_name)
        else:
            file_name, max_iter, tabu_size, P, verbose = menu()
            best_solution = tabu_search(file_name, max_iter, tabu_size, P, verbose)
        best_solution.print_results(final=True)
        run = rerun()