from cost_of_equity_debt_and_capital.historical_asset_returns import *
from cost_of_equity_debt_and_capital.capital_asset_pricing_model import *
from cost_of_equity_debt_and_capital.fama_french_three_factors_model import *
from cost_of_equity_debt_and_capital.arbitrage_pricing_theory_model import *
from cost_of_equity_debt_and_capital.weighted_average_cost_captial import *

class cost_of_equity_debt_capital_score:
    def __init__(self, target, target_yr, tickers_statement_dict):
        self.target = target
        self.target_yr = target_yr
        self.target_statement_dict = tickers_statement_dict[self.target]

    def calc_ratio(self):
        income_statement = self.target_statement_dict[0]
        balance_sheet = self.target_statement_dict[1]
        cashflow_statement = self.target_statement_dict[2]
        enterprise_value = self.target_statement_dict[3]
        his = his_asset_returns(income_statement, cashflow_statement, enterprise_value, self.target, "normal", self.target_yr)
        s_n_p_his = his_asset_returns(income_statement, cashflow_statement, enterprise_value, "S&P500", "normal", self.target_yr)
        capm_re = capm(income_statement, cashflow_statement, enterprise_value, self.target_yr)
        three_fact_re = fama_french_three_factors_model(income_statement, cashflow_statement, enterprise_value, self.target_yr)
        arbit_price_re = arbitrage_pricing_theory_model(income_statement, cashflow_statement, enterprise_value, self.target_yr)
        wacc_re = wacc(income_statement, balance_sheet, cashflow_statement, enterprise_value, self.target_yr)
        return wacc_re