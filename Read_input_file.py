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