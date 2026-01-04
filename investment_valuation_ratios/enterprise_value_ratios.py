# ENTERPRISE VALUE RATIOS
# [[ENTERPRISE VALUE TO EBIT RATIO],
# [ENTERPRISE VALUE TO EBITDA RATIO]]

def en_val_ratios(income_statement, enterprise_value, num_yr):

    en_val_ratios = []
    ev_ebit_arr = []
    ev_ebitda_arr = []

    for yr in range(num_yr):
        yr_inc = income_statement[yr]
        yr_ev = enterprise_value[yr]

        en_v = yr_ev["enterpriseValue"]

        ebitda = yr_inc["ebitda"]
        depre_amort = yr_inc["depreciationAndAmortization"]
        ebit = ebitda - depre_amort

        # ENTERPRISE VALUE / EBIT
        ev_ebit = en_v / ebit
        ev_ebit_arr.append(ev_ebit)

        # ENTERPRISE VALUE / EBITDA
        ev_ebitda = en_v / ebitda
        ev_ebitda_arr.append(ev_ebitda)

    en_val_ratios.append(ev_ebit_arr)
    en_val_ratios.append(ev_ebitda_arr)

    return en_val_ratios
