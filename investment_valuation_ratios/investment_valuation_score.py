from investment_valuation_ratios.price_ratios import *
from investment_valuation_ratios.enterprise_value_ratios import *
from investment_valuation_ratios.yield_ratios import *
from investment_valuation_ratios.investment_scores_comparison import *

class investment_valuation_score:
    def __init__(self, tickers_arr, target_yr, tickers_statement_dict):
        self.tickers_arr = tickers_arr
        self.tickers_statement_dict = tickers_statement_dict
        self.target_yr = target_yr
        self.year = (len(list(tickers_statement_dict.values())[0][0]))

    def calc_ratio(self, income_statement, balance_sheet, cashflow_statement, enterprise_value):
        price_r = price_ratios(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        ev_val_r = en_val_ratios(income_statement, enterprise_value, self.target_yr)
        yield_r = yield_ratios(income_statement, cashflow_statement, enterprise_value, self.target_yr)
        return [price_r, ev_val_r, yield_r]

    def create_dict(self):
        # tickers_r_dict = {ticker : [[price_r], [ev_val_r], [yield_r]]}
        tickers_r_dict = {}
        index = 0
        for ticker in self.tickers_statement_dict:
            income_statement = self.tickers_statement_dict[ticker][0]
            balance_sheet = self.tickers_statement_dict[ticker][1]
            cashflow_statement = self.tickers_statement_dict[ticker][2]
            enterprise_value = self.tickers_statement_dict[ticker][3]
            ticker_r = self.calc_ratio(income_statement, balance_sheet, cashflow_statement, enterprise_value)
            tickers_r_dict[self.tickers_arr[index]] = ticker_r
            index += 1
        return tickers_r_dict

    def calc_score(self, target):
        tickers_ratios = self.create_dict()
        score = inv_sc_compare(target, tickers_ratios, self.year)
        return score