import graphing_model.interconnectors as i
import graphing_model.renewable_generation as rg
import graphing_model.prices as p
import seaborn as sns
import matplotlib.pyplot as plt

def wind_forecast_vs_actual():
    wind_hh = rg.wind_hh()
    wind_for_hh = rg.wind_for_hh()
    sum_interconnector_hh=i.sum_interconnector_hh()

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=wind_hh, x='startTime', y='generation', sort=True, ax=ax, label='Actual')
    sns.lineplot(data=wind_for_hh, x='startTime', y='generation', sort=True, ax=ax, label='Forecast')
    sns.lineplot(data=sum_interconnector_hh, x='startTime', y='generation', sort=True, ax=ax, label='Interconnector')

    ax.set_title("Wind Generation: Actual vs Forecast")
    ax.set_xlabel("Time")
    ax.set_ylabel("Generation (MW)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

def prices_graph():
    ssp_price = p.ssp_price()
    n2ex_price = p.n2ex_price()
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=ssp_price, x='settlementPeriod', y='systemSellPrice', sort=True, ax=ax, label='SSP')
    sns.lineplot(data=n2ex_price, x='settlementPeriod', y='APXMIDP', sort=True, ax=ax, label='EPEX')
    sns.lineplot(data=n2ex_price, x='settlementPeriod', y='N2EXMIDP', sort=True, ax=ax, label='N2EX')

    for x, y in zip(ssp_price['settlementPeriod'], ssp_price['systemSellPrice']):
        ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 5), fontsize=7, ha='center')

    for x, y in zip(n2ex_price['settlementPeriod'], n2ex_price['APXMIDP']):
        ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 5), fontsize=7, ha='center')

    for x, y in zip(n2ex_price['settlementPeriod'], n2ex_price['N2EXMIDP']):
        ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 5), fontsize=7, ha='center')

    ax.set_title("Price Comparisons")
    ax.set_xlabel("Settlement Period")
    ax.set_ylabel("£/MWH")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()