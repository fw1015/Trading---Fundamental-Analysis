# PRICE RATIOS
# [[P/E],
# [P/S],
# [P/BV],
# [P/OCF]]

def price_ratios(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    # year = len(income_statement)
    p_ratios = []

    pe_arr = []
    ps_arr = []
    pbv_arr = []
    pocf_arr = []

    for yr in range(num_yr):
        yr_inc = income_statement[yr]
        yr_bal = balance_sheet[yr]
        yr_csh = cashflow_statement[yr]
        yr_ev = enterprise_value[yr]

        sh_price = yr_ev["stockPrice"]
        net_sales = yr_inc["netIncome"]
        sh_out_dil = yr_inc["weightedAverageShsOutDil"]

        sh_eq = yr_bal["totalStockholdersEquity"] + yr_bal["othertotalStockholdersEquity"]
        if sh_eq == 0:
            sh_eq = yr_bal["totalLiabilitiesAndStockholdersEquity"] - yr_bal["totalLiabilities"]

        sh_out = yr_inc["weightedAverageShsOut"]

        op_csh = yr_csh["netCashProvidedByOperatingActivities"]

        bv_per_sh = sh_eq / sh_out

        # P/E
        ern_per_sh_dil = net_sales / sh_out_dil
        pe = sh_price / ern_per_sh_dil
        pe_arr.append(pe)

        # P/S
        net_sales_per_sh = net_sales / sh_out_dil
        ps = sh_price / net_sales_per_sh
        ps_arr.append(ps)

        # P/B
        pbv = sh_price / bv_per_sh
        pbv_arr.append(pbv)

        # P/OCF
        pocf = sh_price / (op_csh / sh_out_dil)
        pocf_arr.append(pocf)

    p_ratios.append(pe_arr)
    p_ratios.append(ps_arr)
    p_ratios.append(pbv_arr)
    p_ratios.append(pocf_arr)

    return p_ratios