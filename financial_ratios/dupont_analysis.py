
# DUPONT ANALYSIS
# [RETURN ON EQUITY]

def du_pont_anlysis(net_profit_mgn_arr, tot_asset_turnover_arr, eq_multi_arr, num_yr):
    du_pont_roe_arr = []

    for yr in range(num_yr - 1):
        du_pont_roe = net_profit_mgn_arr[yr] * tot_asset_turnover_arr[yr] * eq_multi_arr[yr]
        du_pont_roe_arr.append(du_pont_roe)

    return du_pont_roe_arr
