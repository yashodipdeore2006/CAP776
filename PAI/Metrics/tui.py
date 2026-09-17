# calculating average total tracked time
def calculate_tui(valid_days):

    # checking if there are no valid days
    if len(valid_days) == 0:
        return 0

    # storing total tracked time
    total_tracked_time = 0

    # adding tracked time of each day
    for day in valid_days:

        tracked_time = day["total_tracked"] or 0

        total_tracked_time += tracked_time

    # calculating average tracked time
    tui = total_tracked_time / len(valid_days)

    return tui