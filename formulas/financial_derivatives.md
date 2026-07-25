information sourced from 
https://people.bath.ac.uk/masmdp/findir.bho/50196.html

## Valuations

Where S(T) is the price S at time T, and K is the strike price

Short = $`S(T) - K`$

Long = $`K - S(T)`$

Bull = Expect prices to rise

Bear = Expect prices to fall

### Time valuation of cash
$$` A(t) = A0((1+R/m)^m)^t = A0 e^rt `$$

### Futures
Where K is the price of a futures contract

$$`K_{no~income} = S(0)e^{rt}`$$

$$`K_{single~income} = (S(0)+u)e^{rt}`$$

$$`K_{continuous~dividend} = S(0)e^{(r-q)t}`$$

$$`K_{discrete~dividend} = S(0)e^{rt} * \prod_{i=0}^n (1-Q_i)`$$

Due to arbitrage a futures contract $`K`$ should match the above, based on S(0), r and t. 

If the futures price should be lower than it actually is, ...
1. Take a short position in the futures (sell the product at T)
2. Borrow cash for the period
3. Buy the asset
4. Sell the asset at time T for more than the future short (and neutralise the earlier short)

If the futures price should be higher than it actually is (actual is too low), one can...
1. Take a long position in the futures (buy the product at T)
2. Short sell the asset
3. Invest the cash for the period
4. Pay for delivery of the long position for less than the future long (and neutralise the earlier long)

## Options
Call (C) is..., with a payoff of $`C = (S(T) - K)^+`$

Put (P) is...
, with a payoff of $`P = (K- S(T))^+`$

|                        |                                                                                     Call                                                                                     |                                                                           Put                                                                           |
|------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Upper Bound            |                                              $`C\le S(0)`$  <br> Otherwise sell call, buy stock, and hand stock over for profit                                              |                                    $`P\le Ke^{-rt}`$  <br> Otherwise sell put, invest and buy for less than invested                                    |
| Lower Bound            | $`C\ge S(0)-Ke^{-rt}`$ <br> Otherwise sell 1 unit of stock, buy the call and invest money. <br> May exercise call via the investment and use it to return the shorted stock. | $`P\ge Ke^{-rt}-S(0)`$ <br> Otherwise borrow money, buy 1 put + 1 sotck, wait and exercise one. <br> May exercise call to repay loan and pocket profit. |

A long position can be made from buying 1 call and selling 1 put, a bull spread.

A short position ca be made from buying 1 put and selling 1 call, a bear spread.

### Put-Call parity
$$`C + Ke^{-rT} = P + S(0)`$$

i.e. 1 call + cash worth $`Ke^{-rT}`$ is the same as 1 put and 1 unit of underlying stock

If the Call + Cash < Put + Asset, 
1. Sell a put and short sell assets
2. Buy a call and invest cash at rate r
3. Net profit is $`P+S(0)-C-Ke^{rT}`$, which will be positive

If the Call + Cash > Put + Asset, 
1. Sell a call and borrow cash at rate r
2. Buy a put and invest in asset
3. Net profit is $`C+Ke^{rT}P-S(0)`$, which will be positive

### Black Scholes for Brownian Stocks

If a stock $`S`$ follows a geometric brownian motion, then the current derivative value is the (expected) future value decayed by time, 

$$
B = Ke^{-erT} = E[f(S(T))]~e^{-rT}
$$

Therefore, for a call and put option,

$$
P = \tilde E~[f(S(T))]e^{-rT} =~...~= Ke^{-rT}\Phi(y_0) ~-~ S(0)\Phi(y_1)
$$

$$
C = \tilde E~[f(S(T))]e^{-rT} =P + S - Ke^{-rT} = S(0)\Phi(x_1) ~-~ Ke^{-rT}\Phi(x_0)
$$

where
$`y_0 = -x_0 = \frac{log\frac{K}{S(0)}-(r-\frac{\sigma}{2}^2)T}{\sigma \sqrt{T}}`$ and $`y_1 = -x_1 = \frac{log\frac{K}{S(0)}-(r+\frac{\sigma}{2}^2)T}{\sigma \sqrt{T}}`$


## The greeks

Delta, the derivative's price sensitivity to the change in the price of the underlying asset: 
$$\Delta = \frac{df}{dS}$$

Gamma, the derivative's delta sensitivity to the change in the price of an underlying asset: $$`\Gamma = \frac{d^2f}{dS^2} = \frac{d\Delta}{dS}`$$

Vega, the derivative's price sensitivity to the volatility of the price of the underlying asset: $$`\mathcal{V} = \frac{df}{d\sigma}`$$

Theta, the derivative's price sensitivity to time: $$`\Theta = \frac{df}{dt}`$$

Rho, the derivative's price sensitivity to interest rates: $$`\rho = \frac{df}{dr}`$$

$$\delta f = f(t+\delta t, S+\delta S, \sigma + \delta \sigma) = f(t,S,\sigma) = \Theta \delta t + \Delta \delta S + \mathcal{V} \delta \sigma + \frac{1}{2} \Gamma (\delta S)^2$$
