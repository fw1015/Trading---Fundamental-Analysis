
# LIQUIDITY RATIOS
# [[CURRENT RATIO],
# [QUICK RATIO],
# ]

def liq_analysis(balance_sheet, num_yr):

    liq_ratios = []
    cur_ratio_arr = []
    quick_ratio_arr = []

    for yr in range(num_yr - 1):
        yr_bal = balance_sheet[yr]
        tot_cur_assets = yr_bal["totalCurrentAssets"]
        tot_cur_lia = yr_bal["totalCurrentLiabilities"]
        inv = yr_bal["inventory"]

        # CURRENT RATIO
        cur_ratio = tot_cur_assets / tot_cur_lia
        cur_ratio_arr.append(cur_ratio)

        # QUICK RATIO
        quick_ratio = (tot_cur_assets - inv) / tot_cur_lia
        quick_ratio_arr.append(quick_ratio)

    liq_ratios.append(cur_ratio_arr)
    liq_ratios.append(quick_ratio_arr)

    return liq_ratios