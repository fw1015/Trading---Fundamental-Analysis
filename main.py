from urllib.request import urlopen
import certifi
import json
from excel import create_excel

from financial_ratios.financial_score import financial_score_analysis
from investment_valuation_ratios.investment_valuation_score import investment_valuation_score
from cost_of_equity_debt_and_capital.cost_of_equity_debt_captial_score import *
from stock_valuation_models.stock_valuation_models_score import *

# API = "eb9f749f26aab3bd40dd487d63fcf214"
API = "5192dd9a5d728d7b425e2ba96378e602"
target_ticker = "AAPL"
tickers_arr = ["AAPL", "BEP", "TSLA"]
fin_Statements = ["income-statement", "balance-sheet-statement", "cash-flow-statement", "enterprise-values"]

# ticker_urls = {ticker : [Income Statement URL, Balance Sheet URL, Cash Flow Statement URL]}
ticker_urls = {}

def tickers_urls():
    for ticker in tickers_arr:
        statement_url_list = []
        for statement in fin_Statements:
            statement_url_list.append(f"https://financialmodelingprep.com/api/v3/{statement}/{ticker}?limit=120&apikey={API}")
        # statement_url_list.append(f"https://financialmodelingprep.com/api/v3/enterprise-values/{ticker}?limit=40&apikey={API}")
        ticker_urls[ticker] = statement_url_list
    return ticker_urls

def get_statement_json_data(ticker, statement, num_yr):
    if statement == "Income Statement":
        index = 0
    elif statement == "Balance Sheet":
        index = 1
    elif statement == "Cash Flow Statement":
        index = 2
    else:
        index = 3
    company_stat_json_url = tickers_urls()[ticker][index]
    response = urlopen(company_stat_json_url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    stat_dict = refine_search_date(json.loads(data))
    # LOOKING AT 6 YEARS OR ALL YEAR
    if num_yr == 0:
        total_year = len(stat_dict)
        if total_year < 40:
            end_index = total_year - 1
        else:
            # From 1981 - 2020
            end_index = 39
    else:
        end_index = num_yr
    stat = stat_dict[0 : end_index]
    return stat

def refine_search_date(json):
    date = json[0]["date"]
    stat_dict = json
    if "2021" in date:
        stat_dict.pop(0)
    return stat_dict

# tickers_statements = {ticker : [[Income Statement], [Balance Sheet], [Cash Flow Statement]]}
def creat_tickers_statements_dict(tickers_arr, num_yr):
    tickers_statements_dict = {}
    for ticker in tickers_arr:
        inc = get_statement_json_data(ticker, "Income Statement", num_yr)
        bal = get_statement_json_data(ticker, "Balance Sheet", num_yr)
        csh = get_statement_json_data(ticker, "Cash Flow Statement", num_yr)
        ent_val = get_statement_json_data(ticker, "Enterprise Value", num_yr)
        tickers_statements_dict[ticker] = [inc, bal, csh, ent_val]
    return tickers_statements_dict

tickers_statement_dict = creat_tickers_statements_dict(tickers_arr, 6)
create_excel(target_ticker, tickers_arr, tickers_statement_dict)

# score = financial_score_analysis(tickers_arr, 5, tickers_statement_dict)
# print(score.calc_score(target_ticker))

# tickers_statement_dict = creat_tickers_statements_dict(tickers_arr, 6)
# score = investment_valuation_score(tickers_arr, tickers_statement_dict)
# print(score.calc_score(target_ticker))
#
#
# tickers_statement_dict = creat_tickers_statements_dict(tickers_arr, 0)
# score = stock_valuation_models_score(target_ticker, 6, tickers_statement_dict)
# print(score.calc_ratio())






