def calculate_infeasibility(assignment_hours, availability):
    valid = True
    infeasibility = 0
    for i in range(len(assignment_hours)):
        if assignment_hours[i] > availability[i]:
            infeasibility += assignment_hours[i] - availability[i]

    return infeasibility

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