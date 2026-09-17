# checking if the day data is valid
def is_valid_day(day):

    # checking if date is available
    if day["date"] is None:
        return False

    # checking if basic activity data is available
    if day["sleep"] is None and day["fitness"] is None and day["study"] is None:
        return False

    return True


# getting only valid days from all data
def get_valid_days(data):

    # storing valid days
    valid_days = []

    # checking each day
    for day in data:

        # adding valid day to the list
        if is_valid_day(day):
            valid_days.append(day)

    return valid_days