# converting the feeling, satisfaction and energy levels into numerical scores
def convert_score(score):

    # converting feeling levels into numerical values
    if score == "Excellent":
        return 5

    elif score == "Good":
        return 4

    elif score == "Neutral":
        return 3

    elif score == "Low":
        return 2

    elif score == "Stressed":
        return 1

    # converting satisfaction levels into numerical values
    elif score == "Very Satisfied":
        return 5

    elif score == "Satisfied":
        return 4

    elif score == "Unsatisfied":
        return 2

    elif score == "Very Unsatisfied":
        return 1

    # converting energy levels into numerical values
    elif score == "High":
        return 5

    elif score == "Medium":
        return 3

    elif score == "Low":
        return 1

    # returning zero when the value does not match any available option
    else:
        return 0


# calculating the average experience score from all valid recorded days
def calculate_ei(valid_days):

    # returning zero when there are no valid days available for calculation
    if len(valid_days) == 0:
        return 0

    # creating a variable to store the total experience score
    total_experience = 0

    # calculating the experience score for each valid day
    for day in valid_days:

        feeling = convert_score(day["feeling"])
        satisfaction = convert_score(day["satisfaction"])
        energy = convert_score(day["energy"])

        # calculating the average experience score for the current day
        daily_experience = (feeling + satisfaction + energy) / 3

        total_experience += daily_experience

    # calculating the average experience score across all valid days
    ei = total_experience / len(valid_days)

    return ei