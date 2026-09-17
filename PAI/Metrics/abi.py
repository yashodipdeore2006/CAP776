# calculating average free time
def calculate_abi(valid_days):

    # checking if there are no valid days
    if len(valid_days) == 0:
        return 0

    # storing total free time
    total_free_time = 0

    # adding free time of each day
    for day in valid_days:

        free_time = day["free_time"] or 0

        total_free_time += free_time

    # calculating average free time
    abi = total_free_time / len(valid_days)

    return abi