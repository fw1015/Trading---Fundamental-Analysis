from financial_ratios.operating_activity_ratios import *
from financial_ratios.investment_activity_ratios import *
from financial_ratios.liquidity_ratios import *
from financial_ratios.solvency_ratios import *
from financial_ratios.profitability_ratios import *
from financial_ratios.dupont_analysis import *
from financial_ratios.altman_z_score import *
from financial_ratios.piotroski_f_score import *
from financial_ratios.historic_results import *
from financial_ratios.financial_scores_comparison import *

class financial_score_analysis:
    # tickers_statements_dict = {ticker : [[Income Statement], [Balance Sheet], [Cash Flow Statement]]}
    def __init__(self, tickers_arr, target_yr, tickers_statement_dict):
        self.tickers_arr = tickers_arr
        self.tickers_statement_dict = tickers_statement_dict
        self.target_yr = target_yr
        print(tickers_statement_dict)

    def calc_ratio(self, income_statement, balance_sheet, cashflow_statement):
        op_act_r = op_analysis(income_statement, balance_sheet, self.target_yr)
        inv_act_r = inv_analysis(income_statement, balance_sheet, self.target_yr)
        liq_r = liq_analysis(balance_sheet, self.target_yr)
        sol_r = sol_analysis(income_statement, balance_sheet, self.target_yr)
        profit_r = profit_analysis(income_statement, balance_sheet, cashflow_statement, self.target_yr)
        du_pont = du_pont_anlysis(profit_r[2], inv_act_r[1], sol_r[2], self.target_yr)
        return [op_act_r, inv_act_r, liq_r, sol_r, profit_r]

    def create_dict(self, target):
        # tickers_r_dict = {ticker : [[op_act_r, inv_act_r, liq_r, sol_r, profit_r], [rating]]}
        tickers_r_dict = {}
        index = 0
        for ticker in self.tickers_statement_dict:
            income_statement = self.tickers_statement_dict[ticker][0]
            balance_sheet = self.tickers_statement_dict[ticker][1]
            cashflow_statement = self.tickers_statement_dict[ticker][2]
            enterprise_value = self.tickers_statement_dict[ticker][3]
            ticker_r = self.calc_ratio(income_statement, balance_sheet, cashflow_statement)

            if ticker == target:
                target_r = ticker_r
                target_rating = self.calc_rating(income_statement, balance_sheet, cashflow_statement, enterprise_value, target_r)
                tickers_r_dict[self.tickers_arr[index]] = [target_r, target_rating]
            else:
                tickers_r_dict[self.tickers_arr[index]] = ticker_r
            index += 1
        return tickers_r_dict

    def calc_score(self, target):
        tickers_ratios = self.create_dict(target)
        score = fin_sc_compare(target, tickers_ratios)
        return score

    def calc_rating(self, income_statement, balance_sheet, cashflow_statement, enterprise_value, fin_ratio):
        alt_z_sc = alt_z_score(income_statement, balance_sheet, enterprise_value, self.target_yr)
        pio_f_sc = pio_f_score(fin_ratio[4][4], fin_ratio[4][6], fin_ratio[3][3], fin_ratio[2][0], fin_ratio[4][0], fin_ratio[1][1],
                               income_statement, cashflow_statement, self.target_yr)
        return [alt_z_sc, pio_f_sc]