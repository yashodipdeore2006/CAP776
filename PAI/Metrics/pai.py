# calculating the Personal Activity Index using all activity index values
def calculate_pai(tpi, aai, phai, sri, tui, ei, dci):

    # applying the predefined weights to each activity index
    pai = (
        0.15 * tpi
        + 0.20 * aai
        + 0.15 * phai
        + 0.20 * sri
        + 0.15 * tui
        + 0.10 * ei
        + 0.05 * dci
    )

    return pai