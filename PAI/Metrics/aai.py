# calculating the average academic activity time from study and class time
def calculate_aai(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total academic activity time
    total_academic_time = 0

    # adding study time and class time recorded for each valid day
    for day in valid_days:

        study_time = day["study"] or 0
        class_time = day["class"] or 0

        total_academic_time += study_time + class_time

    # calculating the average academic activity time per valid day
    aai = total_academic_time / len(valid_days)

    return aai


# calculating the average amount of study time recorded for each valid day
def calculate_average_study(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total study time
    total_study_time = 0

    # adding the study time recorded for each valid day
    for day in valid_days:

        study_time = day["study"] or 0

        total_study_time += study_time

    # calculating the average study time per valid day
    average_study = total_study_time / len(valid_days)

    return average_study


# calculating the average amount of class time recorded for each valid day
def calculate_average_class(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total class time
    total_class_time = 0

    # adding the class time recorded for each valid day
    for day in valid_days:

        class_time = day["class"] or 0

        total_class_time += class_time

    # calculating the average class time per valid day
    average_class = total_class_time / len(valid_days)

    return average_class