from financial_ratios.profitability_ratios import *
from investment_valuation_ratios.yield_ratios import *
from cost_of_equity_debt_and_capital.capital_asset_pricing_model import *

# FORECAST MODEL
# +1 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +2 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +3 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +4 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +5 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]

def discounted_dividends(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    yield_r_arr = yield_ratios(income_statement, cashflow_statement, enterprise_value, num_yr)
    profit_arr = profit_analysis(income_statement, balance_sheet, cashflow_statement, num_yr)
    exp_return = capm(income_statement, cashflow_statement, enterprise_value, num_yr)

    div_payout = yield_r_arr[2]
    roe = profit_arr[3]
    exp_return_a = exp_return[0]

    div_per_sh_dil_arr = []
    prat_arr = []
    gordon_arr = []

    sh_price_arr = []
    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]
        yr_csh = cashflow_statement[yr]
        yr_ev = enterprise_value[yr]

        sh_price = yr_ev["stockPrice"]
        sh_out_dil = yr_inc["weightedAverageShsOutDil"]
        div_paid = - yr_csh["dividendsPaid"]
        div_per_sh_dil = div_paid / sh_out_dil

        prat = (1 - div_payout[yr]) * roe[yr]
        gordon = (sh_price * exp_return_a[yr] - div_per_sh_dil) / (sh_price + div_per_sh_dil)

        div_per_sh_dil_arr.append(div_per_sh_dil)
        prat_arr.append(prat)
        gordon_arr.append(gordon)
        sh_price_arr.append(sh_price)


    div_growth_rate_H_model = [prat_arr]
    div_per_sh_arr = [div_per_sh_dil_arr]
    div_present_val = []

    forecast_tot_yr = 5
    for forecast_yr in range(1, forecast_tot_yr - 1):
        forecast_div_gr_arr = []
        for yr in range(num_yr - 1):
            forecast_div_gr = prat_arr[yr] + (((gordon_arr[yr] - prat_arr[yr]) * (forecast_yr)) / (forecast_tot_yr - 1))
            forecast_div_gr_arr.append(forecast_div_gr)
        div_growth_rate_H_model.append(forecast_div_gr_arr)
        div_growth_rate_H_model.append(gordon_arr)

    for forecast_yr in range(forecast_tot_yr):
        forecast_div_per_sh_arr = []
        for yr in range(num_yr - 1):
            forecast_div_per_sh = div_per_sh_arr[forecast_yr][yr] * (1 + div_growth_rate_H_model[forecast_yr][yr])
            forecast_div_per_sh_arr.append(forecast_div_per_sh)
        div_per_sh_arr.append(forecast_div_per_sh_arr)

    for forecast_yr in range(1, forecast_tot_yr):
        forecast_div_per_sh_pre_val_arr = []
        for yr in range(num_yr - 1):
            forecast_div_per_sh_pre_val = div_per_sh_arr[forecast_yr][yr] / ((1 + exp_return_a[yr]) ** forecast_yr)
            forecast_div_per_sh_pre_val_arr.append(forecast_div_per_sh_pre_val)
        div_present_val.append(forecast_div_per_sh_pre_val_arr)

    term_int_val_per_sh_arr = []
    pre_int_val_per_sh_arr = []
    p_ddm_arr = []
    for yr in range(num_yr - 1):
        term_int_val_per_sh = (div_per_sh_arr[forecast_tot_yr][yr] * (1 + gordon_arr[yr])) / (exp_return_a[yr] - gordon_arr[yr])
        print(div_per_sh_arr[forecast_tot_yr][yr])

        pre_div_per_sh_tot = 0
        for forecast_yr in range(forecast_tot_yr - 1):
            pre_div_per_sh_tot += div_present_val[forecast_yr][yr]
        pre_int_val_per_sh = (term_int_val_per_sh / ((1 + exp_return_a[yr]) ** forecast_tot_yr)) + pre_div_per_sh_tot
        p_ddm = sh_price_arr[yr] / pre_int_val_per_sh

        term_int_val_per_sh_arr.append(term_int_val_per_sh)
        pre_int_val_per_sh_arr.append(pre_int_val_per_sh)
        p_ddm_arr.append(p_ddm)

    # print(term_int_val_per_sh_arr)
    # print(pre_int_val_per_sh_arr)
    # print(sh_price_arr)
    return p_ddm_arr



