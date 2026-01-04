
# PROFITABILITY RATIOS
# [[GROSS PROFIT MARGIN],
# [OPERATING PROFIT MARGIN],
# [NET PROFIT MARGIN],
# [RETURN ON EQUITY (ROE)],
# [RETURN ON ASSETS (ROA)],
# [RETURN ON INVESTED CAPITAL (ROIC)],
# [CASH FLOW RETURN ON ASSET RATIO (CFROA)]]

def profit_analysis(income_statement, balance_sheet, cashflow_statement, num_yr):
    profit_ratios = []

    gr_profit_mgn_arr = []
    op_profit_mgn_arr = []
    net_profit_mgn_arr = []
    roe_arr = []
    roa_arr = []
    roic_arr = []
    cfroa_arr = []

    # DATA 5 YEARS AVERAGE
    # AVERAGE SHAREHOLDERS' EQUITY, AVERAGE TOTAL ASSETS, AVERAGE INVESTED CAPITAL
    sh_eq_arr = []
    tot_assets_arr = []
    inv_cap_arr = []
    for yr in range(num_yr):
        yr_bal = balance_sheet[yr]

        tot_assets = yr_bal["totalAssets"]
        tot_assets_arr.append(tot_assets)

        sh_eq = yr_bal["totalStockholdersEquity"] + yr_bal["othertotalStockholdersEquity"]
        if sh_eq == 0:
            sh_eq = tot_assets - yr_bal["totalLiabilities"]
        sh_eq_arr.append(sh_eq)

        sh_term_debt = yr_bal["shortTermDebt"]
        cur_long_term_debt = yr_bal["otherCurrentLiabilities"]
        long_term_debt = yr_bal["longTermDebt"]
        tot_sh_eq = yr_bal["totalStockholdersEquity"]
        csh_csh_eq = yr_bal["cashAndCashEquivalents"]

        inv_cap = sh_term_debt + cur_long_term_debt + long_term_debt + tot_sh_eq - csh_csh_eq
        inv_cap_arr.append(inv_cap)

    av_sh_eq_arr = []
    av_tot_assets_arr = []
    av_inv_cap_arr = []
    for yr in range(num_yr - 1):
        # AVERAGE SHAREHOLDERS' EQUITY
        av_sh_eq_arr.append((sh_eq_arr[yr] + sh_eq_arr[yr + 1]) / 2)

        # AVERAGE TOTAL ASSETS
        av_tot_assets_arr.append((tot_assets_arr[yr] + tot_assets_arr[yr + 1]) / 2)

        # AVERAGE INVESTED CAPITAL
        av_inv_cap_arr.append((inv_cap_arr[yr] + inv_cap_arr[yr + 1]) / 2)

    # CALCULATE PROFITABILITY RATIOS FOR EACH YEAR
    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]

        gr_mgn = yr_inc["grossProfit"]
        net_sales = yr_inc["revenue"]
        op_inc = yr_inc["operatingIncome"]
        net_inc = yr_inc["netIncome"]

        ebitda = yr_inc["ebitda"]
        depre_amort = yr_inc["depreciationAndAmortization"]
        ebit = ebitda - depre_amort

        inc_tax = yr_inc["incomeTaxExpense"]
        ebt = yr_inc["incomeBeforeTax"]
        eff_tax = inc_tax / ebt

        op_csh = cashflow_statement[yr]["netCashProvidedByOperatingActivities"]

        # GROSS PROFIT MARGIN
        gr_profit_mgn = gr_mgn / net_sales
        gr_profit_mgn_arr.append(gr_profit_mgn)

        # OPERATING PROFIT MARGIN
        op_profit_mgn = op_inc / net_sales
        op_profit_mgn_arr.append(op_profit_mgn)

        # NET PROFIT MARGIN
        net_profit_mgn = net_inc / net_sales
        net_profit_mgn_arr.append(net_profit_mgn)

        # RETURN ON EQUITY (ROE)
        roe = net_inc / av_sh_eq_arr[yr]
        roe_arr.append(roe)

        # RETURN ON ASSETS (ROA)
        roa = net_inc / av_tot_assets_arr[yr]
        roa_arr.append(roa)

        # RETURN ON INVESTED CAPITAL (ROIC)
        roic = (ebit * (1 - eff_tax)) / av_inv_cap_arr[yr]
        roic_arr.append(roic)

        # CASH FLOW RETURN ON ASSET RATIO (CFROA)
        cfroa = op_csh / av_tot_assets_arr[yr]
        cfroa_arr.append(cfroa)

    profit_ratios.append(gr_profit_mgn_arr)
    profit_ratios.append(op_profit_mgn_arr)
    profit_ratios.append(net_profit_mgn_arr)
    profit_ratios.append(roe_arr)
    profit_ratios.append(roa_arr)
    profit_ratios.append(roic_arr)
    profit_ratios.append(cfroa_arr)

    return profit_ratios
