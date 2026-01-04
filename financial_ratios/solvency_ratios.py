
# SOLVENCY RATIOS
# [[DEBT TO EQUITY],
# [INTEREST COVERAGE],
# [EQUITY MULTIPLIER],
# [DEBT TO ASSETS],
# ]

def sol_analysis(income_statement, balance_sheet, num_yr):

    sol_ratios = []
    debt_to_eq_arr = []
    int_cov_arr = []
    eq_multi_arr = []
    debt_to_assets_arr = []

    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]

        ebitda = yr_inc["ebitda"]
        depre_amort = yr_inc["depreciationAndAmortization"]
        ebit = ebitda - depre_amort
        int_exp = yr_inc["interestExpense"]

        # INTEREST COVERAGE
        int_cov = ebit / int_exp
        int_cov_arr.append(int_cov)

    for yr in range(num_yr - 1):
        yr_bal = balance_sheet[yr]
        lt_debt = yr_bal["longTermDebt"]
        tot_assets = yr_bal["totalAssets"]

        tot_sh_eq = yr_bal["totalStockholdersEquity"] + yr_bal["othertotalStockholdersEquity"]
        if tot_sh_eq == 0:
            tot_sh_eq = tot_assets - yr_bal["totalLiabilities"]


        # DEBT TO EQUITY RATIO
        debt_to_eq = lt_debt / tot_sh_eq
        debt_to_eq_arr.append(debt_to_eq)

        # EQUITY MULTIPLIER
        eq_multi = tot_assets / tot_sh_eq
        eq_multi_arr.append(eq_multi)

        # DEBT TO ASSETS RATIO
        debt_to_assets = lt_debt / tot_assets
        debt_to_assets_arr.append(debt_to_assets)

    sol_ratios.append(debt_to_eq_arr)
    sol_ratios.append(int_cov_arr)
    sol_ratios.append(eq_multi_arr)
    sol_ratios.append(debt_to_assets_arr)

    return sol_ratios
