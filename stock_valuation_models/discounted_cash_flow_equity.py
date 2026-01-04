from financial_ratios.profitability_ratios import *
from investment_valuation_ratios.yield_ratios import *
from cost_of_equity_debt_and_capital.capital_asset_pricing_model import *
from cost_of_equity_debt_and_capital.weighted_average_cost_captial import wacc as wacc_func

# FORECAST MODEL
# +1 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +2 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +3 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +4 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]
# +5 YEAR FORECAST [[YEAR 5, YEAR 4, YEAR 3, YEAR 2, YEAR 1]]

def discounted_cash_flow_eq(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    yield_r_arr = yield_ratios(income_statement, cashflow_statement, enterprise_value, num_yr)
    profit_arr = profit_analysis(income_statement, balance_sheet, cashflow_statement, num_yr)
    wacc_arr = wacc_func(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr)
    exp_return = capm(income_statement, cashflow_statement, enterprise_value, num_yr)

    div_payout = yield_r_arr[2]
    roe = profit_arr[3]
    market_val_eq = wacc_arr[2]
    exp_return_a = exp_return[0]

    free_csh_eq_arr = []
    prat_arr = []
    single_stage_arr = []
    for yr in range(num_yr - 1):
        yr_csh = cashflow_statement[yr]

        csh_fin_act = yr_csh["netCashUsedProvidedByFinancingActivities"]
        common_stock_re = yr_csh["commonStockRepurchased"]
        common_stock_issued = yr_csh["commonStockIssued"]
        free_csh = yr_csh["freeCashFlow"]

        other_csh_fin_act = csh_fin_act - common_stock_re - common_stock_issued
        free_csh_eq = free_csh + other_csh_fin_act

        prat = (1 - div_payout[yr]) * roe[yr]
        single_stage = (market_val_eq[yr] * exp_return_a[yr] - free_csh_eq) / (market_val_eq[yr] + free_csh_eq)

        free_csh_eq_arr.append(free_csh_eq)
        prat_arr.append(prat)
        single_stage_arr.append(single_stage)

    fcfe_growth_rate_H_model = [prat_arr]
    fcfe_arr = [free_csh_eq_arr]
    fcfe_present_val = []

    forecast_tot_yr = 5
    for forecast_yr in range(1, forecast_tot_yr - 1):
        forecast_fcfe_gr_arr = []
        for yr in range(num_yr - 1):
            forecast_fcfe_gr = prat_arr[yr] + (((single_stage_arr[yr] - prat_arr[yr]) * (forecast_yr)) / (forecast_tot_yr - 1))
            forecast_fcfe_gr_arr.append(forecast_fcfe_gr)
        fcfe_growth_rate_H_model.append(forecast_fcfe_gr_arr)
        fcfe_growth_rate_H_model.append(single_stage_arr)

    for forecast_yr in range(forecast_tot_yr):
        forecast_fcfe_arr = []
        for yr in range(num_yr - 1):
            forecast_fcfe = fcfe_arr[forecast_yr][yr] * (1 + fcfe_growth_rate_H_model[forecast_yr][yr])
            forecast_fcfe_arr.append(forecast_fcfe)
        fcfe_arr.append(forecast_fcfe_arr)

    for forecast_yr in range(1, forecast_tot_yr):
        forecast_fcfe_pre_val_arr = []
        for yr in range(num_yr - 1):
            forecast_fcfe_pre_val = fcfe_arr[forecast_yr][yr] / ((1 + exp_return_a[yr]) ** forecast_yr)
            forecast_fcfe_pre_val_arr.append(forecast_fcfe_pre_val)
        fcfe_present_val.append(forecast_fcfe_pre_val_arr)
    return fcfe_present_val



