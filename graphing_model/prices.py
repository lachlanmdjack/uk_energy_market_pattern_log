import config_fetch as cf
import pandas as pd

def ssp_price():
    ssp_fetch = cf.fetch_bmrs("balancing/settlement/system-prices/"+cf.end_date)
    print(list(ssp_fetch))
    return ssp_fetch

def n2ex_price():
    n2ex_fetch = cf.fetch_bmrs("balancing/pricing/market-index", **{"from": cf.end_date+"T00:00Z", "to": cf.end_date+"T23:30Z"})
    print(list(n2ex_fetch))
    n2ex_pivoted = n2ex_fetch.pivot_table(
        index=['startTime', 'settlementDate', 'settlementPeriod'], 
        columns='dataProvider',
        values='price',
        aggfunc='first'  # or 'mean' if there could be duplicates per provider/period
    ).reset_index()
    print(n2ex_pivoted)

    return n2ex_pivoted

n2ex_price()