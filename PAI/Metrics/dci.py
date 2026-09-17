def calculate_dci(valid_days, expected_days):

    if expected_days == 0:
        return 0

    valid_recorded_days = len(valid_days)

    dci = (valid_recorded_days / expected_days) * 100

    return dci