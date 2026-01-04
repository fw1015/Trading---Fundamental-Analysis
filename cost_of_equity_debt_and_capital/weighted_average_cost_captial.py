from cost_of_equity_debt_and_capital.capital_asset_pricing_model import *
import statistics
# WEIGHTED AVERAGE COST CAPITAL

def wacc(income_statement, balance_sheet, cashflow_statement, enterprise_value, num_yr):
    capm_arr = capm(income_statement, cashflow_statement, enterprise_value, num_yr)[0]

    wacc_all_arr = []
    tot_debt_arr = []
    market_val_eq_arr = []
    for yr in range(num_yr):
        yr_bal = balance_sheet[yr]
        commercial_paper = yr_bal["shortTermDebt"]
        cur_long_term_debt = yr_bal["otherCurrentLiabilities"]
        long_term_debt = yr_bal["longTermDebt"]
        tot_debt = commercial_paper + cur_long_term_debt + long_term_debt
        tot_debt_arr.append(tot_debt)

        yr_ev = enterprise_value[yr]
        en_v = yr_ev["enterpriseValue"]
        csh_csh_eq = yr_bal["cashAndCashEquivalents"]
        short_inv = yr_bal["shortTermInvestments"]
        market_val_eq = en_v - tot_debt + csh_csh_eq + short_inv
        market_val_eq_arr.append(market_val_eq)

    cost_of_debt_arr = []
    av_tot_debt_arr = []
    weight_eq_arr = []
    weight_dbt_arr = []
    wacc_arr = []
    for yr in range(num_yr - 1):
        av_tot_debt = statistics.mean(tot_debt_arr[yr:yr + 1])
        av_tot_debt_arr.append(av_tot_debt)

        int_exp = income_statement[yr]["interestExpense"]
        cost_of_debt = int_exp / av_tot_debt
        cost_of_debt_arr.append(cost_of_debt)

        weight_eq = market_val_eq_arr[yr] / (market_val_eq_arr[yr] + av_tot_debt)
        weight_eq_arr.append(weight_eq)

        weight_dbt = 1 - weight_eq
        weight_dbt_arr.append(weight_dbt)

        yr_inc = income_statement[yr]
        inc_tax = yr_inc["incomeTaxExpense"]
        ebt = yr_inc["incomeBeforeTax"]
        eff_tax = inc_tax / ebt

        wacc = (capm_arr[yr] * weight_eq) + (cost_of_debt * weight_dbt * (1 - eff_tax))
        wacc_arr.append(wacc)

    wacc_all_arr.append(capm_arr)
    wacc_all_arr.append(cost_of_debt_arr)
    wacc_all_arr.append(market_val_eq_arr)
    wacc_all_arr.append(av_tot_debt_arr)
    wacc_all_arr.append(weight_eq_arr)
    wacc_all_arr.append(weight_dbt_arr)
    wacc_all_arr.append(wacc_arr)

    return wacc_all_arr