# ALTMAN Z SCORE
# [rating]

def alt_z_score(income_statement, balance_sheet, enterprise_value, num_yr):
    alt_z_sc = []

    # DATA 5 YEARS AVERAGE
    # AVERAGE TOTAL ASSETS
    av_tot_assets_arr = []
    for yr in range(num_yr - 1):
        yr_bal = balance_sheet[yr]
        nxt_yr_bal = balance_sheet[yr + 1]

        # AVERAGE TOTAL ASSETS
        av_tot_assets_arr.append((yr_bal["totalAssets"] + nxt_yr_bal["totalAssets"]) / 2)


    # INVENTORY TURNOVER, RECEIVABLES TURNOVER, PYABLES TURNOVER
    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]
        yr_bal = balance_sheet[yr]
        yr_ent_val = enterprise_value[yr]

        cur_assets = yr_bal["totalCurrentAssets"]
        cur_lia = yr_bal["totalCurrentLiabilities"]
        tot_assets = yr_bal["totalAssets"]
        retn_ern = yr_bal["retainedEarnings"]

        ebitda = yr_inc["ebitda"]
        depre_amort = yr_inc["depreciationAndAmortization"]
        ebit = ebitda - depre_amort

        market_val_sh = yr_ent_val["stockPrice"]
        sh_outstanding = yr_inc["weightedAverageShsOut"]
        market_val_eq = market_val_sh * sh_outstanding

        tot_lia = yr_bal["totalLiabilities"]

        net_sales = yr_inc["revenue"]

        # X1
        x1 = (cur_assets - cur_lia) / tot_assets

        # X2
        x2 = retn_ern / tot_assets

        # X3
        x3 = ebit / av_tot_assets_arr[yr]

        # X4
        x4 = market_val_eq / tot_lia

        # X5
        x5 = net_sales / av_tot_assets_arr[yr]

        z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1 * x5

        if z >= 2.99:
            rating = "Safe Zone"
        elif z >= 1.81 and z < 2.99:
            rating = "Grey Zone"
        elif z <1.81:
            rating = "Distress Zone"

        alt_z_sc.append(rating)

    return alt_z_sc