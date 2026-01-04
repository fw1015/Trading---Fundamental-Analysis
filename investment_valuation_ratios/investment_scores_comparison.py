from investment_valuation_ratios.historic_results import *
from investment_valuation_ratios.yield_ratios import *

def inv_sc_compare(target, tickers_r_dict, year):
    target_ratios = tickers_r_dict[target]
    tickers_r_dict.pop(target, None)
    comp_score_arr = {}

    # COMPARE WITH OTHER TICKERS
    # tickers_r_dict = {ticker : [[price_r], [ev_val_r], [yield_r]]}
    for competitor in tickers_r_dict:
        competitor_ratios = tickers_r_dict[competitor]
        comp_score_arr[competitor] = comparing_loop(target_ratios, competitor_ratios, competitor)

    # COMPARE WITH HISTORY
    historic_ratios = historic_results(target_ratios)
    comp_score_arr["History"] = comparing_loop(target_ratios, historic_ratios, "History")

    # COMPARE WITH MARKET
    market_y = market_yield(year)
    comp_score_arr["S&P 500"] = comparing_loop(target_ratios, market_y[0], "S&P 500")
    comp_score_arr["10 Years Treasury"] = comparing_loop(target_ratios, market_y[1], "10 Years Treasury")

    return comp_score_arr

def comparing_loop(target_ratios, comparing_ratios, comparing_target):
    rating_arr = []
    if comparing_target == "S&P 500" or comparing_target == "10 Years Treasury":
        score = 0
        # target_ratios = [[price_r], [ev_val_r], [yield_r]]
        # target_ratio = target_ratios[2]
        # target_ratio = [yield_r]
        # target_ratio = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # target_ratio = [Earnings yield, Dividends Yield, Dividends Payout]
        target_ratio = target_ratios[2]
        ratio_count = len(target_ratio)
        if comparing_target == "10 Years Treasury":
            ratio_count = len(target_ratio) - 1
        for j in range(ratio_count):
            # comparing_ratios = [[0, 0, 0], [0, 0]]
            # comparing_ratios = [[Earnings yield, Dividends Yield, Dividends Payout]]
            # measure_ratio = [Earnings yield]
            measure_ratio = comparing_ratios[j]
            if target_ratio[j][0] > measure_ratio:
                score += 1
            else:
                score += 0
        yield_score = score / ratio_count
        rating_arr.append(yield_score)
    else:
        # target_ratios = [[price_r], [ev_val_r], [yield_r]]
        for i in range(len(target_ratios)):
            score = 0
            # target_ratios[i] = [price_r]
            # target_ratios[i][j] = [[PE], [PS], [PB], [POCF]]
            # target_ratios[i][j][0] = first yr PE
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

            over_val_score = score / len(target_ratios[i])
            under_val_score = 1 - over_val_score

            if i == 2:
                rating_arr.append(over_val_score)
            else:
                rating_arr.append([over_val_score, under_val_score])

    return rating_arr