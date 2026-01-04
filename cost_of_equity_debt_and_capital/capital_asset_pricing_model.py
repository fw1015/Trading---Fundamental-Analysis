import numpy as np
from scipy.stats import linregress
from cost_of_equity_debt_and_capital.historical_asset_returns import *
# CAPITAL ASSET PRICING MODEL
# [[EXPECTED RETURN A],
# [EXPECTED RETURN B]]

def capm(income_statement, cashflow_statement, enterprise_value, num_yr):
    min_year = min(len(income_statement), len(cashflow_statement), len(enterprise_value))
    yr_re = target_re(income_statement, cashflow_statement, enterprise_value, min_year)

    rf = market_r("rf", min_year - 1)
    rm_rf = market_r("rm_rf", min_year - 1)

    target_rf_arr = []
    for i in range(len(yr_re)):
        target_rf = yr_re[i] - rf[i]
        target_rf_arr.append(target_rf)

    exp_re_a_arr = []
    exp_re_b_arr = []
    capm_exp_re = [[]]

    for yr in range(num_yr):
        market_regress = linregress(rm_rf[yr:], target_rf_arr[yr:])
        jen_alpha = market_regress.intercept
        market_beta = market_regress.slope

        exp_re_a = market_beta * np.mean(rf[yr:]) + np.mean(rm_rf[yr:])
        exp_re_a_arr.append(exp_re_a)

        exp_re_b = jen_alpha + exp_re_a
        exp_re_b_arr.append(exp_re_b)

    capm_exp_re.append(exp_re_a_arr)
    capm_exp_re.append(exp_re_b_arr)

    capm_exp_re.pop(0)

    return capm_exp_re

def market_r(target, min_yr):
    rf = []
    rm_rf = []

    wb = load_workbook(filename="Market Historic Data.xlsx")
    wb.active
    sheets = wb.sheetnames
    maket_risk_free = wb[sheets[2]]

    if target == "rf":
        for i in range(4, 4 + min_yr):
            rf.append(maket_risk_free[f"C{i}"].value)
        return rf
    elif target == "rm_rf":
        for i in range(4, 4 + min_yr):
            rm_rf.append(maket_risk_free[f"D{i}"].value)
        return rm_rf
