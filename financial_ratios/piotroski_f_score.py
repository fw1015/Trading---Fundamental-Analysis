
# PIOTROSKI F SCORE

# PROFITABILITY
# [[POSITIVE ROA],
# [POSITIVE CASHFLOW FROM OPERATIONS],
# [ROA > PREVIOUS ROA],
# [CFROA > ROA],

# FUNDING
# [DEBT/ASSETS < PREVIOUS DEBT/ASSETS],
# [CURRENT RATIO > PREVIOUS CURRENT RATIO],
# [SHARES OUTSTANDING < PREVIOUS SHARES OUTSTANDING],

# EFFICIENCY
# [GROSS PROFIT MARGIN > PREVIOUS GROSS PROFIT MARGIN],
# [TOTAL ASSET TURNOVER RATIO > PREVIOUS TOTAL ASSET TURNOVER RATIO]]

def pio_f_score(roa_arr, cfroa_arr, debt_to_assets_arr, cur_ratio_arr, gr_profit_mgn_arr, tot_assets_turnover_arr, income_statement, cashflow_statement, num_yr):
    pio_f_score_arr = []

    op_csh_arr = []
    shs_out_arr = []

    for yr in range(num_yr - 1):
        op_csh = cashflow_statement[yr]["netCashProvidedByOperatingActivities"]
        op_csh_arr.append(op_csh)

        sh_out = income_statement[yr]["weightedAverageShsOut"]
        shs_out_arr.append(sh_out)

    for yr in range(num_yr - 2):
        # Q1
        if roa_arr[yr] > 0:
            q1 = 1
        else:
            q1 = 0

        # Q2
        if op_csh_arr[yr] > 0:
            q2 = 1
        else:
            q2 = 0

        # Q3
        if roa_arr[yr] > roa_arr[yr + 1]:
            q3 = 1
        else:
            q3 = 0

        # Q4
        if cfroa_arr[yr] > roa_arr[yr]:
            q4 = 1
        else:
            q4 = 0

        # Q5
        if debt_to_assets_arr[yr] < debt_to_assets_arr[yr + 1]:
            q5 = 1
        else:
            q5 = 0

        # Q6
        if cur_ratio_arr[yr] > cur_ratio_arr[yr + 1]:
            q6 = 1
        else:
            q6 = 0

        # Q7
        if shs_out_arr[yr] < shs_out_arr[yr + 1]:
            q7 = 1
        else:
            q7 = 0

        # Q8
        if gr_profit_mgn_arr[yr] > gr_profit_mgn_arr[yr + 1]:
            q8 = 1
        else:
            q8 = 0

        # Q9
        if tot_assets_turnover_arr[yr] > tot_assets_turnover_arr[yr + 1]:
            q9 = 1
        else:
            q9 = 0

        # TOTAL Q
        q = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9

        if q >= 0 and q <= 3:
            rating = "Low Score"
        elif q >= 4 and q <= 6:
            rating = "Average Score"
        elif q >= 7:
            rating = "High Score"

        pio_f_score_arr.append(rating)

    return pio_f_score_arr

