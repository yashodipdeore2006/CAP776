def calculate_tpi(valid_days):

    if len(valid_days) == 0:
        return 0

    total_coding_time = 0

    for day in valid_days:

        total_coding_time += day["coding"]

    tpi = total_coding_time / len(valid_days)

    return tpi