import graphing_model.config_fetch as cf
import pandas as pd

def interconnector_hh():
    interconnector_hh_fetched = cf.fetch_bmrs("generation/outturn/summary", startTime=cf.start_date, endTime=cf.end_date+"T23:30:00", includeNegativeGeneration=True)
    i_exploded = interconnector_hh_fetched.explode("data").reset_index(drop=True)
    i_normalised = pd.json_normalize(i_exploded["data"])
    i_finalised = pd.concat([i_exploded.drop(columns="data"), i_normalised], axis=1)
    i_finalised['startTime'] = pd.to_datetime(i_finalised['startTime'])
    return  i_finalised[i_finalised["fuelType"].isin(["INTELEC","INTFR","INTGRNL","INTIFA2","INTNED","INTNEM","INTVKL","INTEW","INTIRL","INTNSL"])]
    # i_finalised.to_csv("interconnector.csv")

def sum_interconnector_hh():
    df = interconnector_hh()
    agg_df = df.groupby(['startTime', 'settlementPeriod'], as_index=False)['generation'].sum()
    return agg_df