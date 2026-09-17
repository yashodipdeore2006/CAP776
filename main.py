from PAI import (
    read_data,
    get_valid_days,
    calculate_tpi,
    calculate_aai,
    calculate_phai,
    calculate_sri,
    calculate_abi,
    calculate_tui,
    calculate_ei,
    calculate_dci,
    generate_insights
)


def main():

    file_path = "Data/12620514.xlsx"

    data = read_data(file_path)

    valid_days = get_valid_days(data)

    expected_days = len(data)

    tpi = calculate_tpi(valid_days)
    aai = calculate_aai(valid_days)
    phai = calculate_phai(valid_days)
    sri = calculate_sri(valid_days)
    abi = calculate_abi(valid_days)
    tui = calculate_tui(valid_days)
    ei = calculate_ei(valid_days)
    dci = calculate_dci(valid_days, expected_days)

    metrics = {
        "TPI": tpi,
        "AAI": aai,
        "PhAI": phai,
        "SRI": sri,
        "ABI": abi,
        "TUI": tui,
        "EI": ei,
        "DCI": dci
    }

    insights = generate_insights(metrics)

    print("\n===== PERSONAL ACTIVITY ANALYSIS =====")

    print("Valid Days:", len(valid_days))
    print("TPI:", round(tpi, 2), "min/day")
    print("AAI:", round(aai, 2), "min/day")
    print("PhAI:", round(phai, 2), "min/day")
    print("SRI:", round(sri, 2), "min/day")
    print("ABI:", round(abi, 2), "min/day")
    print("TUI:", round(tui, 2), "min/day")
    print("EI:", round(ei, 2), "/5")
    print("DCI:", round(dci, 2), "%")

    print("\n===== INSIGHTS =====")

    for insight in insights:
        print("-", insight)


if __name__ == "__main__":
    main()