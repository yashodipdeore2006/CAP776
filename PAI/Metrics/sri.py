# calculating the average amount of sleep time recorded for each valid day
def calculate_sri(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total sleep time of all valid days
    total_sleep_time = 0

    # adding the sleep time recorded for each valid day
    for day in valid_days:

        sleep_time = day["sleep"] or 0

        total_sleep_time += sleep_time

    # calculating the average sleep time from the total sleep time
    sri = total_sleep_time / len(valid_days)

    return sri