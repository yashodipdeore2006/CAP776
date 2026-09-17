def generate_insights(metrics):

    insights = []

    insights.append(
        "Average coding time: "
        + str(round(metrics["TPI"], 2))
        + " min/day."
    )

    insights.append(
        "Average academic activity: "
        + str(round(metrics["AAI"], 2))
        + " min/day."
    )

    insights.append(
        "Average fitness time: "
        + str(round(metrics["PhAI"], 2))
        + " min/day."
    )

    sleep_hours = metrics["SRI"] / 60

    insights.append(
        "Average sleep: "
        + str(round(sleep_hours, 2))
        + " hours/day."
    )

    insights.append(
        "Average free/unaccounted time: "
        + str(round(metrics["ABI"], 2))
        + " min/day."
    )

    insights.append(
        "Average total tracked time: "
        + str(round(metrics["TUI"], 2))
        + " min/day."
    )

    insights.append(
        "Average experience score: "
        + str(round(metrics["EI"], 2))
        + "/5."
    )

    insights.append(
        "Data continuity: "
        + str(round(metrics["DCI"], 2))
        + "%."
    )

    return insights