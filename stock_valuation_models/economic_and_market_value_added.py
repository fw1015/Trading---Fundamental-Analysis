from cost_of_equity_debt_and_capital.weighted_average_cost_captial import wacc as wacc_func
from financial_ratios.profitability_ratios import *

def econ_market_val(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    wacc_arr = wacc_func(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr)
    profit_arr = profit_analysis(income_statement, balance_sheet, cashflow_statement, num_yr)

    roic = profit_arr[5]
    wacc = wacc_arr[6]
    av_inv_cap = wacc_arr[3]
    market_val_added = wacc_arr[2]

    econ_market_arr = [[]]
    econ_val_arr = []
    market_val_arr = []
    for yr in range(len(wacc)):
        yr_inc = income_statement[yr]
        econ_val_added = (roic[yr] - wacc[yr]) * av_inv_cap[yr]
        econ_spread = econ_val_added / av_inv_cap[yr]
        econ_profit_mgn = econ_val_added / yr_inc["revenue"]
        econ_val_arr.append(econ_val_added)

        ob_market_val_added = market_val_added[yr] - av_inv_cap[yr]
        ob_market_val_spread = ob_market_val_added / av_inv_cap[yr]
        ob_market_val_mgn = ob_market_val_added / yr_inc["revenue"]
        market_val_arr.append(ob_market_val_added)

    econ_market_arr.append(econ_val_arr)
    econ_market_arr.append(market_val_arr)
    econ_market_arr.pop(0)

    return econ_market_arr

