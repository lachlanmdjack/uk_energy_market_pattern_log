"Ships and Storage : The Global Gas Market" by Jordan Dimov:
-
> - 40% of UK gas is from Norwegian oil pipes (via St Fergus), the remaining 60% is from European interconnectors (via Bacton) and US (and other) LNG imports (via Milford Haven).
> Henry Hub fundamentals
> - UK and EU gas markets (NBP and TTF) lag the US Henry Hub LNG price movements by 6-8 weeks, when US markets fall it becomes more profitable to ship to European markets (arbitrage between NBP and Henry Hub, less shipping costs). This lag is 6-8 weeks from 2-3 weeks of physical LNG shipping + 4-5 weeks of logistics and scale. Conversely, when prices fall cargo is diverted to Asia. As such, sensitivity is directly tied to cargo charter rates (higher charter rates divert away from Europe). 
> LNG is the marginal source of gas
> - Norwegian and interconnector flows change slowly to seasonal changes as volume is committed to from long-term contracts, whereas LNG imports are highly reactive to price signals so become the price-setting mechanism in the UK.
> - LNG gas is traded via energy (therms), not volume (m3) as different fields have different heating values (MJ/m3, Btu/scf). Gas fields are lower than Shale, US gas fields are higher than Norwegian gas fields. UK terminals must bring the gas to within specificication (38.2 to 42 MJ/m3, impurities %) via blending or repricing the commodity (which can make Asian markets more or less favourable).
> LNG shipping costs
> - LNG transportation is formed of 1) liquefaction (\$2.50/MMBtu), 2) Shipping (based on cargo charter rates), and 3) regasification (\$0.40/MMBtu). Transportation across the Atlantic can take ~30 days, and charter costs can be ~$1/MMBtu (depending on cost per day and size).
>   - Shipping rates are highly volatile across season (5x swing from summer to winter) and logistics (congestion, rerouting and repositioning), and give way to arbitrage opportunity with 'floating storage' from season-to-season. 
>   - Asian shipping to JKM takes ~25 days from the US, so have a higher shipping stack than Europe. If there is equal prices, the Asian kickback (price less shipping stack) will be lower.
> Gas storage
> - UK has minimal gas storage (2% of annual demand), so is heavily reliant on LNG and pipeline imports throughout winter. Europe does have high gas storage (20% of annual demand), so NBP and TTF can decouple and not track each other in tight UK conditions despite an interconnector, especially if LNG terminals are at capacity and pipelines do not react to demand signals. Each gas storage location has maximum flow rates, so winter demand spikes must be supported by LNG if the requirement is greater than storage flow rates. 
> - Contracting storage introduces storage fees for short term arbitrage traders, but for long term traders/facility owners with sunk cost storage fees the price swing between summer and winter for profitability is much smaller, just injection and withdrawal fees. Alternatively, it can be used for a financial option hedge rather than taking advantage of seasonal-spread trading. 
> - Policy regimes can force flows - EU storage mandate can create force buyers and cause backwardation, pushing summer prices up and winter down. 

concept to come back to: "The result: NBP spiked while TTF stayed subdued. Traders who were long TTF and short NBP (betting on convergence) lost money as the basis widened instead of narrowing."

"The Spark Spread: A Trader’s Guide to Power Plant Economics" by Jordan Dimov, 
-
These are some key concepts that relate to the optionality provided to gas powered CCGTs:
> - During times of positive (clean) spark spread, plants _have the right but not obligation_ to turn gas + carbon taxes into electricity.
> - CSS = Ppower− (Pgas × H)− (Pcarbon × E) = Ppower - (Pgas * 0.3412) - (Pcarbon * 0.394)
> - UK carbon costs comprise of UKA + Carbon Price Support (£18/tonne)
> - As natural gas is significantly more liquid than power, price discovery on power is easier whilst using updated gas prices + the spark spread, held constant. 
> - Gas turbines can hedge future profitability via selling power futures and buying gas futures simultaneously, guaranteeing spark at a future date. 
> - Gas plants may be unhedged during times of negative spark spread, and will operate at a loss. 
> - Gas plants may choose to operate in periods of negative spark spread due to subsidies by NESO, extraordinarily high start-up costs (fuel + mechanical wear), if they have 'take-or-pay' contracts where gas is pre-bought and the marginal cost is effectively 0p/th. 
> - Spark spread cannot be hedged individually, but is a component of 1 MWh of power, 2.035MWh of gas, and 0.394 units of carbon allowance.


"Position Aggregation & Delta Exposure | Energy Trading" by Jordan Dimov:
-
> - Positions can only aggregate by commodity (product + location), delivery period + _book_ (via ownership, and tags as analytical).
> - Physical trades involve delivery of the prodct, whereas financial trades are settled based on reference prices, used within the hedge book to mitigate risk and arbitrage opportunity via swaps, futures and cfds.
> - Books aggregated by physical/financial analytics is highly rigid, whereas those grouped by ownership can enable trades that are cross-portfolio - deliverying physical produced indexed against financial instruments. 
> - $Delta = (+Physical Long) + (−Hedge Short) = Net Unhedged$, net sensitivity to price movements. 
> - $Hedge Coverage = |financial position| / |hedge position| * 100%$, exposure to market risk (strategic), and $Hedge Ratio = |financial position + hedge position| / |natural exposure| * 100%$, exposure to basis risk (operational)
> - Risk limits may be derived from above (i.e. hedge coverage must be 70%+, maximum delta exposure within a month is £50k)
> - "Build granular, store granular, display aggregated"
> - Basis risk is the risk that hedges don't move perfectly with physical exposure (settle or changing exposures due to different reference prices, delivery times, or locations). 
>   - Physical may settle at Heren DA, whereas financial (price hub) at Argus DA, where Heren and Argus may not move exactly the same.  
>   - Gas terminal prices may vary from NBP on day of due to physical constraints, misaligning physical and financial hedges 


"Mark-to-Market, Profit and Loss | Building Your Own P&L Calculation" by Jordan Dimov:
-
> - Mark-to-market shows the difference between what trades were traded at against what they are valued at today, showing unrealised gains/losses. Tracking MtM allows for risk reporting and limits (e.g. unrealised mark-to-market P&L swing of £500 per day) and process performance tracking.
> - The MtM for physical and hedge books should be inverse, demonstrating the hedges work (profit in physical offset by loss in hedge).
> - Value at Risk (VaR) is a reasonable 'worst case scenario' based on unhedged volume's market exposure, typically p90 or p95 movement levels. 
>
> $MtM = (PRICEmarket - PRICEtrade) * Net Position$

Trading Opportunities
- 
> - Understanding GMAR assumptions and basis risks, and identify where basis risk spreads are increasing to take action to lock in margin/ prevent increased losses. 
> - Building: Choleksy decomposition of historical covariance matrix for GMAR - importance is on that in shocks the gas + power + carbon are likely to move together not independently. Additionally, there are mean-reverting stochastic shocks + long term trends.
> - Understanding: What is the response to model outputs, do I agree with the assumptions that have gone into it.
> 

MA50196
https://people.bath.ac.uk/masmdp/findir.bho/50196.html