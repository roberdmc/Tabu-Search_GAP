def read_input_file(file_name):
    with open(file_name) as file:
        num_prog = int(file.readline().strip())
        num_mod = int(file.readline().strip())
        costs = []
        for i in range(num_prog):
            row = list(map(int, file.readline().strip().split()))
            costs.append(row)
        hours = []
        for i in range(num_prog):
            row = list(map(int, file.readline().strip().split()))
            hours.append(row)
        availability = list(map(int, file.readline().strip().split()))
    return num_prog, num_mod, costs, hours, availability