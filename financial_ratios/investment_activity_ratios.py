
# INVESTMENT ACTIVITY RATIOS
# [[NET FIXED ASSET TURNOVER],
# [TOTAL ASSET TURNOVER],
# ]

def inv_analysis(income_statement, balance_sheet, num_yr):

    inv_act_ratios = []
    fixed_assets_turnover_arr = []
    tot_assets_turnover_arr = []

    # DATA 5 YEARS AVERAGE
    # AVERAGE PP&E NET, AVERAGE TOTAL ASSETS
    av_ppne_arr = []
    av_tot_assets_sum_arr = []
    for yr in range(num_yr - 1):
        yr_bal = balance_sheet[yr]
        nxt_yr_bal = balance_sheet[yr + 1]

        # AVERAGE PP&E NET
        av_ppne_arr.append((yr_bal["propertyPlantEquipmentNet"] + nxt_yr_bal["propertyPlantEquipmentNet"]) / 2)

        # AVERAGE TOTAL ASSETS
        av_tot_assets_sum_arr.append((yr_bal["totalAssets"] + nxt_yr_bal["totalAssets"]) / 2)

    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]
        net_sales = yr_inc["revenue"]

        # FIXED ASSETS TURNOVER
        fixed_assets_turnover = net_sales / av_ppne_arr[yr]
        fixed_assets_turnover_arr.append(fixed_assets_turnover)

        # TOTAL ASSETS TURNOVER
        tot_assets_turnover = net_sales / av_tot_assets_sum_arr[yr]
        tot_assets_turnover_arr.append(tot_assets_turnover)

    inv_act_ratios.append(fixed_assets_turnover_arr)
    inv_act_ratios.append(tot_assets_turnover_arr)

    return inv_act_ratios
