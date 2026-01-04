from stock_valuation_models.economic_and_market_value_added import *
from stock_valuation_models.discounted_dividends import *
from stock_valuation_models.discounted_cash_flow_equity import *
from stock_valuation_models.discounted_cash_flow_firm import *

class stock_valuation_models_score:
    def __init__(self, target, target_yr, tickers_statement_dict):
        self.target = target
        self.target_yr = target_yr
        self.target_statement_dict = tickers_statement_dict[self.target]

    def calc_ratio(self):
        income_statement = self.target_statement_dict[0]
        balance_sheet = self.target_statement_dict[1]
        cashflow_statement = self.target_statement_dict[2]
        enterprise_value = self.target_statement_dict[3]
        econ_mark_val = econ_market_val(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        ddm = discounted_dividends(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        fcfe = discounted_cash_flow_eq(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        fcff = discounted_cash_flow_f(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        return ddm