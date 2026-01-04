# OPERATING ACTIVITY RATIOS
# [[INVENTORY TURNOVER],
# [RECEIVABLES TURNOVER],
# [PAYABLES TURNOVER],
# [INVENTORY PERIOD],
# [RECEIVABLES COLLECTION PERIOD (DAYS SALES OUTSTANDING)],
# [PAYABLES PERIOD],
# [CASH CONVERSION CYCLE]

def op_analysis(income_statement, balance_sheet, num_yr):
    # year = len(income_statement)
    op_act_ratios = []

    inv_turnover_arr = []
    rec_turnover_arr = []
    pay_turnover_arr = []
    ccc_arr = []

    # DATA 5 YEARS AVERAGE
    # AVERAGE INVENTORY, AVERAGE ACCOUNT RECEIVABLES, AVERAGE ACCOUNT PAYABLES
    av_inv_arr = []
    av_ac_receivables_arr = []
    av_ac_payables_arr = []
    for yr in range(num_yr - 1):
        yr_bal = balance_sheet[yr]
        nxt_yr_bal = balance_sheet[yr + 1]

        # AVERAGE INVENTORY
        av_inv_arr.append((yr_bal["inventory"] + nxt_yr_bal["inventory"]) / 2)

        # AVERAGE ACCOUNT RECEIVABLES
        av_ac_receivables_arr.append((yr_bal["netReceivables"] + nxt_yr_bal["netReceivables"]) / 2)

        # AVERAGE ACCOUNT PAYABLES
        av_ac_payables_arr.append((yr_bal["accountPayables"] + nxt_yr_bal["accountPayables"]) / 2)

    print(av_inv_arr)
    # INVENTORY TURNOVER, RECEIVABLES TURNOVER, PYABLES TURNOVER
    for yr in range(num_yr - 1):
        yr_inc = income_statement[yr]
        cog = yr_inc["costOfRevenue"]
        net_sales = yr_inc["revenue"]

        # INVENTORY TURNOVER
        inv_turnover = cog / av_inv_arr[yr]
        inv_turnover_arr.append(inv_turnover)

        # RECEIVABLES TURNOVER
        rec_turnover = net_sales / av_ac_receivables_arr[yr]
        rec_turnover_arr.append(rec_turnover)

        # PYABLES TURNOVER
        pay_turnover = cog / av_ac_payables_arr[yr]
        pay_turnover_arr.append(pay_turnover)

    op_act_ratios.append(inv_turnover_arr)
    op_act_ratios.append(rec_turnover_arr)
    op_act_ratios.append(pay_turnover_arr)

    # INVENTORY PROCESSING PERIOD
    inv_process_prd_arr = [365 / inv_turnover for inv_turnover in inv_turnover_arr]

    # RECEIVABLES COLLECTION PERIOD
    rec_collect_prd_arr = [365 / rec_turnover for rec_turnover in rec_turnover_arr]

    # PAYABLES PAYMENT PERIOD
    pay_payment_prd_arr = [365 / pay_turnover for pay_turnover in pay_turnover_arr]

    # CASH CONVERSION CYCLE
    for yr in range(num_yr - 1):
        ccc = inv_process_prd_arr[yr] + rec_collect_prd_arr[yr] - pay_payment_prd_arr[yr]
        ccc_arr.append(ccc)

    op_act_ratios.append(inv_process_prd_arr)
    op_act_ratios.append(rec_collect_prd_arr)
    op_act_ratios.append(pay_payment_prd_arr)
    op_act_ratios.append(ccc_arr)

    # history_avg = history_results(op_act_ratios)
    return op_act_ratios
