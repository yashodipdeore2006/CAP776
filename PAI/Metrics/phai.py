# calculating average fitness time
def calculate_phai(valid_days):

    # checking if there are no valid days
    if len(valid_days) == 0:
        return 0

    # storing total fitness time
    total_fitness_time = 0

    # adding fitness time of each day
    for day in valid_days:

        fitness_time = day["fitness"] or 0

        total_fitness_time += fitness_time

    # calculating average fitness time
    phai = total_fitness_time / len(valid_days)

    return phai