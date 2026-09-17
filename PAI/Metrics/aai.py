# calculating average academic activity time
def calculate_aai(valid_days):

    # checking if there are no valid days
    if len(valid_days) == 0:
        return 0

    # storing total academic time
    total_academic_time = 0

    # adding study and class time of each day
    for day in valid_days:

        study_time = day["study"] or 0
        class_time = day["class"] or 0

        total_academic_time += study_time + class_time

    # calculating average academic time
    aai = total_academic_time / len(valid_days)

    return aai