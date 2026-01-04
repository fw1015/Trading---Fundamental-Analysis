import numpy as np

def historic_results(target_ratios):
    # history_arr = [[]]
    historic_arr = []

    for fin_ratios in target_ratios:
        avg_ratio_arr = []
        for ratio in fin_ratios:
            avg_ratio = np.mean(ratio)
            avg_ratio_arr.append(avg_ratio)
        historic_arr.append(avg_ratio_arr)
    return historic_arr