import graphing_model.config_fetch as cf
import pandas as pd

def wind_hh():
    wind_hh_fetched = cf.fetch_bmrs("datasets/FUELHH", settlementDateFrom=cf.start_date, settlementDateTo=cf.end_date,fuelType="WIND")
    # wind_hh.to_csv("wind.csv")
    wind_hh_fetched['startTime'] = pd.to_datetime(wind_hh_fetched['startTime'])
    return wind_hh_fetched

def wind_for_hh():
    wind_for_hh_fetched = cf.fetch_bmrs("forecast/generation/wind/latest", **{"from": cf.start_date, "to": cf.end_date+"T23:30:00Z"})
    wind_for_hh_fetched['startTime'] = pd.to_datetime(wind_for_hh_fetched['startTime'])
    return wind_for_hh_fetched