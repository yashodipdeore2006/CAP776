from PAI import (
    read_data,
    get_valid_days,
    calculate_tpi,
    calculate_aai,
    calculate_average_study,
    calculate_average_class,
    calculate_phai,
    calculate_sri,
    calculate_abi,
    calculate_average_other_activities,
    calculate_tui,
    calculate_ei,
    calculate_dci,
    calculate_pai,
    find_key_findings
)


def main():

    file_path = "12620514.xlsx"

    data = read_data(file_path)

    valid_days = get_valid_days(data)

    expected_days = len(data)

    # Calculate index values
    tpi = calculate_tpi(valid_days)
    aai = calculate_aai(valid_days)
    phai = calculate_phai(valid_days)
    sri = calculate_sri(valid_days)
    abi = calculate_abi(valid_days)
    tui = calculate_tui(valid_days)
    ei = calculate_ei(valid_days)
    dci = calculate_dci(valid_days, expected_days)

    pai = calculate_pai(
        tpi,
        aai,
        phai,
        sri,
        tui,
        ei,
        dci
    )

    # Calculate daily averages
    average_study = calculate_average_study(valid_days)
    average_class = calculate_average_class(valid_days)
    average_other_activities = calculate_average_other_activities(valid_days)

    # Calculate key findings
    key_findings = find_key_findings(valid_days)


    # ==========================================
    # 1. DAILY ACTIVITY
    # ==========================================

    print("\n===== DAILY ACTIVITY =====")
    print("Valid days recorded:", len(valid_days))
    
    print(
        "Average Sleep/day:",
        round(sri / 60, 2),
        "hours/day"
    )

    print(
        "Average Fitness/day:",
        round(phai, 2),
        "min/day"
    )

    print(
        "Average Study/day:",
        round(average_study, 2),
        "min/day"
    )

    print(
        "Average Coding/day:",
        round(tpi, 2),
        "min/day"
    )

    print(
        "Average Class/day:",
        round(average_class, 2),
        "min/day"
    )

    print(
        "Average Other Activities/day:",
        round(average_other_activities, 2),
        "min/day"
    )

    print(
        "Average Free / Unaccounted Time/day:",
        round(abi, 2),
        "min/day"
    )


    # ==========================================
    # 2. INDEX VALUES
    # ==========================================

    print("\n===== INDEX VALUES =====")

    print(
        "Personal Activity Index (PAI):",
        round(pai, 2)
    )

    print(
        "Tech Productivity (TPI):",
        round(tpi, 2),
        "min/day"
    )

    print(
        "Academic Activity (AAI):",
        round(aai, 2),
        "min/day"
    )

    print(
        "Physical Activity (PhAI):",
        round(phai, 2),
        "min/day"
    )

    print(
        "Sleep & Recovery (SRI):",
        round(sri, 2),
        "min/day"
    )

    print(
        "Activity Balance (ABI):",
        round(abi, 2),
        "min/day"
    )

    print(
        "Time Utilization (TUI):",
        round(tui, 2),
        "min/day"
    )

    print(
        "Experience Index (EI):",
        round(ei, 2),
        "/5"
    )

    print(
        "Data Continuity Index (DCI):",
        round(dci, 2),
        "%"
    )


    # ==========================================
    # 3. KEY FINDINGS
    # ==========================================

    print("\n===== KEY FINDINGS =====")

    for number, finding in enumerate(key_findings, 1):

        correlation = finding["correlation"]

        print(
            number,
            finding["name"] + ":",
            round(correlation, 2)
        )


if __name__ == "__main__":
    main()