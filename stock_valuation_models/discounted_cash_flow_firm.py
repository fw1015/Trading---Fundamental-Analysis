from financial_ratios.profitability_ratios import *
from cost_of_equity_debt_and_capital.weighted_average_cost_captial import wacc as wacc_func

# FORECAST MODEL
# +1 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +2 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +3 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +4 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +5 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]

def discounted_cash_flow_f(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    profit_arr = profit_analysis(income_statement, balance_sheet, cashflow_statement, num_yr)
    wacc_arr = wacc_func(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr)

    roic = profit_arr[5]
    market_val_eq = wacc_arr[2]
    wacc = wacc_arr[6]

    free_csh_firm_arr = []
    prat_arr = []
    single_stage_arr = []
    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]
        yr_csh = cashflow_statement[yr]

        net_inc = yr_inc["netIncome"]
        div_paid = - yr_csh["dividendsPaid"]
        int_exp = yr_inc["interestExpense"]
        inc_tax = yr_inc["incomeTaxExpense"]
        ebt = yr_inc["incomeBeforeTax"]
        eff_tax = inc_tax / ebt

        retention_r = (net_inc - div_paid) / (net_inc + int_exp * (1 - eff_tax))
        prat = retention_r * roic[yr]

        free_csh = yr_csh["freeCashFlow"]
        free_csh_firm = free_csh - int_exp * (1 - eff_tax)
        single_stage = (market_val_eq[yr] * wacc[yr] - free_csh_firm) / (market_val_eq[yr] + free_csh_firm)

        free_csh_firm_arr.append(free_csh_firm)
        prat_arr.append(prat)
        single_stage_arr.append(single_stage)

    fcff_growth_rate_H_model = [prat_arr]
    fcff_arr = [free_csh_firm_arr]
    fcff_present_val = []

    forecast_tot_yr = 5
    for forecast_yr in range(1, forecast_tot_yr - 1):
        forecast_fcff_gr_arr = []
        for yr in range(num_yr - 1):
            forecast_fcff_gr = prat_arr[yr] + (((single_stage_arr[yr] - prat_arr[yr]) * (forecast_yr)) / (forecast_tot_yr - 1))
            forecast_fcff_gr_arr.append(forecast_fcff_gr)
        fcff_growth_rate_H_model.append(forecast_fcff_gr_arr)
        fcff_growth_rate_H_model.append(single_stage_arr)

    for forecast_yr in range(forecast_tot_yr):
        forecast_fcff_arr = []
        for yr in range(num_yr - 1):
            forecast_fcff = fcff_arr[forecast_yr][yr] * (1 + fcff_growth_rate_H_model[forecast_yr][yr])
            forecast_fcff_arr.append(forecast_fcff)
        fcff_arr.append(forecast_fcff_arr)

    for forecast_yr in range(1, forecast_tot_yr):
        forecast_fcff_pre_val_arr = []
        for yr in range(num_yr - 1):
            forecast_fcff_pre_val = fcff_arr[forecast_yr][yr] / ((1 + wacc[yr]) ** forecast_yr)
            forecast_fcff_pre_val_arr.append(forecast_fcff_pre_val)
        fcff_present_val.append(forecast_fcff_pre_val_arr)
    return fcff_present_val



