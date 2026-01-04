import pandas as pd
from sklearn import linear_model
from cost_of_equity_debt_and_capital.historical_asset_returns import *
# FAMA-FRENCH THREE FACTORS MODEL
# [[EXPECTED RETURN A],
# [EXPECTED RETURN B]]

def fama_french_three_factors_model(income_statement, cashflow_statement, enterprise_value, num_yr):
    min_year = min(len(income_statement), len(cashflow_statement), len(enterprise_value))
    yr_re = target_re(income_statement, cashflow_statement, enterprise_value, min_year)

    rf = market_r("rf", min_year - 1)

    target_rf_arr = []
    for i in range(len(yr_re)):
        target_rf = yr_re[i] - rf[i]
        target_rf_arr.append(target_rf)

    exp_re_a_arr = []
    exp_re_b_arr = []
    three_exp_re = [[]]

    skiprows = [0, 2]
    for yr in range(num_yr):
        nrows = min_year - (yr + 1)
        df = pd.read_excel("Market Historic Data.xlsx", sheet_name=2, skiprows=skiprows, nrows=nrows,
                           usecols=[1, 2, 3, 4, 5])
        df["Target_rf"] = target_rf_arr[yr:]

        reg = linear_model.LinearRegression()
        reg.fit(df[['Rm-Rf', 'SMB', 'HML']], df.Target_rf)

        market_beta = reg.coef_[0]
        size_beta = reg.coef_[1]
        style_beta = reg.coef_[2]

        exp_re_a = market_beta * df['Rm-Rf'].mean() + size_beta * df['SMB'].mean() + style_beta * df['HML'].mean() + df['Rf'].mean()
        exp_re_a_arr.append(exp_re_a)

        exp_re_b = exp_re_a + reg.intercept_
        exp_re_b_arr.append(exp_re_b)

        skiprows.append(3 + yr)

    three_exp_re.append(exp_re_a_arr)
    three_exp_re.append(exp_re_b_arr)

    three_exp_re.pop(0)

    return three_exp_re

def market_r(target, min_yr):
    rf = []

    wb = load_workbook(filename="Market Historic Data.xlsx")
    wb.active
    sheets = wb.sheetnames
    maket_risk_free = wb[sheets[2]]

    if target == "rf":
        for i in range(4, 4 + min_yr):
            rf.append(maket_risk_free[f"C{i}"].value)
        return rf
