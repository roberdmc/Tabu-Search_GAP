def print_results(best_assignment, best_cost, best_hours, availability, it=0, initial = False, final=False):
    if final:
        print()
        print("---- Tabu Search completed successfully ----")
        print()
        print("--- Best valid result: ---")
    elif not initial:
        print()
        print(f"--- Iteration {it}: ---")
        print("--- Best result: ---")
    else:
        print("--- Initial solution: ---")
    print("Assignment:")
    for row in best_assignment:
        print("\t\t",row)
    print(f"Cost:\t\t {best_cost}")
    print(f"Hours used:\t {best_hours}")
    print(f"Availability:\t {availability}")
    print()