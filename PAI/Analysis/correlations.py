# calculating the correlation between two sets of values
def calculate_correlation(x_values, y_values):

    # checking if both sets have the same number of values
    if len(x_values) != len(y_values):
        return 0

    # checking if there are not enough values for correlation
    if len(x_values) < 2:
        return 0

    # calculating the average of both sets
    x_average = sum(x_values) / len(x_values)
    y_average = sum(y_values) / len(y_values)

    # creating variables to store the correlation calculation
    numerator = 0
    x_difference = 0
    y_difference = 0

    # calculating the differences between each value and its average
    for i in range(len(x_values)):

        x_diff = x_values[i] - x_average
        y_diff = y_values[i] - y_average

        numerator += x_diff * y_diff
        x_difference += x_diff ** 2
        y_difference += y_diff ** 2

    # checking if correlation cannot be calculated
    if x_difference == 0 or y_difference == 0:
        return 0

    # calculating the correlation value
    correlation = numerator / (x_difference ** 0.5 * y_difference ** 0.5)

    return correlation


# converting the energy level into a numerical score
def convert_energy(score):

    if score == "High":
        return 3

    elif score == "Medium":
        return 2

    elif score == "Low":
        return 1

    return 0


# converting the satisfaction level into a numerical score
def convert_satisfaction(score):

    if score == "Very Satisfied":
        return 5

    elif score == "Satisfied":
        return 4

    elif score == "Neutral":
        return 3

    elif score == "Unsatisfied":
        return 2

    elif score == "Very Unsatisfied":
        return 1

    return 0


# finding the important relationships in the activity data
def find_key_findings(valid_days):

    # creating lists to store the required daily values
    sleep_values = []
    energy_values = []

    study_values = []
    satisfaction_values = []

    coding_values = []

    # collecting values from every valid recorded day
    for day in valid_days:

        sleep_values.append(day["sleep"] or 0)
        energy_values.append(convert_energy(day["energy"]))

        study_values.append(day["study"] or 0)
        satisfaction_values.append(
            convert_satisfaction(day["satisfaction"])
        )

        coding_values.append(day["coding"] or 0)

    # calculating the required correlations
    sleep_energy = calculate_correlation(
        sleep_values,
        energy_values
    )

    study_satisfaction = calculate_correlation(
        study_values,
        satisfaction_values
    )

    coding_energy = calculate_correlation(
        coding_values,
        energy_values
    )

    # storing all key findings
    findings = [
        {
            "name": "Sleep ↔ Energy",
            "correlation": sleep_energy
        },
        {
            "name": "Study ↔ Satisfaction",
            "correlation": study_satisfaction
        },
        {
            "name": "Coding ↔ Energy",
            "correlation": coding_energy
        }
    ]

    return findings