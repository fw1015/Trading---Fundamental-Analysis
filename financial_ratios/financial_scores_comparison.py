from financial_ratios.historic_results import *

# tickers_r_dict = {ticker : [op_act_r, inv_act_r, liq_r, sol_r, profit_r]}
def fin_sc_compare(target, tickers_r_dict):
    target_ratios = tickers_r_dict[target][0]
    target_ratings = tickers_r_dict[target][1]
    tickers_r_dict.pop(target, None)
    # comp_score_arr = {ticker : [x %, y %], ticker : [x %, y %]}
    comp_score_arr = {}

    # COMPARE WITH OTHER TICKERS
    for competitor in tickers_r_dict:
        competitor_ratios = tickers_r_dict[competitor]
        comp_score_arr[competitor] = comparing_loop(target_ratios, competitor_ratios, competitor)

    # COMPARE WITH HISTORY
    historic_ratios = historic_results(target_ratios)
    comp_score_arr["History"] = comparing_loop(target_ratios, historic_ratios, "History")

    # ADD BACK SELF RATINGS
    comp_score_arr[target] = target_ratings
    return comp_score_arr

def comparing_loop(target_ratios, comparing_ratios, comparing_target):
    avg_score_arr = []
    for i in range(len(target_ratios)):
        score = 0
        for j in range(len(target_ratios[i])):
            target_ratio = target_ratios[i][j][0]
            if comparing_target == "History":
                measure_ratio = comparing_ratios[i][j]
            else:
                measure_ratio = comparing_ratios[i][j][0]

            if target_ratio > measure_ratio:
                score += 1
            else:
                score += 0
        avg_score = score / len(target_ratios[i])
        avg_score_arr.append(avg_score)
    return avg_score_arr
