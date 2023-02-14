def print_results(best_assignment, best_cost, best_hours, availability, it=0, feasible=False, initial = False, final=False):
    if final:
        print()
        print("---- Tabu Search completed successfully ----")
        print()
        print("--- Best valid result: ---")
    elif initial:
        print()
        print("--- Initial solution: ---")
    else:
        print()
        print(f"--- Iteration {it}: ---")
        if feasible:
            print("--- Best neighbor (Valid): ---")
        else:
            print("--- Best neighbor (Not valid): ---")
    print("Assignment:")
    for row in best_assignment:
        print("\t\t",row)
    print(f"Cost: {best_cost}")
    print(f"Hours used:\t {best_hours}")
    print(f"Availability:\t {availability}")
    print()
