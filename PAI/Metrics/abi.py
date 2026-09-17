# calculating the average amount of free or unaccounted time per valid day
def calculate_abi(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total free time of all valid days
    total_free_time = 0

    # adding the free time recorded for each valid day
    for day in valid_days:

        free_time = day["free_time"] or 0

        total_free_time += free_time

    # calculating the average free time from the total free time
    abi = total_free_time / len(valid_days)

    return abi


# calculating the average amount of other activities recorded for each valid day
def calculate_average_other_activities(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total other activities time
    total_other_activities = 0

    # adding other activities time recorded for each valid day
    for day in valid_days:

        other_activities = day["other_activities"] or 0

        total_other_activities += other_activities

    # calculating the average other activities time per valid day
    average_other_activities = total_other_activities / len(valid_days)

    return average_other_activities