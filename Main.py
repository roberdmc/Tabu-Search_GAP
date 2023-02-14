from Gap_tabu_search import tabu_search
from Clear_screen import clear_screen
from Results import print_results
from Menu import type_menu, menu, menu_default

if __name__ == "__main__":
    default_values = type_menu()

    if default_values:
        file_name_default = menu_default()
        best_assignment, best_cost, best_hours, availability = tabu_search(file_name_default)
    else:
        file_name, max_iter, tabu_size, P, verbose = menu()
        best_assignment, best_cost, best_hours, availability = tabu_search(file_name, max_iter, tabu_size, P, verbose)
    
    print_results(best_assignment, best_cost, best_hours, availability, final=True)